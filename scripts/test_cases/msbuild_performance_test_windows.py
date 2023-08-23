"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import subprocess
import time


# ___ EXTRACTION CONSTANTS ___ #
EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"

# _____ BENCHMARK DEPENDENCIES CONSTANTS _____ #

DOTNET_BASE_VERSION_URL_WINDOWS: "https://download.visualstudio.microsoft.com/download/pr/de1f99bb-4d6d-4dfe-9935-d24b1e8bca12/0b449d12398e45c62dce4b497e1b49bb/dotnet-sdk-6.0.316-win-x64.zip"

DOTNET_DAILY_VERSION_URL_WINDOWS: "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-win-x64.zip"

TEST_SOLUTION_REPO_URL: "https://github.com/marcin-krystianc/TestSolutions.git"

TEST_SOLUTION_DIR: "LargeAppWithPrivatePackagesCentralisedNGBVRemoved/solution"


def back_to_previous_dir():
    """_summary_
    """
    subprocess.call("cd ..", shell=True)


def download_and_extract_dotnet_sdk(version_url, is_base):
    """_summary_

    Args:
        version_url (String): dotnet sdk version url
"""
    path = f"{EXTRACT_PATH}/base" if is_base else f"{EXTRACT_PATH}/daily"

    # Download the dotnet sdk
    powershell_command = f"Invoke-WebRequest -Uri {version_url} -OutFile dotnet-sdk.zip"
    extract_command = f"Expand-Archive -Path dotnet-sdk.zip -DestinationPath sdk/{path}"

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
    download_and_extract_dotnet_sdk(DOTNET_BASE_VERSION_URL_WINDOWS, True)

    # clone the repository and navigate to the solution directory
    clone_repository(TEST_SOLUTION_REPO_URL, TEST_SOLUTION_DIR)

    # build the solution using the base version
    exec_path = "../../sdk/base/dotnet.exe"
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
