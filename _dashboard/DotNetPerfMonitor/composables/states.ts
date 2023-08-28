export const useDataSource = () =>
  useState<string>(
    "datasource",
    () =>
      "https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data/nuget.csv"
  );

export const useRegressionsNumber = () =>
  useState<number>("regressions_number", () => 0);
