export default function useColumnsetExtractor(
  data: Array<{ field: string; [key: string]: any }>,
  column: string
) {

  const scenarios = Array.from(new Set(data.map((row) => row[column])));
  return scenarios;
}
