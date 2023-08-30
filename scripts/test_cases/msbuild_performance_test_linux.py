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
    subprocess.run(["ls"], check=True)


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
    check_directory('BEFORE EXTRACT FILE')
    # extract_command = f"tar -xzf {tar_gz_file} -C {extract_path}"
    subprocess.run(["tar", "-xzf", tar_gz_file,
                   "-C", extract_path], check=True)


def measure_execution_time(command):
    """summary for measure_execution_time

    Args:
        command ([String]): [command to be executed]

    Returns:
        [Number]: [ellapsed time in seconds]
    """

    subprocess.run(["cd", TEST_REPO_NAME], check=True)

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
    subprocess.run(['git', 'clone', repo_url], check=True)
    subprocess.run(['cd', TEST_REPO_NAME], check=True)
    subprocess.run(['cd', repo_path], check=True)
    subprocess.run(['cd', TEST_SOLUTION_DIR], check=True)
    subprocess.run(['ls'], check=True)


def main():
    """_summary_
        main()

    """

    # create the extract destination directories if they do not exist
    create_extract_destinations()

    # download and extract the dotnet sdk
    path = "base"
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_LINUX, path)

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_CASE)

    check_directory('BEFORE BUILD SOLUTION')

    # build the solution using the base version
    exec_path = "../../sdk/base/dotnet"
    msbuild_command = """
      msbuild LargeAppWithPrivatePackagesCentralisedNGBVRemoved.sln /t:GetSuggestedWorkloads;_CheckForInvalidConfigurationAndPlatform;ResolveReferences;ResolveProjectReferences;ResolveAssemblyReferences;ResolveComReferences;ResolveNativeReferences;ResolveSdkReferences;ResolveFrameworkReferences;ResolvePackageDependenciesDesignTime;Compile;CoreCompile \
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

    simple_command = "build LargeAppWithPrivatePackagesCentralisedNGBVRemoved.sln"
    command = f"{exec_path} {simple_command}"
    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time}s to execute.")
    return elapsed_time


if __name__ == "__main__":
    main()
