<template>
    <div>
        <UCard>
            <LineChart :data="data" :options="config" />
        </UCard>
    </div>
</template>

<script setup>
import * as d3 from 'd3'

const props = defineProps({
    scenario: String,
    groupedData: Object,
})

const groupedData = props.groupedData
const scenario = props.scenario
const filtered = groupedData.get(scenario)

const _rows = [];
const benchmarks = useColumnsetExtractor(filtered, "test case")
const d3colors = d3.scaleOrdinal(d3.schemeCategory10)
d3colors.domain(benchmarks);

benchmarks.forEach(async (benchmark) => {
    const _data = filtered.filter((item) => item["test case"] === benchmark)

    const color = d3colors(benchmark)

    const _dataset = {
        label: benchmark,
        fill: false,
        type: 'line',
        borderWidth: .5,
        pointRadius: .5,
        cubicInterpolationMode: 'monotone',
        backgroundColor: color,
        borderColor: color,
        data: _data
    }
    _rows.push(_dataset)
})

const config = useChartOptions('line')
const data = computed(() => {
    return {
        labels: filtered.map((item) => item.timestamp),
        datasets: _rows,
    }
})
</script>