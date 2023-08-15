export default function useBenchmarkGrouper(
  data: Array<{ field: String; [key: string]: any }>,
  benchmark: String
) {
  return data.filter((item) => item["test case"] === benchmark);
}

const solutions = [
  "LargeAppCPM-142722b",
  "LargeAppCPM64-142722b",
  "LargeAppCPM-nostaticgraph-142722b",
  "LargeAppCPM64-nostaticgraph-142722b",
  "Orleans-eda972a",
  "OrchardCore-5dbd92c",
  "NuGetClient-win-d76a117",
];
