"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import subprocess
import time
import argparse


def measure_execution_time(command):
    """summary for measure_execution_time

    Args:
        command ([String]): [command to be executed]

    Returns:
        [Number]: [ellapsed time in seconds]
    """

    # Record start time
    start_time = time.time()

    # Run the command
    subprocess.call(command, shell=True)

    # Calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time


def clone_repository(repo_url, repo_path):
    """_summary_

    Args:
        repo_url (String): url of the repository to be cloned
        repo_path (String): path containing test code
    """

    # Clone the repository containing the solution
    subprocess.call(f"git clone {repo_url}", shell=True)
    subprocess.call(f"cd {repo_path}", shell=True)


def delete_clone(repo_url):
    """_summary_

    Args:
        repo_path (String): path containing test code
    """
    # extract the repository name from the url
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    subprocess.call(f"rm -rf {repo_name}", shell=True)


def main(operating_system, base_version_url, daily_version_url,
         solution_repo_url, solution_dir):
    """_summary_

    Returns:
        operating_system: operating system to be used to run the test
        base_version_url: dotnet sdk base version URL
        daily_version_url: dotnet sdk daily version URL
        solution_repo_url: test code repository URL
        solution_dir: directory of test code


    """

    # clone the repository and navigate to the solution directory
    clone_repository(solution_repo_url, solution_dir)

    # build the solution using the base version
    command = "dotnet build Solution.sln"
    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time}s to execute.")
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
    solution_repo_url = args.solution_repo_url
    solution_dir = args.solution_dir

    main(operating_system, base_version_url, daily_version_url,
         solution_repo_url, solution_dir)
