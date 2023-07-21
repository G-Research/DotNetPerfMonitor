<template>
    <div>
        <div class="chart-div">
            <LineChart :data="data" category="line" />
        </div>
    </div>
</template>


<script setup>
const data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [{
        label: 'My First dataset',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0, 10, 5, 2, 20, 30, 45],
    }]

}
const path = 'https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data.csv'
const convertedData = useCsvConverter(path)
console.log(convertedData)
</script>