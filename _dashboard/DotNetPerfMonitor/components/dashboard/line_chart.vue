<template>
    <div>
        <div class="chart-div">
            <LineChart :data="data" />
        </div>
    </div>
</template>


<script setup>

const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'

const converted = await useCsvConverter(path)
const filtered = useScenarioFilter(converted, 'cold')
const largeAppCPM = useBenchmarkGrouper(filtered, "LargeAppCPM-142722b")
const largeAppCPM64 = useBenchmarkGrouper(filtered, "LargeAppCPM64-142722b")
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
    }
};

const _options = useChartOptions('line')
const data = {
    labels: useDataExtracter(filtered, 'timestamp'),
    options: _options,
    datasets: [{
        label: 'OrchardCore',
        fill: false,
        type: 'line',
        tension: .1,
        backgroundColor: scenarioColors.warmup.bgColor,
        borderColor: scenarioColors.warmup.lineColor,
        data: orchardcore.map((x) => {
            const _data = { x: x.timestamp, y: x.duration, }
            return _data

        }),
    },
    {
        label: 'largeAppCPM',
        fill: false,
        type: 'line',
        tension: .1,
        backgroundColor: scenarioColors.force.bgColor,
        borderColor: scenarioColors.force.lineColor,
        data: largeAppCPM.map((x) => {
            const _data = { x: x.timestamp, y: x.duration, }
            return _data

        }),
    },

    {
        label: 'NuGet',
        fill: false,
        type: 'line',
        tension: .1,
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
        type: 'line',
        tension: .1,
        backgroundColor: scenarioColors.arctic.bgColor,
        borderColor: scenarioColors.arctic.lineColor,
        data: orleans.map((x) => {
            const _data = { x: x.timestamp, y: x.duration }
            return _data

        }),
    }

    ]
}
</script>