"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import argparse
import subprocess
import time
import os

EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"


def back_to_previous_dir():
    """_summary_
    """
    subprocess.call(f"cd ..", shell=True)


def download_file(url, filename):
    """ Download file from url and save it to filename"""
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


def extract_zip(zip_file, extract_folder):
    """ Extracts zip file to extract_folder"""
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def extract_zip(zip_file, extract_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def download_and_extract_dotnet_sdk(version_url, is_base):
    """_summary_

    Args:
        version_url (String): dotnet sdk version url
    """
    path = f"{EXTRACT_PATH}/base" if is_base else f"{EXTRACT_PATH}/daily"
    download_file(url, os.path.basename(version_url))
    extract_zip(os.path.basename(version_url), path)
    # Download the dotnet sdk
    # if operating_system == "ubuntu-latest":
    #     subprocess.call(
    #         f"curl -O {version_url} -o dotnet-sdk.zip", shell=True)
    #     subprocess.call("tar -xf dotnet-sdk.zip", shell=True)

    # else:
    #     # means os is windows
    #     powershell_command = f"Invoke-WebRequest -Uri {version_url} -OutFile dotnet-sdk.zip"
    #     extract_command = "Expand-Archive -Path dotnet-sdk.zip -DestinationPath sdk"

    #     subprocess.call(f"powershell {powershell_command}", shell=True)
    #     subprocess.call(f"powershell {extract_command}", shell=True)


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
    # create a working directory for the test experiment
    subprocess.call(f"mkdir {WORKING_DIR}", shell=True)
    subprocess.call(f"cd {WORKING_DIR}", shell=True)
    # download and extract the dotnet sdk
    download_and_extract_dotnet_sdk(base_version_url)

    # clone the repository and navigate to the solution directory
    clone_repository(solution_repo_url, solution_dir)

    # build the solution using the base version
    exec_path = "../../sdk/base/dotnet.exe" if operating_system == "windows-latest" else "../sdk/base/dotnet"
    command = f"{exec_path} build Solution.sln"
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
