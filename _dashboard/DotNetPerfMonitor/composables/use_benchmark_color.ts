export default async function useBenchmarkColor(benchmark: string) {
  const config = await useDataConfig();
  const benchmarkColor = config.data.nuget.benchmarks;

  // populate key:name value:color in a map
  const benchmarkColorMap = new Map<string, string>();
  benchmarkColor.forEach((element: any) => {
    benchmarkColorMap.set(element.name, element.color);
  });

  // if the benchmark is not in the map, generate a random color
  if (!benchmarkColorMap.has(benchmark)) {
    return useColorGenerator();
  }
  // if the benchmark is in the map, return the color
  return benchmarkColorMap.get(benchmark);
}
