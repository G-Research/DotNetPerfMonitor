#########################################################
$dotnet_base_url = "https://download.visualstudio.microsoft.com/download/pr/1fb808dc-d017-4460-94f8-bf1ac83e6cd8/756b301e714755e411b84684b885a516/dotnet-sdk-7.0.100-win-x64.zip"
$dotnet_url = Get-Content -Path $PSScriptRoot\daily-windows.txt
$repoUrl = "https://github.com/NuGet/NuGet.Client.git"
$commitHash = "d76a117c590f8a91b844013bba7ea9b60e469aa1"
$solutionFilePath = "NuGet.sln"
$globalJsonPath = "global.json"

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
	Invoke-WebRequest -Uri "$url" -OutFile ("$version" + ".zip")
    Expand-Archive ("$version" + ".zip") -DestinationPath "$version"
	. "$PSScriptRoot\..\RunPerformanceTests.ps1" -nugetClientFilePath "$version\dotnet.exe" -solutionFilePath $solutionFilePath -resultsFilePath $resultsFilePath -iterationCount 1
}