"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild
Returns:
    None: .....
"""

import subprocess

EXTRACT_PATH = "sdk"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/253e5af8-41aa-48c6-86f1-39a51b44afdc/5bb2cb9380c5b1a7f0153e0a2775727b/dotnet-sdk-7.0.100-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"
TEST_SOLUTION_REPO_URL = "https://github.com/OrchardCMS/OrchardCore"
TEST_REPO_NAME = "OrchardCore"
TEST_SOLUTION_CASE = "OrchardCore"
TEST_SOLUTION_DIR = "./"
SDK_VERSION = "7.0.100"
SDK_DAILY_VERSION = "8.0.1xx"
SOLUTION_FILE = "OrchardCore.sln"
DATABASE_FILE = "./../../../data/msbuild.csv"
NESTED = "False"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_linux.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_LINUX, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_LINUX, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_repo_name", TEST_REPO_NAME, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--sdk_version", SDK_VERSION, "--sdk_daily_version", SDK_DAILY_VERSION, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
