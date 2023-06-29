# NuGet Performance Monitor
The NuGet Performance Monitor is an automated system for monitoring the performance of the NuGet package manager.
It continuously runs benchmarks for new releases of NuGet and in case of performance regressions, it raises an alert by opening a new Issue in this repository.
Visit https://G-Research.github.io/NuPerfMonitor/ to see the dashboard.

## Motivation
In our company we work with .NET solutions containing hundreds of projects, we also care about developer productivity, therefore we are deeply interested in improving the performance of the .NET ecosystem.

One of the key factors of developer productivity is the time spent waiting for NuGet to restore packages. We also want to benefit from runtime improvements which are shipped with every new release of .NET, but migrating to a new runtime is depending on being able to use the corresponding version of a .NET SDK and NuGet.

It happened in the past that there were some changes in NuGet that performed very poorly on large solutions and it prevented us from jumping to a newly released .NET until the bug was fixed. To prevent from such unpleasant surprises in the future we have created NuGet Performance Monitor.

## How it works
- [Scripts](https://github.com/NuGet/NuGet.Client/tree/dev/scripts/perftests) from the [NuGet.Client](https://github.com/NuGet/NuGet.Client) repository with custom [test cases](https://github.com/G-Research/NuPerfMonitor/tree/master/scripts/perftests/testCases).are are used for benchmarks, 
- GitHub Actions and GitHub-hosted runners are used to run benchmarks on a [daily schedule](https://github.com/G-Research/NuPerfMonitor/blob/master/.github/workflows/benchmarks.yml)
- Python script is used to [process results](https://github.com/G-Research/NuPerfMonitor/blob/master/process_results.py) and append it to the [data.csv](https://github.com/G-Research/NuPerfMonitor/blob/master/data.csv) file that makes it easy to plot charts and can be used further data analysis.
- There is also another python script that is used to [generate alerts](https://github.com/G-Research/NuPerfMonitor/blob/master/generate_alert.py). In case of performance regression is found a new Issue is opened.
- [Plotly.js](https://plotly.com/javascript/) is used to [generate](https://github.com/G-Research/NuPerfMonitor/blob/master/_site/index.html) charts with results.

It is worth noting that NuGet Performance Monitor uses GitHub-hosted runners to run the benchmark, therefore it cannot just assume what is the performance of the particular runner's VM or how it is going to change over time. Therefore, each test job runs actually two tests, one test for the baseline version and one test for the current version. By measuring the relative performance of the current version, the NuGet Performance Monitor is independent of the infrastructure that is running it.

## Contributing
Contributions are welcome! Whenever you have any suggestions or ideas to be implemented, we encourage you to:

* [File an issue](https://github.com/G-Research/NuPerfMonitor/issues/new/choose)
* [Submit a pull request](https://github.com/G-Research/NuPerfMonitor/pulls)
