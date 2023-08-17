import subprocess
import time
import sys
import os
import argparse


def measure_execution_time(command):
    # Record start time
    start_time = time.time()

    # Run the command
    subprocess.call(command, shell=True)

    # Calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time


def main(repo_url, repo_path, command):
    if repo_path and repo_url is not None:
        checkout_repository(repo_url, repo_path)
        os.chdir(repo_path)

    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time:.2f} seconds to execute.")
    return elapsed_time


if __name__ == "__main__":
    main()
