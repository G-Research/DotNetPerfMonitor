export default function useScenarioFilter(
  data: Array<{ scenario: String; [key: string]: any }>,
  scenario: String
) {
  const filtered =
    scenario === "all"
      ? data
      : data.filter((item) => item.scenario === scenario);
  return filtered.map((item) => item.duration);
}
