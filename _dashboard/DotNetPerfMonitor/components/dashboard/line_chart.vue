<template>
    <div>
        <UCard>

            <LineChart :data="data" :options="config" />
        </UCard>

    </div>
</template>


<script  setup>
const props = defineProps({
    scenario: String
})
const path = "https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data/nuget.csv"
//const file = '../../../../data/nuget.csv'
const converted = await useCsvConverter(path)
const scenario = useAlphaScenario()
const filtered = useScenarioFilter(converted, props.scenario)

const _options = useChartOptions('line')
const _rows = [];
const benchmarks = useColumnsetExtractor(converted, 'test case')
benchmarks.forEach(async (benchmark) => {
    const _data = useBenchmarkGrouper(filtered, benchmark)
    const clean_data = _data.map((x) => {
        const row = { x: new Date(x.timestamp), y: x.duration }
        return row
    })
    //const _color = await useBenchmarkColor(benchmark)
    // Programatically generate colors and assign them to the benchmark
    const _color = useColorGenerator()

    const _dataset = {
        label: benchmark,
        fill: false,
        type: 'line',
        borderWidth: .5,
        pointRadius: .5,
        cubicInterpolationMode: 'monotone',
        backgroundColor: _color,
        borderColor: _color,
        data: _data
    }
    _rows.push(_dataset)
})
const config = useChartOptions('line')
const data = computed(() => {
    return {
        labels: useDataExtracter(filtered, 'timestamp'),
        datasets: _rows,
    }
})
</script>