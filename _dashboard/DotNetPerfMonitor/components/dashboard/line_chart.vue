<template>
    <div>
        <div class="chart-div">
            <LineChart :data="data" category="line" />
        </div>
    </div>
</template>


<script setup>

const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'
const convertedData = await useCsvConverter(path)
console.log(useScenarioFilter(convertedData, 'cold'));
const scenarioColors = {
    warmup: {
        bgColor: 'rgb(255, 99, 132)',
        lineColor: 'rgb(255, 99, 132)'
    },
    noop: {
        bgColor: 'rgb(54, 162, 235)',
        lineColor: 'rgb(54, 162, 235)'
    },
    force: {
        bgColor: 'rgb(255, 205, 86)',
        lineColor: 'rgb(255, 205, 86)'
    },
    cold: {
        bgColor: 'rgb(75, 192, 192)',
        lineColor: 'rgb(75, 192, 192)'
    },
    arctic: {
        bgColor: 'rgb(153, 102, 255)',
        lineColor: 'rgb(153, 102, 255)'
    }
};
const data = {
    labels: ['February', 'March', 'April', 'May', 'June',],
    datasets: [{
        label: 'Warmup',
        backgroundColor: scenarioColors.warmup.bgColor,
        borderColor: scenarioColors.warmup.lineColor,
        data: useScenarioFilter(convertedData, 'warmup')
    },
    {
        label: 'Noop',
        backgroundColor: scenarioColors.noop.bgColor,
        borderColor: scenarioColors.noop.lineColor,
        data: useScenarioFilter(convertedData, 'noop')
    },
    {
        label: 'Force',
        backgroundColor: scenarioColors.force.bgColor,
        borderColor: scenarioColors.force.lineColor,
        data: useScenarioFilter(convertedData, 'force')
    },
    {
        label: 'Cold',
        backgroundColor: scenarioColors.cold.bgColor,
        borderColor: scenarioColors.cold.lineColor,
        data: useScenarioFilter(convertedData, 'cold')
    },
    {
        label: 'Arctic',
        backgroundColor: scenarioColors.arctic.bgColor,
        borderColor: scenarioColors.arctic.lineColor,
        data: useScenarioFilter(convertedData, 'arctic')
    }

    ]
}
const options = {
    "tension": .9,
    "responsive": true,
    "maintainAspectRatio": false,
    "title": {
        "display": true,
        "text": "Line Chart"
    },
    "legend": {
        "display": true,
        "position": "top",
        "labels": {
            "fontSize": 12,
            "fontColor": "black",
            "usePointStyle": false,
            "padding": 10
        }
    },
    "scales": {
        "yAxes": [
            {
                "id": "y-axis-1",
                "type": "linear",
                "position": "left",
                "ticks": {
                    "beginAtZero": true,
                    "suggestedMax": 100,
                    "stepSize": 10,
                    "fontSize": 12,
                    "fontColor": "black",
                    "padding": 10
                },
                "gridLines": {
                    "display": false,
                    "color": "rgba(0, 0, 0, 0.1)"
                },
                "scaleLabel": {
                    "display": true,
                    "labelString": "Y-Axis Label",
                    "fontSize": 12,
                    "fontColor": "black",
                    "padding": 10
                }
            }
        ],
        "xAxes": [
            {
                "id": "x-axis-1",
                "type": "category",
                "position": "bottom",
                "ticks": {
                    "fontSize": 12,
                    "fontColor": "black",
                    "padding": 10
                },
                "gridLines": {
                    "display": false,
                    "color": "rgba(0, 0, 0, 0.1)"
                },
                "scaleLabel": {
                    "display": true,
                    "labelString": "X-Axis Label",
                    "fontSize": 12,
                    "fontColor": "black",
                    "padding": 10
                }
            }
        ]
    },
    "tooltips": {
        "enabled": true,
        "mode": "index",
        "intersect": false,
        "backgroundColor": "rgba(0,0,0,0.8)",
        "titleFontColor": "white",
        "titleFontSize": 14,
        "titleMarginBottom": 10,
        "bodyFontColor": "white",
        "bodyFontSize": 12,
        "bodySpacing": 10,
        "xPadding": 10,
        "yPadding": 10,
        "caretSize": 8,
        "cornerRadius": 6,
        "displayColors": false
    }
}
</script>