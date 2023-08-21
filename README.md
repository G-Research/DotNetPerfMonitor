# DotNet Performance Monitor

[![Version](https://img.shields.io/badge/Version-1.0-gold.svg)](https://github.com/G-Research/DotNetPerfMonitor) [![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0) [![Pylint](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/pylint.yaml/badge.svg)](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/pylint.yaml)

DotnetPerfMonitor is an automated system for monitoring the performance of various components in the .NET ecosystem, including **NuGet, F# compiler, C# compiler, and MSBuild**. It builds upon the foundation of the [**NuGet Performance Monitor**](https://github.com/G-Research/NuPerfMonitor) and expands its functionality to encompass a broader range of tools and technologies. Visit https://g-research.github.io/DotNetPerfMonitor/ to see the dashboard.


## Motivation
In our company, we work extensively with .NET solutions consisting of hundreds of projects. Developer productivity is a key focus for us, and we are deeply invested in enhancing the performance of the .NET ecosystem.

One crucial aspect of developer productivity is the time spent waiting for NuGet to restore packages. We also want to take advantage of the runtime improvements that accompany each new release of .NET. However, transitioning to a new runtime version relies on being able to use the corresponding .NET SDK and NuGet version.

In the past, we have encountered situations where certain changes in NuGet resulted in poor performance for large solutions. These performance issues prevented us from adopting a new .NET release until the bug was fixed. To avoid such unpleasant surprises in the future, we developed the **NuGet Performance Monitor**. 

**Now, we aim to expand its capabilities to cover other aspects of the .NET ecosystem, such as the F# compiler, C# compiler, and MSBuild.**

**DotNetPerfMonitor** is this extended monitoring system. By encompassing additional components, we strive to gain insights into the performance characteristics of the entire .NET ecosystem. This will enable us to identify and address any performance regressions promptly, ensuring a smooth transition to new releases and an overall improved development experience.
## How it works
- [Scripts](https://github.com/NuGet/NuGet.Client/tree/dev/scripts/perftests) from the [NuGet.Client](https://github.com/NuGet/NuGet.Client) repository with custom [test cases](https://github.com/G-Research/DotNetPerfMonitor/tree/main/scripts/perftests/testCases).are are used for benchmarks, 
- GitHub Actions and GitHub-hosted runners are used to run benchmarks on a [daily schedule](https://github.com/G-Research/DotNetPerfMonitor/blob/main/.github/workflows/benchmarks.yml)
- Python script is used to [process results](https://github.com/G-Research/DotNetPerfMonitor/blob/main/process_results.py) and append it to the [data.csv](https://github.com/G-Research/DotNetPerfMonitor/blob/main/data.csv) file that makes it easy to plot charts and can be used further data analysis.
- There is also another python script that is used to [generate alerts](https://github.com/G-Research/DotNetPerfMonitor/blob/main/generate_alert.py). In case of performance regression is found a new Issue is opened.
- [Plotly.js](https://plotly.com/javascript/) is used to [generate](https://github.com/G-Research/DotNetPerfMonitor/blob/main/_site/index.html) charts with results.

It is worth noting that DotNet Performance Monitor uses GitHub-hosted runners to run the benchmark, therefore it cannot just assume what is the performance of the particular runner's VM or how it is going to change over time. Therefore, each test job runs actually two tests, one test for the baseline version and one test for the current version. By measuring the relative performance of the current version, the DotNet Performance Monitor is independent of the infrastructure that is running it.

## License
DotNetPerfMonitor is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/G-Research/DotNetPerfMonitor/blob/main/LICENSE) for the full license details.

## Contributing
Contributions are welcome! Whenever you have any suggestions or ideas to be implemented, we encourage you to:

* [File an issue](https://github.com/G-Research/DotNetPerfMonitor/issues/new/choose)
* [Submit a pull request](https://github.com/G-Research/DotNetPerfMonitor/pulls)


## Contributors
[![](https://contrib.rocks/image?repo=G-Research/DotNetPerfMonitor)](https://github.com/G-Research/DotNetPerfMonitor/graphs/contributors)
