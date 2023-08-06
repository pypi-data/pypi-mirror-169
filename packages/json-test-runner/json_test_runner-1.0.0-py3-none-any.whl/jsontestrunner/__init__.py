__author__ = "mengjianhua"
__version__ = "1.0"

import datetime
import io
import json
import os.path
import unittest
from xml.sax import saxutils
import sys


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

# ----------------------------------------------------------------------
# Template

TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        super(_TestResult, self).__init__(verbosity=verbosity)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        # 增加一个测试通过率 --Findyou
        self.passrate = float(0)

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class Runner:
    """
    """

    def __init__(self, case_path=None, verbosity=1):
        self.STATUS = {
            0: '通过',
            1: '失败',
            2: '错误',
        }

        self.case = self.load_case(case_path)
        self.stream = {}
        self.verbosity = verbosity

        self.err_infos = []
        self.failed_infos = []

        self.startTime = datetime.datetime.now()
        self.stopTime = datetime.datetime.now()

    @staticmethod
    def load_case(case_path):
        if not os.path.exists(case_path):
            raise FileNotFoundError(f'{case_path} not found')
        case = unittest.TestSuite()
        case.addTest(unittest.defaultTestLoader.discover(case_path, pattern='*.py', top_level_dir=case_path))
        return case

    def run(self, testCase=None):
        """Run the given test case or test suite."""
        if not testCase:
            testCase = self.case
        result = _TestResult(self.verbosity)
        testCase(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(testCase, result)
        print('\nTime Elapsed: %s' % (self.stopTime - self.startTime), file=sys.stderr)
        return self

    def save(self, filepath):
        if os.path.isdir(filepath):
            filepath = os.path.join(filepath, 'report.json')
        print(f'save report file: {filepath}', file=sys.stderr)
        with open(filepath, 'w', encoding='u8') as f:
            f.write(json.dumps(self.stream, ensure_ascii=False))

    def get_err_or_failed_result(self):
        return len(self.err_infos) > 0 or len(self.failed_infos) > 0, self.err_infos, self.failed_infos

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if cls not in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def generateReport(self, test, result):
        self.stream = self._generate_report(result)

    def _generate_report(self, result):
        rows = []
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        self.passrate = str("%.2f%%" % (float(result.success_count) / float(
            result.success_count + result.failure_count + result.error_count) * 100))

        sortedResult = self.sortResult(result.result)
        err_result = []
        failed_result = []
        pass_result = []
        _driver = ''
        for cid, (cls, cls_results) in enumerate(sortedResult):

            # subtotal for a class
            np = nf = ne = 0

            for n, t, o, e in cls_results:

                if n == 0:
                    np += 1
                    pass_result.append([str(t), str(o), str(e)])
                elif n == 1:
                    nf += 1
                    failed_result.append([str(t), str(o), str(e)])
                else:
                    ne += 1
                    err_result.append([str(t), str(o), str(e)])

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__ or ""

            row = dict(
                style=ne > 0 and 'Error' or nf > 0 and 'Failed' or 'Pass',
                name=name,
                doc=doc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
                info=[],
            )
            for tid, (n, t, o, e) in enumerate(cls_results):
                row['info'].append(self._generate_report_test(cid, tid, n, t, o, e))
            rows.append(row)

        report = dict(
            test_list=rows,
            count=result.success_count + result.failure_count + result.error_count,
            Pass=result.success_count,
            fail=result.failure_count,
            error=result.error_count,
            passrate=self.passrate,
            start_time=startTime,
            stop_time=str(self.stopTime)[:19],
            duration=duration
        )

        self.err_infos = err_result
        self.failed_infos = failed_result

        return report

    def _generate_report_test(self, cid, tid, n, t, o, e):
        tid = (n == 0 and 'p' or 'f') + 't%s_%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        desc = t._testMethodDoc or ""

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):

            uo = o
        else:
            uo = o
        if isinstance(e, str):

            ue = e
        else:
            ue = e

        row = dict(
            index=t.id(),
            name=name,
            style=n == 2 and 'Error' or (n == 1 and 'Failed' or 'Pass'),
            desc=desc,
            script=saxutils.escape(uo + ue),
            status=self.STATUS[n]
        )
        return row


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = Runner()
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################


if __name__ == "__main__":
    main(module=None)
