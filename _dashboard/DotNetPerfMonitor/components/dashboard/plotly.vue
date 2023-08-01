<template>
    <div>
        <nuxt-plotly :data="data" :layout="layout" @on-ready="onReady" />
    </div>
</template>


<script setup>

const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'
const data = await useCsvConverter(path)
const layout = usePlotlyLayout()
const onReady = computed(() => {
    alert('ready')
})
</script>