import argparse
import sys

from jsontestrunner import Runner


def main():
    args = argparse.ArgumentParser(description='json test runner')
    args.add_argument('--case_path', '-c', type=str, help='case path')
    parse = args.parse_args()
    if not parse.case_path:
        print('need case path!', file=sys.stderr)
        return
    Runner(case_path=parse.case_path, verbosity=2).run().save(parse.case_path)

