"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild on windows
Returns:
    None: .....
"""

import subprocess
# ___ EXTRACTION CONSTANTS ___ #
EXTRACT_PATH = "sdk"

# _____ BENCHMARK DEPENDENCIES CONSTANTS _____ #

DOTNET_BASE_VERSION_URL_WINDOWS = "https://download.visualstudio.microsoft.com/download/pr/1fb808dc-d017-4460-94f8-bf1ac83e6cd8/756b301e714755e411b84684b885a516/dotnet-sdk-7.0.100-win-x64.zip"

DOTNET_DAILY_VERSION_URL_WINDOWS = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-win-x64.zip"

TEST_SOLUTION_REPO_URL = "https://github.com/NuGet/NuGet.Client"

TEST_REPO_NAME = "NuGet.Client"
TEST_SOLUTION_CASE = "NuGet.Client"
TEST_SOLUTION_DIR = "./"
SDK_VERSION = "7.0.100"
SOLUTION_FILE = "NuGet.sln"
SDK_DAILY_VERSION = "8.0.1xx"
DATABASE_FILE = "./../../../data/msbuild.csv"
NESTED = "False"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_windows.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_WINDOWS, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_WINDOWS, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_repo_name", TEST_REPO_NAME, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--sdk_version", SDK_VERSION, "--sdk_daily_version", SDK_DAILY_VERSION, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
