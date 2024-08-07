![dotnetpermonitor-banner](https://github.com/G-Research/DotNetPerfMonitor/assets/49169158/15a51578-38c3-4f36-9bfc-a83eaba5471c)

[![Version](https://img.shields.io/badge/Version-1.0-gold.svg)](https://github.com/G-Research/DotNetPerfMonitor) [![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0) [![Pylint](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/pylint.yaml/badge.svg)](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/pylint.yaml) [![NuGet](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/benchmarks_nuget.yml/badge.svg)](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/benchmarks_nuget.yml) [![Dashboard to github Pages](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/dashboard.yaml/badge.svg)](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/dashboard.yaml)

DotnetPerfMonitor is an automated system for monitoring the performance of various components in the .NET ecosystem, including **NuGet, F# compiler, C# compiler, and MSBuild**. It builds upon the foundation of the [**NuGet Performance Monitor**](https://github.com/G-Research/NuPerfMonitor) and expands its functionality to encompass a broader range of tools and technologies. Visit https://g-research.github.io/DotNetPerfMonitor/ to see the dashboard.


## Motivation
In our company, we work extensively with .NET solutions consisting of hundreds of projects. Developer productivity is a key focus for us, and we are deeply invested in enhancing the performance of the .NET ecosystem.

One crucial aspect of developer productivity is the time spent waiting for NuGet to restore packages. We also want to take advantage of the runtime improvements that accompany each new release of .NET. However, transitioning to a new runtime version relies on being able to use the corresponding .NET SDK and NuGet version.

In the past, we have encountered situations where certain changes in NuGet resulted in poor performance for large solutions. These performance issues prevented us from adopting a new .NET release until the bug was fixed. To avoid such unpleasant surprises in the future, we developed the **NuGet Performance Monitor**. 

**Now, we aim to expand its capabilities to cover other aspects of the .NET ecosystem, such as the F# compiler, C# compiler, and MSBuild.**

**DotNetPerfMonitor** is this extended monitoring system. By encompassing additional components, we strive to gain insights into the performance characteristics of the entire .NET ecosystem. This will enable us to identify and address any performance regressions promptly, ensuring a smooth transition to new releases and an overall improved development experience.
## How it works

We use scripts from various repositories with custom test cases for benchamrks. **GitHub Actions** and **GitHub-hosted** runners are used to run `benchmarks` on a [daily schedule](https://github.com/G-Research/DotNetPerfMonitor/blob/main/.github/workflows), with a cron job running `three times per day`. **These benchmarks measure the performance of various components**.

After the benchmarks are run, the results are processed using Python scripts. These scripts analyze the benchmark data and extract relevant information. The processed data is then saved to CSV files for further analysis and visualization.

The CSV files containing the benchmark results can be used to generate charts and visualizations on a dashboard or any other reporting tool. This allows for a comprehensive understanding of the performance characteristics of the components being tested.

By regularly running benchmarks and analyzing the performance data, `DotnetPerfMonitor` can identify any performance regressions. A python script that is used to [generate alerts](https://github.com/G-Research/DotNetPerfMonitor/blob/main/scripts/processors/generate_alert.py). In case of performance regression is found a new Issue is opened. In the case of a performance regression, **a new Github issue is automatically opened to track the problem**.


*It is worth noting that DotNet Performance Monitor uses `GitHub-hosted` runners to run the benchmark, therefore it cannot just assume what is the performance of the particular runner's VM or how it is going to change over time. Therefore, each test job runs actually two tests, one test for the baseline version and one test for the current version. By measuring the relative performance of the current version, the DotNet Performance Monitor is independent of the infrastructure that is running it.*

### You can also check more details about each compotent here.
<details>
    <summary>🟢 NuGet</summary>

- [Scripts](https://github.com/NuGet/NuGet.Client/tree/dev/scripts/perftests) from the [NuGet.Client](https://github.com/NuGet/NuGet.Client) repository with custom [test cases](https://github.com/G-Research/DotNetPerfMonitor/tree/main/scripts/perftests/testCases) are are used for benchmarks, 
- GitHub Actions and GitHub-hosted runners are used to run benchmarks on a [daily schedule](https://github.com/G-Research/DotNetPerfMonitor/blob/main/.github/workflows/benchmarks_nuget.yml)
- Python script is used to [process results](https://github.com/G-Research/DotNetPerfMonitor/blob/main/process_results.py) and append it to the [nuget.csv](https://github.com/G-Research/DotNetPerfMonitor/blob/main/data/nuget.csv) file that makes it easy to plot charts and can be used further data analysis.
- The data is the visualized on the [dashboard](https://g-research.github.io/DotNetPerfMonitor/) using [ChartJS](https://chartjs.org/), on the NuGet Tab.
</details>

<details>
    <summary>🟣 MS Build</summary>

- Python [scripts](https://github.com/G-Research/DotNetPerfMonitor/tree/main/scripts/test_cases/) are used for MSBuild benchamrking, using test cases like [Orleans](https://github.com/dotnet/orleans) and [OrchardCore](https://github.com/OrchardCMS/OrchardCore)
- GitHub Actions and GitHub-hosted runners are used to run benchmarks on a [daily schedule](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/benchmark_msbuild.yaml)
- Benchamrk results are processed and added to the [msbuild.csv file](https://github.com/G-Research/DotNetPerfMonitor/blob/main/data/msbuild.csv) that makes it easy to plot charts and can be used further data analysis.
- The data is the visualized on the [dashboard](https://g-research.github.io/DotNetPerfMonitor/) using [ChartJS](https://chartjs.org/), on the `MSBuild` Tab.
</details>

<details>
    <summary>🔵 F#</summary>
</details>

<details>
    <summary>🟠 C#</summary>
</details>

## License
`DotNetPerfMonitor` is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/G-Research/DotNetPerfMonitor/blob/main/LICENSE) for the full license details.

## Contributing
We welcome contributions from the community to enhance DotNetPerfMonitor. If you're interested in contributing, please follow these guidelines specified in [CONTRIBUTING.md](CONTRIBUTING.md).
## Contributors
[![](https://contrib.rocks/image?repo=G-Research/DotNetPerfMonitor)](https://github.com/G-Research/DotNetPerfMonitor/graphs/contributors)
