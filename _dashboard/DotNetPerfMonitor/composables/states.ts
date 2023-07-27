export const useActiveScenario = () =>
  useState<string>("activeScenario", () => "cold");
export const useAlphaScenario = () =>
  useState<string>("scenario", () => "cold");
export const useDataSource = () =>
  useState<string>(
    "datasource",
    () =>
      "https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv"
  );
