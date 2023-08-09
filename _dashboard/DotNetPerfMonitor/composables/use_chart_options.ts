import "chartjs-adapter-date-fns";
import { enUS } from "date-fns/locale";

export default function useChartOptions(type: String) {
  const lineOptions = computed(() => {
    return {
      responsive: true,
      legend: {
        display: false,
      },
      maintainAspectRatio: true,
      tooltips: {
        enabled: true,
        callbacks: {
          label: function (tooltipItem: any, data: any) {},
        },
      },

      parsing: {
        xAxisKey: "timestamp",
        yAxisKey: "relative duration",
      },
      plugins: {
        zoom: {
          zoom: {
            wheel: {
              enabled: true,
            },
            pinch: {
              enabled: true,
            },
            mode: "xy",
          },
        },
        tooltip: {
          callbacks: {
            footer: (tooltipItems: any) => {
              let summary = "";
              tooltipItems.forEach(function (tooltipItem: any) {
                const row = tooltipItem.raw;
                summary += "Scenario: " + row.scenario + "\n";
                summary += "Version: " + row.version + "\n";
                summary += "Base Version: " + row["base version"] + "\n";
                summary += "Duration: " + row.duration + "s \n";
                summary +=
                  "Relative Duration: " + row["relative duration"] + "s \n";
                summary += "Base Duration: " + row["base duration"] + "s \n";
              });
              return summary;
            },
          },
        },
      },

      scales: {
        x: {
          type: "timeseries",
          title: {
            display: true,
            text: "Benchmark Test Date",
          },
          ticks: {
            display: true,
          },
          grid: {
            display: false, // Disable vertical grid lines
          },
          adapters: {
            date: {
              displayFormats: {
                quarter: "MMM YYYY",
              },
              locale: enUS,
            },
          },
        },
        y: {
          type: "logarithmic",
          title: {
            display: true,
            text: "Relative Duration",
          },
          grid: {
            display: false, // Disable vertical grid lines
          },
          ticks: {
            callback: function (value: any, index: number, values: any) {
              return Number(value.toString()); //pass tick values as a string into Number function
            },
          },
        },
      },
    };
  });

  return type === "line" ? lineOptions : lineOptions;
}
