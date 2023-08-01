<template>
    <div>
        <!-- <client-only>
            <nuxt-plotly :data="data"></nuxt-plotly>
        </client-only> -->
        <LineChart :data="data" />

    </div>
</template>


<script setup>
const props = defineProps({
    scenario: String
})
const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'

const converted = await useCsvConverter(path)
const scenario = useAlphaScenario()
const filtered = useScenarioFilter(converted, 'noop')
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
    const _data = { x: x.timestamp, y: x.duration, }
    return _data

})
const data = {
    labels: useDataExtracter(filtered, 'timestamp'),
    options: _options,
    datasets: [{
        label: 'OrchardCore',
        fill: true,
        borderWidth: .5,
        pointRadius: .5,
        type: 'line', tension: 0.4,
        cubicInterpolationMode: 'monotone',
        backgroundColor: scenarioColors.warmup.bgColor,
        borderColor: scenarioColors.warmup.lineColor,
        data: see
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
        data: largeAppCPM.map((x) => {
            const _data = { x: x.timestamp, y: x.duration > 20 ? 18 : x.duration, }
            return _data

        }),
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
        data: largeAppCPM64.map((x) => {
            const _data = { x: x.timestamp, y: x.duration, }
            return _data

        }),
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
        data: nuget.map((x) => {
            const _data = { x: x.timestamp, y: x.duration, }
            return _data

        }),
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
        data: orleans.map((x) => {
            const _data = { x: x.timestamp, y: x.duration }
            return _data

        }),
    }

    ],
    options: _options
}
</script>