<template>
    <div ref="chart"></div>
</template>

<script>
import * as d3 from 'd3';

export default {
    mounted() {
        this.drawChart();
    },
    methods: {
        drawChart() {
            const data = [
                { date: '2021-01-01', value: 65 },
                { date: '2021-02-01', value: 59 },
                { date: '2021-03-01', value: 80 },
                { date: '2021-04-01', value: 81 },
                { date: '2021-05-01', value: 56 },
                { date: '2021-06-01', value: 55 },
                { date: '2021-07-01', value: 40 }
            ];

            const margin = { top: 20, right: 20, bottom: 30, left: 50 };
            const width = 400;
            const height = 300;

            const svg = d3
                .select(this.$refs.chart)
                .append('svg')
                .attr('width', width + margin.left + margin.right)
                .attr('height', height + margin.top + margin.bottom)
                .append('g')
                .attr('transform', `translate(${margin.left}, ${margin.top})`);

            const x = d3
                .scaleTime()
                .domain(d3.extent(data, d => new Date(d.date)))
                .range([0, width]);

            const y = d3
                .scaleLinear()
                .domain([0, d3.max(data, d => d.value)])
                .range([height, 0]);

            const line = d3
                .line()
                .x(d => x(new Date(d.date)))
                .y(d => y(d.value));

            svg
                .append('path')
                .datum(data)
                .attr('fill', 'none')
                .attr('stroke', 'steelblue')
                .attr('stroke-width', 2)
                .attr('d', line);

            svg
                .append('g')
                .attr('transform', `translate(0, ${height})`)
                .call(d3.axisBottom(x));

            svg.append('g').call(d3.axisLeft(y));
        }
    }
};
</script>
