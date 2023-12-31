#########################################################
$dotnet_base_url = "https://download.visualstudio.microsoft.com/download/pr/cd0d0a4d-2a6a-4d0d-b42e-dfd3b880e222/008a93f83aba6d1acf75ded3d2cfba24/dotnet-sdk-6.0.400-linux-x64.tar.gz"
$dotnet_url = Get-Content -Path $PSScriptRoot\daily-linux.txt
$repoUrl = "https://github.com/OrchardCMS/OrchardCore.git"
$commitHash = "5dbd92cb06cee203b95e0b3bc133d852adf3fbeb"
$solutionFilePath = "OrchardCore.sln"
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

#########################################################
# Workaround for errors due to a vulnerability scanning (https://github.com/NuGet/Home/blob/dev/proposed/2022/vulnerabilities-in-restore.md)
New-Item "$sourcePath\Directory.Build.rsp" -Value "/p:NuGetAudit=disable"

$versions = @("dotnet_base", "dotnet")
ForEach ($version In $versions) {
	$url = (Get-Variable ("$version" + "_url")).Value
	Invoke-WebRequest -Uri "$url" -OutFile ("$version" + ".tar.gz")
	New-Item -Name "$version" -ItemType "Directory"
	. tar xfz ("$version" + ".tar.gz") --directory "$version"
	. "$PSScriptRoot\..\RunPerformanceTests.ps1" -nugetClientFilePath "$version\dotnet" -solutionFilePath $solutionFilePath -resultsFilePath $resultsFilePath -iterationCount 1 -staticGraphRestore
}