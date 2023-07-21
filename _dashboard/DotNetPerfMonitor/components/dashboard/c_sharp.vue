<template>
    <div class="flex flex-col justify-between">
        <div class="flex flex-row w-full gap-8">
            <DashboardStatsBox v-for="(stat, index) in statistics" :key="index" :title="stat.title" :data="stat.data"
                :icon="stat.icon" :background="stat.background" :desc="stat.desc" />
        </div>
        <DashboardLineChart />
    </div>
</template>

<script setup>
const statistics = [
    {
        title: 'Regressions',
        desc: 'Performance regressions',
        data: 2,
        icon: 'i-heroicons-arrow-trending-down',
        background: 'bg-purple-400'
    },
    {
        title: 'Issues',
        desc: 'Active issues on Github',
        data: 12,
        icon: 'i-heroicons-exclamation-circle',
        background: 'bg-red-400'
    },
    {
        title: 'Pull Requests',
        desc: 'Active pull requests',
        data: 4,
        icon: 'i-heroicons-arrow-path-rounded-square',
        background: 'bg-green-400'
    },
    {
        title: 'Benchmarks',
        desc: 'Benchmarks tests',
        data: 24,
        icon: 'i-heroicons-variable',
        background: 'bg-gray-800'
    }
]
</script>
