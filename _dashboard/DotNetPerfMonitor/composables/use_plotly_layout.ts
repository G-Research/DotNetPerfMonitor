export default function usePlotlyLayout() {
  return {
    annotations: [],
    hovermode: "closest",
    hoverlabel: { align: "left", font: { size: 8 } },
    legend: {
      title: {
        text: "Test case",
      },
      tracegroupgap: 0,
    },
    title: {
      x: 0.5,
      text: "NuGet Performance Monitor",
      font: { size: 18 },
    },
    mapbox: { style: "light" },
    template: {
      layout: {
        font: {
          color: "#2a3f5f",
          size: 8,
        },
        hovermode: "closest",
        hoverlabel: {
          align: "left",
        },
        paper_bgcolor: "#00AAE1",
        //"plot_bgcolor": "#00AAE1", - G-Research blue
        plot_bgcolor: "#E5ECF6",
        xaxis: {
          gridcolor: "white",
          linecolor: "white",
          ticks: "",
          title: {
            standoff: 15,
          },
          zerolinecolor: "white",
          automargin: true,
          zerolinewidth: 2,
        },
        yaxis: {
          gridcolor: "white",
          linecolor: "white",
          ticks: "%",
          title: {
            standoff: 15,
          },
          zerolinecolor: "white",
          automargin: true,
          zerolinewidth: 2,
        },
      },
    },
  };
}
