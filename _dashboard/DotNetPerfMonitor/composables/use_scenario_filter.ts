// export default function useScenarioFilter(
//   data: Array<{ scenario: String; [key: string]: any }>,
//   scenario: String
// ) {
//   const filtered =
//     scenario === "all"
//       ? data
//       : data.filter((item) => item.scenario === scenario);
//   return filtered.map((item) => {
//     const timestamp = new Date(item.timestamp);
//     const month = timestamp.toLocaleString("default", { month: "long" });
//     const duration = item.duration;
//     const obj = {
//       x: month,
//       y: duration,
//     };
//     useLogger(obj);
//     return obj;
//   });
// }

export default function useScenarioFilter(
  data: Array<{ scenario: String; [key: string]: any }>,
  scenario: String
) {
  const filtered =
    scenario === "all"
      ? data
      : data.filter((item) => item.scenario === scenario);
  return filtered;
}
