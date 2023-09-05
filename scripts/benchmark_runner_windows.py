"""Run a benchmark and return the results."""
import argparse
import zipfile
import subprocess
import time
import os
import urllib.request
import benchmark_utils as utils


def create_extract_destinations(path):
    """ Create the extract destination directories if they do not exist"""
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    if not os.path.exists("base"):
        os.mkdir("base")
    if not os.path.exists("daily"):
        os.mkdir("daily")


# def download_file(url, filename):
#     """ Download file from url and save it to filename"""
#     subprocess.run(['powershell', 'Invoke-WebRequest', '-Uri',
#                    url, '-OutFile', filename], check=True, shell=True)

def download_file(url, filename):
    """ Download file from url and save it to filename"""
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


def extract_zip(zip_file, extract_path):
    """Extract a zip file to the specified destination path."""
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


def download_and_extract_dotnet_sdk(version_url, extract_path):
    """ Download and extract the dotnet sdk"""
    zip_file = "dotnet-sdk.zip"
    download_file(version_url, zip_file)

    # Extract the zip file
    extract_zip(zip_file, extract_path)
    # subprocess.run(["powershell", "Expand-Archive", "-Path", zip_file,
    #                "-DestinationPath", extract_path], check=True, shell=True)


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


def clone_repository(repo_url, test_repo_name, test_repo_path, nested, test_solution_dir):
    """_summary_

    Args:
        repo_url (String): url of the repository to be cloned
        repo_path (String): path containing test code
    """
    # Clone the repository containing the solution
    os.chdir('..')
    subprocess.run(['git', 'clone', repo_url], check=True)
    os.chdir(test_repo_name)
    if nested:
        os.chdir(test_repo_path)
    os.chdir(test_solution_dir)
    subprocess.run(['dir'], check=True)


def run_benchamrk(args):
    """_summary_
        run_benchamrk()

    """
    # Access the arguments as attributes of the 'args' object
    EXTRACT_PATH = args.extract_path
    DOTNET_BASE_VERSION_URL_LINUX = args.dotnet_base_version_url_linux
    DOTNET_DAILY_VERSION_URL_LINUX = args.dotnet_daily_version_url_linux
    TEST_SOLUTION_REPO_URL = args.test_solution_repo_url
    TEST_REPO_NAME = args.test_repo_name
    TEST_SOLUTION_CASE = args.test_solution_case
    TEST_SOLUTION_DIR = args.test_solution_dir
    TEST_SOLUTION_FILE = args.solution_file
    SDK_VERSION = args.sdk_version
    SDK_DAILY_VERSION = args.sdk_daily_version
    DATABASE_FILE = args.database_file
    NESTED = args.is_nested_solution == "True"

    # create the extract destination directories if they do not exist
    create_extract_destinations(EXTRACT_PATH)

    # download and extract the dotnet sdk

    download_and_extract_dotnet_sdk(DOTNET_BASE_VERSION_URL_LINUX, "base")
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_LINUX, "daily")

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL,
                     TEST_REPO_NAME, TEST_SOLUTION_CASE, NESTED, TEST_SOLUTION_DIR)

    # build the solution using the base version

    msbuild_command = f"msbuild {TEST_SOLUTION_FILE}"
    versions = ['base']
    duration_in_seconds = 0
    base_duration_in_seconds = 0
    test_scenario = 'cold'
    for version in versions:
        # sub_dir = "/sdk" if version == 'daily' else ''
        # subdirs = './../../../sdk' if NESTED else './../sdk'
        subdirs = './../../../sdk' if NESTED else './../sdk'
        exec_path = os.path.abspath(f"{subdirs}/{version}/dotnet")
        run_build_to_restore_packages(exec_path)
        simple_command = f"msbuild {TEST_SOLUTION_FILE}"
        command = f"{exec_path} {simple_command}"
        elapsed_time = measure_execution_time(command)
        if version == 'base':
            base_duration_in_seconds = elapsed_time
        else:
            duration_in_seconds = elapsed_time
        print('-----WINDOWS BENCHMARK RESULT-----')
        print(
            f"Running '{command}' with {version} version took {elapsed_time}s to execute.")

    # save benchmark results to a csv file
    # save_benchmark_results(file_path, benchmark_duration, benchmark_base_duration, sdk_version, sdk_daily_version, test_case_name, test_scenario):
    utils.save_benchmark_results(
        DATABASE_FILE, duration_in_seconds, base_duration_in_seconds, SDK_VERSION, SDK_DAILY_VERSION, TEST_SOLUTION_CASE, test_scenario
    )


if __name__ == '__main__':
    # Parse arguments using argparse
    parser = argparse.ArgumentParser(
        description='---Benchmark Runner---')

   # <-Parse arguments
    parser.add_argument('--extract_path', help='Path for extraction')
    parser.add_argument('--dotnet_base_version_url_linux',
                        help='URL for the base version of .NET SDK on Linux')
    parser.add_argument('--dotnet_daily_version_url_linux',
                        help='URL for the daily version of .NET SDK on Linux')
    parser.add_argument('--test_solution_repo_url',
                        help='URL of the test solution repository')
    parser.add_argument('--test_repo_name', help='Name of the test repository')
    parser.add_argument('--test_solution_case', help='Test solution case')
    parser.add_argument('--test_solution_dir', help='Test solution directory')
    parser.add_argument('--sdk_version', help='Version of the SDK')
    parser.add_argument('--sdk_daily_version', help='Version of the daily SDK')
    parser.add_argument('--database_file', help='Path to the database file')
    parser.add_argument('--solution_file', help='Path to the database file')
    parser.add_argument('--is_nested_solution',
                        help='Path to the database file')
    # Parse arguments ->

    args = parser.parse_args()

    run_benchamrk(args)
