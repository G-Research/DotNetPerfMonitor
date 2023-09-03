"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild on windows
Returns:
    None: .....
"""

import subprocess
import time
import os

# ___ EXTRACTION CONSTANTS ___ #
EXTRACT_PATH = "sdk"

# _____ BENCHMARK DEPENDENCIES CONSTANTS _____ #

DOTNET_BASE_VERSION_URL_WINDOWS = "https://download.visualstudio.microsoft.com/download/pr/1fb808dc-d017-4460-94f8-bf1ac83e6cd8/756b301e714755e411b84684b885a516/dotnet-sdk-7.0.100-win-x64.zip"

DOTNET_DAILY_VERSION_URL_WINDOWS = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-win-x64.zip"

TEST_SOLUTION_REPO_URL = "https://github.com/OrchardCMS/OrchardCore"

TEST_REPO_NAME = "OrchardCore"
TEST_SOLUTION_CASE = "OrchardCore"
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
    subprocess.run(['powershell', 'Invoke-WebRequest', '-Uri',
                   url, '-OutFile', filename], check=True, shell=True)


def download_and_extract_dotnet_sdk(version_url, extract_path):
    """ Download and extract the dotnet sdk"""
    zip_file = "dotnet-sdk.zip"
    download_file(version_url, zip_file)

    # Extract the zip file
    subprocess.run(["powershell", "Expand-Archive", "-Path", zip_file,
                   "-DestinationPath", extract_path], check=True, shell=True)


def run_build_to_restore_packages(dotnet_executable):
    """_summary_

    Args:
        dotnet_executable (_type_): _description_
    """
    print('-----_restoting packages_-----')
    subprocess.run([dotnet_executable, 'restore'], check=True)
    subprocess.run([dotnet_executable, 'build'], check=True)


def measure_execution_time(command):
    """measure_execution_time runs build command and measure its execution time"""

    # run `build` to restore packages
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
    subprocess.run(['dir'], check=True)


def main():
    """_summary_
        main()

    """

    # create the extract destination directories if they do not exist
    create_extract_destinations()

    # download and extract the dotnet sdk

    download_and_extract_dotnet_sdk(DOTNET_BASE_VERSION_URL_WINDOWS, "base")
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_WINDOWS, "daily")

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_CASE)

    # build the solution using the base version

    msbuild_command = "msbuild OrchardCore.sln"
    versions = ['base', 'daily']
    for version in versions:
        sub_dir = "/sdk" if version == 'daily' else ''
        exec_path = os.path.abspath(f"./../sdk/{version}/dotnet{sub_dir}")
        run_build_to_restore_packages(exec_path)
        simple_command = "msbuild OrchardCore.sln"
        command = f"{exec_path} {simple_command}"
        elapsed_time = measure_execution_time(command)
        print('-----ORLEANS WINDOWS RESULT-----')
        print(
            f"Running '{command}' with {version} version took {elapsed_time}s to execute.")


if __name__ == "__main__":
    main()
