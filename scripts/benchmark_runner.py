"""Run a benchmark and return the results."""
import argparse


def run_benchamrk():
    """_summary_
        run_benchmark()
    """


if __name__ == '__main__':
    # Parse arguments using argparse
    parser = argparse.ArgumentParser(
        description='---Benchmark Runner---')
    parser.add_argument('name', help='Name of the test case')
    parser.add_argument('results_file', help='File that stores the results')

    args = parser.parse_args()

    run_benchamrk()
