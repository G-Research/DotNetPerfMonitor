export default function useScenarioColor(scenario: string) {
  const colors: { [key: string]: { [key: string]: string } } = {
    warmup: {
      bgColor: "rgb(255, 99, 132)",
      lineColor: "rgb(255, 99, 132)",
    },
    noop: {
      bgColor: "rgb(54, 162, 235)",
      lineColor: "rgb(54, 162, 235)",
    },
    force: {
      bgColor: "rgb(255, 205, 86)",
      lineColor: "rgb(255, 205, 86)",
    },
    cold: {
      bgColor: "rgb(75, 192, 192)",
      lineColor: "rgb(75, 192, 192)",
    },
    arctic: {
      bgColor: "rgb(153, 102, 255)",
      lineColor: "rgb(153, 102, 255)",
    },
    hot: {
      bgColor: "rgb(56, 142, 60)",
      lineColor: "rgb(56, 142, 60)",
    },
  };
  return colors[scenario];
}
