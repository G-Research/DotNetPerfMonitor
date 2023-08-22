"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import argparse
import subprocess
import time
import os
import zipfile
import urllib
import urllib.request

EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"


DOTNET_BASE_VERSION_URL_LINUX: "https://download.visualstudio.microsoft.com/download/pr/dc930bff-ef3d-4f6f-8799-6eb60390f5b4/1efee2a8ea0180c94aff8f15eb3af981/dotnet-sdk-6.0.300-linux-x64.tar.gz"

DOTNET_DAILY_VERSION_URL_LINUX: "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"

TEST_SOLUTION_REPO_URL: "https://github.com/marcin-krystianc/TestSolutions.git"

TEST_SOLUTION_DIR: "LargeAppWithPrivatePackagesCentralisedNGBVRemoved/solution"


def download_file(url, filename):
    """ Download file from url and save it to filename"""
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


def extract_zip(zip_file, extract_folder):
    """ Extracts zip file to extract_folder"""
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def download_and_extract_dotnet_sdk(version_url, is_base):
    """_summary_

    Args:
        version_url (String): dotnet sdk version url
    """

    # Download the dotnet sdk
    path = f"{EXTRACT_PATH}/base" if is_base else f"{EXTRACT_PATH}/daily"
    command = f"wget {version_url} -O dotnet-sdk.zip"
    unzipcommand = f"unzip dotnet-sdk.zip -d sdk/{path}"

    subprocess.call(f"powershell {powershell_command}", shell=True)
    subprocess.call(f"powershell {extract_command}", shell=True)


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


def main():
    """_summary_
        main()

    """
    # create a working directory for the test experiment
    subprocess.call(f"mkdir {WORKING_DIR}", shell=True)
    subprocess.call(f"cd {WORKING_DIR}", shell=True)

    # download and extract the dotnet sdk
    download_and_extract_dotnet_sdk(DOTNET_DAILY_VERSION_URL_LINUX, True)

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_DIR)

    # build the solution using the base version
    exec_path = "../../sdk/base/dotnet"
    msbuild_command = """
     msbuild /t:GetSuggestedWorkloads;_CheckForInvalidConfigurationAndPlatform;ResolveReferences;ResolveProjectReferences;ResolveAssemblyReferences;ResolveComReferences;ResolveNativeReferences;ResolveSdkReferences;ResolveFrameworkReferences;ResolvePackageDependenciesDesignTime;Compile;CoreCompile ^
        /p:AndroidPreserveUserData=True ^
        /p:AndroidUseManagedDesignTimeResourceGenerator=True ^
        /p:BuildingByReSharper=True ^
        /p:BuildingProject=False ^
        /p:BuildProjectReferences=False ^
        /p:ContinueOnError=ErrorAndContinue ^
        /p:DesignTimeBuild=True ^
        /p:DesignTimeSilentResolution=False ^
        /p:JetBrainsDesignTimeBuild=True ^
        /p:ProvideCommandLineArgs=True ^
        /p:ResolveAssemblyReferencesSilent=False ^
        /p:SkipCompilerExecution=True ^
        /p:TargetFramework=net5.0 ^
        /v:n ^
        /m:1 ^
        /bl ^
        /flp:v=n;PerformanceSummary ^
        /clp:Summary ^
        /clp:PerformanceSummary > log.txt
    """
    command = f"{exec_path} {msbuild_command}"
    elapsed_time = measure_execution_time(command)
    print(f"Command '{command}' took {elapsed_time}s to execute.")
    return elapsed_time


if __name__ == "__main__":
    main()
