export default function useBenchmarkGrouper(
  data: Array<{ field: String; [key: string]: any }>,
  benchmark: String
) {
  return data.filter((item) => item["test case"] === benchmark);
}
