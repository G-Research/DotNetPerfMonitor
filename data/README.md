# DotnetPerfMonitor Benchmarks

This directory contains database of benchmarks for DotnetPerfMonitor components (MSBUILD, F#, C# and NUGET).

- Each benchmarks set is a separate file with a name that corresponds to the name of the component.
- These files are updated automatically by the [benchmarks workflow](https://github.com/G-Research/DotNetPerfMonitor/actions/workflows/benchmarks.yml) on a daily basis, thrice in a day.
- We save `base duration`, `relative duration`, `version`, `base version`, `duration`, `test case`, and `timestamp` for each benchmark.
- Data recoreded in these files is used to generate charts on the [dashboard](https://g-research.github.io/DotNetPerfMonitor/).