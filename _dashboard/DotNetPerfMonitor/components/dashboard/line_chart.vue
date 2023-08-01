<template>
    <div>
        <LineChart :data="data" :options="config" />

    </div>
</template>


<script  setup>
import 'chartjs-adapter-date-fns';
import { enUS } from 'date-fns/locale';

const props = defineProps({
    scenario: String
})
const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'

const converted = await useCsvConverter(path)
const scenario = useAlphaScenario()
const filtered = useScenarioFilter(converted, props.scenario)
const largeAppCPM = useBenchmarkGrouper(filtered, "LargeAppCPM-142722b")
const largeAppCPM64 = useBenchmarkGrouper(filtered, "LargeAppCPM-nostaticgraph-142722b")
const orleans = useBenchmarkGrouper(filtered, "Orleans-eda972a")
const orchardcore = useBenchmarkGrouper(filtered, "OrchardCore-5dbd92c")
const nuget = useBenchmarkGrouper(filtered, "NuGetClient-win-d76a117",)
//console.log(useScenarioFilter(converted, "LargeAppCPM-142722b",));
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
    },
    hot: {
        bgColor: 'rgb(56, 142, 60)',
        lineColor: 'rgb(56, 142, 60)'
    }
};

const _options = useChartOptions('line')
const see = orchardcore.map((x) => {
    const _data = { x: x.timestamp, y: x.duration, benchmark: x.solution }
    return _data

})
const _rows = [];
const benchmarks = useColumnsetExtractor(converted, 'solution')
benchmarks.forEach((benchmark) => {
    const _data = useBenchmarkGrouper(filtered, benchmark)
    const clean_data = _data.map((x) => {
        const row = { x: new Date(x.timestamp), y: x.duration }
        return row
    })
    const _dataset = {
        label: benchmark,
        fill: false,
        type: 'line', tension: 0.4,
        borderWidth: .5,
        pointRadius: .5,
        cubicInterpolationMode: 'monotone',
        backgroundColor: scenarioColors.warmup.bgColor,
        borderColor: scenarioColors.warmup.lineColor,
        data: _data
    }
    _rows.push(_dataset)
})
const config = computed(() => {
    return {
        responsive: true,
        maintainAspectRatio: false,
        parsing: {
            xAxisKey: 'timestamp',
            yAxisKey: 'relative duration'
        },
        scales: {
            x: {
                type: 'timeseries',
                adapters: {
                    date: {
                        displayFormats: {
                            quarter: 'MMM YYYY'
                        },
                        locale: enUS,
                    },
                },
            },
            y: {
                type: 'logarithmic',
                ticks: {
                    callback: function (value, index, values) {
                        return Number(value.toString());//pass tick values as a string into Number function
                    }
                }
            },

        },

        plugins: [],
        tooltips: {
            callbacks: {
                label(tooltipItem, data) {
                    const label = data.datasets[tooltipItem.datasetIndex].label;
                    const value = tooltipItem.yLabel

                    return `${label}: ${value}`;
                }
            }
        }
    }
})

const data = computed(() => {
    return {
        labels: useDataExtracter(filtered, 'timestamp'),
        //datasets: _rows,
        datasets: [{
            label: 'OrchardCore',
            fill: true,
            borderWidth: .5,
            pointRadius: .5,
            type: 'line', tension: 0.4,
            cubicInterpolationMode: 'monotone',
            backgroundColor: scenarioColors.warmup.bgColor,
            borderColor: scenarioColors.warmup.lineColor,
            data: orchardcore,
            showLine: true,

        },
        {
            label: 'largeAppCPM',
            fill: false,
            type: 'line',
            tension: 0.4,
            borderWidth: .5,
            pointRadius: .5,
            cubicInterpolationMode: 'monotone',
            backgroundColor: scenarioColors.force.bgColor,
            borderColor: scenarioColors.force.lineColor,
            data: largeAppCPM
        },
        {
            label: 'largeAppCPM-Nostaticgraph',
            fill: true,
            type: 'line',
            tension: 0.1,
            borderWidth: .5,
            pointRadius: .5,
            cubicInterpolationMode: 'monotone',
            backgroundColor: scenarioColors.hot.bgColor,
            borderColor: scenarioColors.hot.lineColor,
            data: largeAppCPM64
        },

        {
            label: 'NuGet',
            fill: false,
            type: 'line', tension: 0.4,
            borderWidth: .5,
            pointRadius: .5,
            cubicInterpolationMode: 'monotone',
            backgroundColor: scenarioColors.noop.bgColor,
            borderColor: scenarioColors.noop.lineColor,
            data: nuget
        },
        {
            label: 'Orleans',
            fill: false,
            type: 'line', tension: 0.4,
            borderWidth: .5,
            pointRadius: .5,
            cubicInterpolationMode: 'monotone',
            backgroundColor: scenarioColors.arctic.bgColor,
            borderColor: scenarioColors.arctic.lineColor,
            data: orleans
        }

        ],
        //options: _options
    }
})
</script>