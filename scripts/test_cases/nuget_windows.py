"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild on windows
Returns:
    None: .....
"""

import subprocess
# ___ EXTRACTION CONSTANTS ___ #
EXTRACT_PATH = "sdk"

# _____ BENCHMARK DEPENDENCIES CONSTANTS _____ #

# DOTNET_BASE_VERSION_URL_WINDOWS = "https://download.visualstudio.microsoft.com/download/pr/4ede0897-e03d-4d93-a50d-e06f2e430d9e/b5bd2605ce07ec7163d5b5b05dc2f1e0/dotnet-sdk-8.0.100-preview.7.23376.3-win-x64.zip"

DOTNET_BASE_VERSION_URL_WINDOWS = "https://download.visualstudio.microsoft.com/download/pr/1fb808dc-d017-4460-94f8-bf1ac83e6cd8/756b301e714755e411b84684b885a516/dotnet-sdk-7.0.100-win-x64.zip"

DOTNET_DAILY_VERSION_URL_WINDOWS = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-win-x64.zip"

TEST_SOLUTION_REPO_URL = "https://github.com/NuGet/NuGet.Client"

TEST_REPO_NAME = "NuGet.Client"
TEST_SOLUTION_CASE = "NuGet.Client"
TEST_SOLUTION_DIR = "./"
SDK_VERSION = "8.0.100-preview.7.23376.3"
SOLUTION_FILE = "NuGet.sln"
SDK_DAILY_VERSION = "8.0.1xx"
DATABASE_FILE = "./../../../data/msbuild.csv"
NESTED = "False"
COMMIT_HASH = "d76a117c590f8a91b844013bba7ea9b60e469aa1"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_windows.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_WINDOWS, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_WINDOWS, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--commit_hash", COMMIT_HASH, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
