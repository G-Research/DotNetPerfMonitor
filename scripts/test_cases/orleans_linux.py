"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild
Returns:
    None: .....
"""

import subprocess
import time
import os
import urllib.request

EXTRACT_PATH = "sdk"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/dc930bff-ef3d-4f6f-8799-6eb60390f5b4/1efee2a8ea0180c94aff8f15eb3af981/dotnet-sdk-6.0.300-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"
TEST_SOLUTION_REPO_URL = "https://github.com/dotnet/orleans"
TEST_REPO_NAME = "orleans"
TEST_SOLUTION_CASE = "orleans"
TEST_SOLUTION_DIR = "./"


def create_extract_destinations():
    """ Create the extract destination directories if they do not exist"""
    if not os.path.exists(EXTRACT_PATH):
        os.mkdir(EXTRACT_PATH)
    os.chdir(EXTRACT_PATH)
    if not os.path.exists("base"):
        os.mkdir("base")
    if not os.path.exists("daily"):
        os.mkdir("daily")


def download_file(url, filename):
    """ Download file from url and save it to filename"""
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


def download_and_extract_dotnet_sdk(version_url, extract_path):
    """ Download and extract the dotnet sdk"""

    tar_gz_file = "dotnet-sdk.tar.gz"
    download_file(version_url, tar_gz_file)

    # Extract the tar.gz file
    # extract_command = f"tar -xzf {tar_gz_file} -C {extract_path}"
    subprocess.run(["tar", "-xzf", tar_gz_file,
                   "-C", extract_path], check=True)


def run_build_to_restore_packages(dotnet_executable):
    """_summary_

    Args:
        dotnet_executable (_type_): _description_
    """
    subprocess.run([dotnet_executable, 'build'], check=True)


def measure_execution_time(command):
    """measure_execution_time runs build command and measure its execution time"""

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
    os.chdir('..')
    subprocess.run(['git', 'clone', repo_url], check=True)
    os.chdir(TEST_REPO_NAME)
    os.chdir(TEST_SOLUTION_DIR)
    subprocess.run(['ls'], check=True)


def main():
    """_summary_
        main()

    """

    # create the extract destination directories if they do not exist
    create_extract_destinations()

    # download and extract the dotnet sdk

    download_and_extract_dotnet_sdk(DOTNET_BASE_VERSION_URL_LINUX, "base")
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_LINUX, "daily")

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_CASE)

    # build the solution using the base version

    msbuild_command = 'msbuild Orleans.sln'
    versions = ['base', 'daily']
    for version in versions:
        exec_path = os.path.abspath(f"./../sdk/{version}/dotnet")
        run_build_to_restore_packages(exec_path)
        simple_command = "msbuild Orleans.sln"
        command = f"{exec_path} {simple_command}"
        elapsed_time = measure_execution_time(command)
        print('-----🟠 ORLEANS LINUX RESULT 🟠-----')
        print(
            f"Running '{command}' with {version} version took {elapsed_time}s to execute.")


if __name__ == "__main__":
    main()
