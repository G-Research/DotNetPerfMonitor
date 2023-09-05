"""_summary_
This script basically runs benchmark test for msbuild on windows
Returns:
    None: .....
"""

import subprocess
# ___ EXTRACTION CONSTANTS ___ #
EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"

# _____ BENCHMARK DEPENDENCIES CONSTANTS _____ #

DOTNET_BASE_VERSION_URL_WINDOWS = "https://download.visualstudio.microsoft.com/download/pr/de1f99bb-4d6d-4dfe-9935-d24b1e8bca12/0b449d12398e45c62dce4b497e1b49bb/dotnet-sdk-6.0.316-win-x64.zip"

DOTNET_DAILY_VERSION_URL_WINDOWS = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-win-x64.zip"

TEST_SOLUTION_REPO_URL = "https://github.com/marcin-krystianc/TestSolutions.git"

TEST_REPO_NAME = "TestSolutions"
TEST_SOLUTION_CASE = "LargeAppWithPrivatePackagesCentralisedSlim"
TEST_SOLUTION_DIR = "solution"
SDK_VERSION = "6.0.316"
SDK_DAILY_VERSION = "8.0.1xx"
DATABASE_FILE = "./../../../data/msbuild.csv"
NESTED = "True"
SOLUTION_FILE = "LargeAppWithPrivatePackagesCentralisedSlim.sln"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_windows.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_WINDOWS, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_WINDOWS, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_repo_name", TEST_REPO_NAME, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--sdk_version", SDK_VERSION, "--sdk_daily_version", SDK_DAILY_VERSION, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
