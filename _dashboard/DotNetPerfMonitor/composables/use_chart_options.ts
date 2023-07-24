export default function useChartOptions(type: String) {
  const lineOptions = {
    //tension: 0.9,
    responsive: true,
    maintainAspectRatio: true,
    title: {
      display: true,
      text: "xs",
    },
    legend: {
      display: true,
      position: "top",
      labels: {
        fontSize: 18,
        fontColor: "red",
        usePointStyle: false,
        padding: 10,
      },
    },
    scales: {
      yAxes: [
        {
          id: "y-axis-1",
          type: "linear",
          position: "left",
          ticks: {
            beginAtZero: true,
            suggestedMax: 100,
            //stepSize: 20,
            fontSize: 12,
            fontColor: "blue",
            padding: 10,
          },
          gridLines: {
            display: true,
            color: "rgba(0, 0, 0, 0.1)",
          },
          scaleLabel: {
            display: true,
            labelString: "Y-Axis Label",
            fontSize: 12,
            fontColor: "black",
            padding: 10,
          },
        },
      ],
      xAxes: [
        {
          id: "months",
          offset: true,
          type: "category",
          distribution: "series",
          time: {
            unit: "month",
            displayFormats: {
              month: "MMM",
            },
          },
          position: "bottom",
          ticks: {
            fontSize: 6,
            fontColor: "red",
            padding: 10,
          },
          gridLines: {
            display: false,
            color: "rgba(0, 0, 0, 0.1)",
          },
          scaleLabel: {
            display: true,
            labelString: "X-Axis Label",
            fontSize: 12,
            fontColor: "black",
            padding: 10,
          },
        },
      ],
    },
    tooltips: {
      enabled: true,
      mode: "index",
      intersect: false,
      backgroundColor: "rgba(0,0,0,0.8)",
      titleFontColor: "white",
      titleFontSize: 14,
      titleMarginBottom: 10,
      bodyFontColor: "white",
      bodyFontSize: 12,
      bodySpacing: 10,
      xPadding: 10,
      yPadding: 10,
      caretSize: 8,
      cornerRadius: 6,
      displayColors: false,
    },
  };

  return type === "line" ? lineOptions : lineOptions;
}
