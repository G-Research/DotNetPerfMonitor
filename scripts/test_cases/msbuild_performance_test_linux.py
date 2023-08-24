"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import subprocess
import time
import os
import urllib.request

EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/dc930bff-ef3d-4f6f-8799-6eb60390f5b4/1efee2a8ea0180c94aff8f15eb3af981/dotnet-sdk-6.0.300-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"
TEST_SOLUTION_REPO_URL = "https://github.com/marcin-krystianc/TestSolutions.git"
TEST_REPO_NAME = "TestSolutions"
TEST_SOLUTION_CASE = "LargeAppWithPrivatePackagesCentralisedNGBVRemoved"
TEST_SOLUTION_DIR = "solution"


def check_directory(event):
    """Checking directory for debugging purposes"""
    print(f'_____CHECKING DIR {event}________')
    subprocess.call("ls", shell=True)


def create_extract_destinations():
    """ Create the extract destination directories if they do not exist"""
    check_directory('BEFORE CREATE EXTRACT DESTINATION')
    if not os.path.exists(EXTRACT_PATH):
        os.mkdir(EXTRACT_PATH)
    os.chdir(EXTRACT_PATH)
    if not os.path.exists("base"):
        os.mkdir("base")
    if not os.path.exists("daily"):
        os.mkdir("daily")
    check_directory('AFTER CREATE EXTRACT DESTINATION')


def download_file(url, filename):
    """ Download file from url and save it to filename"""
    check_directory('BEFORE DOWNLOAD FILE')
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    check_directory('AFTER DOWNLOAD FILE')


def download_and_extract_dotnet_sdk(version_url, is_base):
    """ Download and extract the dotnet sdk"""
    path = "base" if is_base else "daily"
    tar_gz_file = "dotnet-sdk.tar.gz"
    download_file(version_url, tar_gz_file)

    # Extract the tar.gz file
    check_directory('BEFORE EXTRACT FILE')
    extract_command = f"tar -xzf {tar_gz_file} -C {path}"
    subprocess.call(extract_command, shell=True)


def measure_execution_time(command):
    """summary for measure_execution_time

    Args:
        command ([String]): [command to be executed]

    Returns:
        [Number]: [ellapsed time in seconds]
    """

    check_directory('BEFORE MEASURE EXECUTION TIME')
    subprocess.call(f"cd {TEST_REPO_NAME}", shell=True)
    check_directory('AFTER CHECKINT OUT TO REPO')

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
    check_directory('BEFORE CLONE REPO')
    # Clone the repository containing the solution
    subprocess.call(f"git clone {repo_url}", shell=True)
    subprocess.call(f"cd {TEST_REPO_NAME}", shell=True)
    subprocess.call(f"cd {repo_path}", shell=True)
    subprocess.call(f"cd {TEST_SOLUTION_DIR}", shell=True)
    check_directory('AFTER CLONE REPO')
    subprocess.call("ls", shell=False)


def delete_clone(repo_url):
    """_summary_

    Args:
        repo_path (String): path containing test code
    """
    # extract the repository name from the url
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    subprocess.call(f"rm -rf {repo_name}", shell=True)


def main():
    """_summary_
        main()

    """
    # create a working directory for the test experiment
    if not os.path.exists(WORKING_DIR):
        os.mkdir(WORKING_DIR)
    os.chdir(WORKING_DIR)

    # create the extract destination directories if they do not exist
    create_extract_destinations()

    # download and extract the dotnet sdk
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_LINUX, True)

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_CASE)

    check_directory('BEFORE BUILD SOLUTION')

    # build the solution using the base version
    exec_path = "../../sdk/base/dotnet"
    msbuild_command = """
      msbuild solution.sln /t:GetSuggestedWorkloads;_CheckForInvalidConfigurationAndPlatform;ResolveReferences;ResolveProjectReferences;ResolveAssemblyReferences;ResolveComReferences;ResolveNativeReferences;ResolveSdkReferences;ResolveFrameworkReferences;ResolvePackageDependenciesDesignTime;Compile;CoreCompile \
    /p:AndroidPreserveUserData=True \
    /p:AndroidUseManagedDesignTimeResourceGenerator=True \
    /p:BuildingByReSharper=False \
    /p:BuildingProject=False \
    /p:BuildProjectReferences=False \
    /p:ContinueOnError=ErrorAndContinue \
    /p:DesignTimeBuild=True \
    /p:DesignTimeSilentResolution=False \
    /p:JetBrainsDesignTimeBuild=True \
    /p:ProvideCommandLineArgs=True \
    /p:ResolveAssemblyReferencesSilent=False \
    /p:SkipCompilerExecution=True \
    /p:TargetFramework=net5.0 \
    /v:n \
    /m:1 \
    /bl \
    /flp:v=n;PerformanceSummary \
    /clp:Summary \
    /clp:PerformanceSummary > log.txt
    """

    simple_command = "build solution.sln"
    command = f"{exec_path} {simple_command}"
    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time}s to execute.")
    return elapsed_time


if __name__ == "__main__":
    main()
