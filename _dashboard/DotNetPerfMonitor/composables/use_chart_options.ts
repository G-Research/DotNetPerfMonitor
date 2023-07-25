export default function useChartOptions(type: String) {
  const lineOptions = {
    responsive: true,
    maintainAspectRatio: true,
    title: {
      display: true,
      text: "Title of chart",
    },
    legend: {
      display: true,
      position: "left",
      labels: {
        fontSize: 18,
        fontColor: "red",
        usePointStyle: false,
        padding: 10,
      },
    },
    scales: {
      x: {
        type: "time",
        time: {
          unit: "day",
          displayFormats: {
            day: "MMM D",
          },
        },
      },
    },

    tooltips: {
      enabled: true,
      mode: "index",
      intersect: false,
      backgroundColor: "rgba(0,0,0,0.8)",
      titleFontColor: "yellow",
      titleFontSize: 14,
      titleMarginBottom: 10,
      bodyFontColor: "white",
      bodyFontSize: 12,
      bodySpacing: 10,
      xPadding: 10,
      yPadding: 10,
      caretSize: 8,
      cornerRadius: 10,
      displayColors: true,
    },
  };

  return type === "line" ? lineOptions : lineOptions;
}
