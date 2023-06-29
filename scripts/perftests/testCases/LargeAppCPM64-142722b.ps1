#########################################################
$dotnet_base_url = "https://download.visualstudio.microsoft.com/download/pr/cd0d0a4d-2a6a-4d0d-b42e-dfd3b880e222/008a93f83aba6d1acf75ded3d2cfba24/dotnet-sdk-6.0.400-linux-x64.tar.gz"
$dotnet_url = Get-Content -Path $PSScriptRoot\daily-linux.txt
$repoUrl = "https://github.com/marcin-krystianc/TestSolutions.git"
$commitHash = "142722bebfe90c4e5c98303fa1598db6a760adae"
$solutionFilePath = "LargeAppWithPrivatePackagesCentralisedNGBVRemoved\solution\LargeAppWithPrivatePackagesCentralisedNGBVRemoved.sln"
$globalJsonPath = ""

#########################################################
$ErrorActionPreference = "Stop"
. "$PSScriptRoot\..\PerformanceTestUtilities.ps1"

$repoName = GenerateNameFromGitUrl $repoUrl
$resultsFilePath = "results.csv"
$sourcePath = $([System.IO.Path]::GetFullPath($repoName))
SetupGitRepository $repoUrl $commitHash $sourcePath
$solutionFilePath = "$sourcePath\$solutionFilePath"
$ProgressPreference = 'SilentlyContinue' #https://github.com/PowerShell/PowerShell/issues/2138 
if ($globalJsonPath) {Remove-Item "$sourcePath\$globalJsonPath"}

$versions = @("dotnet_base", "dotnet")
ForEach ($version In $versions) {
	$url = (Get-Variable ("$version" + "_url")).Value
	Invoke-WebRequest -Uri "$url" -OutFile ("$version" + ".tar.gz")
	New-Item -Name "$version" -ItemType "Directory"
	. tar xfz ("$version" + ".tar.gz") --directory "$version"
	. "$PSScriptRoot\..\RunPerformanceTests.ps1" -nugetClientFilePath "$version\dotnet" -solutionFilePath $solutionFilePath -resultsFilePath $resultsFilePath -iterationCount 1 -staticGraphRestore
}