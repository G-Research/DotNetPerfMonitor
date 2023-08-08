export default function useColumnsetExtractor(
  data: Array<{ field: string; [key: string]: any }>,
  column: string
) {
  const scenarios: String[] = [];
  // add scenarios of each row to array without duplicates
  data.forEach((row: any) => {
    if (!scenarios.includes(row[column])) {
      scenarios.push(row[column]);
    }
  });

  return scenarios;
}
