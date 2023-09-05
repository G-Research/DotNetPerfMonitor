"""_summary_
This script basically runs benchmark test with [ORLEANS] solution for msbuild
Returns:
    None: .....
"""

import subprocess

EXTRACT_PATH = "sdk"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/32f2c846-5581-4638-a428-5891dd76f630/ee8beef066f06c57998058c5af6df222/dotnet-sdk-8.0.100-preview.7.23376.3-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"

TEST_SOLUTION_REPO_URL = "https://github.com/NuGet/NuGet.Client"
TEST_REPO_NAME = "NuGet.Client"
TEST_SOLUTION_CASE = "NuGet.Client"
TEST_SOLUTION_DIR = "./"
SDK_VERSION = "8.0.100-preview.7.23376.3"
SOLUTION_FILE = "NuGet.sln"
SDK_DAILY_VERSION = "8.0.1xx"
DATABASE_FILE = "./../../../data/msbuild.csv"
NESTED = "False"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_linux.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_LINUX, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_LINUX, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_repo_name", TEST_REPO_NAME, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--sdk_version", SDK_VERSION, "--sdk_daily_version", SDK_DAILY_VERSION, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
