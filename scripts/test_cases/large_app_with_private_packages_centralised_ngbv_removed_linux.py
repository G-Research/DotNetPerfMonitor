"""_summary_
This script basically runs benchmark test for msbuild
Returns:
    None: .....
"""

import subprocess

EXTRACT_PATH = "sdk"
WORKING_DIR = "msbuild-performance-test"
DOTNET_BASE_VERSION_URL_LINUX = "https://download.visualstudio.microsoft.com/download/pr/dc930bff-ef3d-4f6f-8799-6eb60390f5b4/1efee2a8ea0180c94aff8f15eb3af981/dotnet-sdk-6.0.300-linux-x64.tar.gz"
DOTNET_DAILY_VERSION_URL_LINUX = "https://aka.ms/dotnet/8.0.1xx/daily/dotnet-sdk-linux-x64.tar.gz"
TEST_SOLUTION_REPO_URL = "https://github.com/marcin-krystianc/TestSolutions"
TEST_REPO_NAME = "TestSolutions"
TEST_SOLUTION_CASE = "LargeAppWithPrivatePackagesCentralisedSlim"
TEST_SOLUTION_DIR = "solution"
SDK_VERSION = "6.0.300"
SDK_DAILY_VERSION = "8.0.1xx"
DATABASE_FILE = "./../../../../../data/msbuild.csv"
NESTED = "True"
SOLUTION_FILE = "LargeAppWithPrivatePackagesCentralisedSlim.sln"
COMMIT_HASH = "142722bebfe90c4e5c98303fa1598db6a760adae"

if __name__ == "__main__":
    commands_chain = ["python3", "./../benchmark_runner_linux.py", "--extract_path", EXTRACT_PATH, "--dotnet_base_version_url_linux",
                      DOTNET_BASE_VERSION_URL_LINUX, "--dotnet_daily_version_url_linux", DOTNET_DAILY_VERSION_URL_LINUX, "--test_solution_repo_url", TEST_SOLUTION_REPO_URL, "--test_solution_case", TEST_SOLUTION_CASE, "--test_solution_dir", TEST_SOLUTION_DIR, "--solution_file", SOLUTION_FILE, "--sdk_version", "--commit_hash", COMMIT_HASH, "--database_file", DATABASE_FILE, "--is_nested_solution", NESTED]

    subprocess.run(commands_chain, check=True)
