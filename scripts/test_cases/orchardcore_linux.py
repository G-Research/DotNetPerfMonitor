"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild
Returns:
    None: .....
"""

import subprocess
import time
import os
import csv
import urllib.request
from datetime import datetime

EXTRACT_PATH = "sdk"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/253e5af8-41aa-48c6-86f1-39a51b44afdc/5bb2cb9380c5b1a7f0153e0a2775727b/dotnet-sdk-7.0.100-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"
TEST_SOLUTION_REPO_URL = "https://github.com/OrchardCMS/OrchardCore"
TEST_REPO_NAME = "OrchardCore"
TEST_SOLUTION_CASE = "OrchardCore"
TEST_SOLUTION_DIR = "./"
SDK_VERSION = "7.0.100"
SDK_DAILY_VERSION = "8.0.1xx"


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
    print('-----_restoting packages_-----')
    subprocess.run([dotnet_executable, 'restore'], check=True)
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


def camel_casify_solution_name(string):
    """This method converts a string to camel case"""
    parts = string.split('_')
    camel_case_parts = [part.capitalize() for part in parts[:-1]]
    return ''.join(camel_case_parts)


def print_csv_content(file_path):
    """Prints content of csv file for debugging purposes"""
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


def save_benchmark_results(file_path, benchmark_duration, benchmark_base_duration):
    """Saves bencharmk results to a csv file

    Args:
        file_path (_type_): _description_
    """
    # Get the benchmark results and create a row data
    # row_data = [version,base version,scenario,test case,timestamp,duration,base duration,relative duration]
    version = SDK_DAILY_VERSION
    base_version = SDK_VERSION
    timestamp = datetime.utcnow().isoformat(timespec='seconds')
    scenario = 'cold'
    test_case = 'OrchardCoreLinux'
    duration = benchmark_duration
    base_duration = benchmark_base_duration
    relative_duration = abs(base_duration - duration)
    benchmark_results = [version, base_version, scenario, test_case,
                         timestamp, duration, base_duration, relative_duration]

    with open(file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(benchmark_results)

    print_csv_content(file_path)


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

    msbuild_command = 'msbuild OrchardCore.sln'
    versions = ['base']
    duration_in_seconds = 0
    base_duration_in_seconds = 0
    for version in versions:
        # sub_dir = "/sdk" if version == 'daily' else ''
        exec_path = os.path.abspath(f"./../sdk/{version}/dotnet")
        run_build_to_restore_packages(exec_path)
        simple_command = "msbuild OrchardCore.sln"
        command = f"{exec_path} {simple_command}"
        elapsed_time = measure_execution_time(command)
        if version == 'base':
            base_duration_in_seconds = elapsed_time
        else:
            duration_in_seconds = elapsed_time
        print('-----🟠 ORCHARDCORE LINUX RESULT🟠-----')
        print(
            f"Running '{command}' with {version} version took {elapsed_time}s to execute.")

    # save benchmark results to a csv file
    save_benchmark_results('../../data/msbuild.csv.csv',
                           duration_in_seconds, base_duration_in_seconds)


if __name__ == "__main__":
    main()
