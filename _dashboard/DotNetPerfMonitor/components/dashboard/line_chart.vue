<template>
    <div>
        <UCard>
            <LineChart :data="data" :options="config" />
        </UCard>
    </div>
</template>

<script setup>
const props = defineProps({
    scenario: String,
    groupedData: Object,
})

const groupedData = props.groupedData
const scenario = props.scenario
const filtered = groupedData.get(scenario)

const _rows = [];
const benchmarks = useColumnsetExtractor(filtered, "test case")
benchmarks.forEach(async (benchmark) => {
    const _data = useBenchmarkGrouper(filtered, benchmark)

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