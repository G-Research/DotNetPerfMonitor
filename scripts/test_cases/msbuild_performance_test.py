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


def clone_repository(repo_url, repo_path):
    # Clone the repository containing the solution
    subprocess.call(f"git clone {repo_url}", shell=True)
    subprocess.call(f"cd {repo_path}", shell=True)


def delete_clone(repo_path):
    # extract the repository name from the url
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    subprocess.call(f"rm -rf {repo_name}", shell=True)


def main(operating_system, base_version_url, daily_version_url,
         solution_repo_url, solution_dir):

    # clone the repository and navigate to the solution directory
    clone_repository(solution_repo_url, solution_dir)

    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time:.2f} seconds to execute.")
    return elapsed_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="___measures the execution time of msbuild command___.")
    parser.add_argument("--os", required=True,
                        help="operating system to be used to run the test")

    parser.add_argument("--base-version-url", required=True,
                        help="dotnet sdk base version URL")
    parser.add_argument("--daily-version-url", required=True,
                        help="dotnet sdk daily version URL")
    parser.add_argument("--solution-repo-url", required=True,
                        help="test code repository URL")
    parser.add_argument("--solution-dir", required=True,
                        help="directory of test code")

    args = parser.parse_args()

    operating_system = args.os
    base_version_url = args.base_version_url
    daily_version_url = args.daily_version_url
    solution_repo_url = args.repo_url
    solution_dir = args.solution_dir

    main(operating_system, base_version_url, daily_version_url,
         solution_repo_url, solution_dir)
