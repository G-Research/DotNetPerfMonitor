export default function useColumnsetExtractor(
  data: Array<{ field: String; [key: string]: any }>,
  column: String
) {
  const scenarios: String[] = [];
  // add scenarios of each row to array without duplicates
  data.forEach((row) => {
    if (!scenarios.includes(row["solution"])) {
      scenarios.push(row["solution"]);
    }
  });

  return scenarios;
}
