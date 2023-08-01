<template>
    <div class="flex flex-col gap-4">
        <h1 class="text-2xl self-center">MS BUILD</h1>
        <div class="flex flex-row w-full gap-8">
            <DashboardStatsBox v-for="(stat, index) in statistics" :key="index" :title="stat.title" :data="stat.data"
                :icon="stat.icon" :background="stat.background" :desc="stat.desc" />
        </div>
    </div>
</template>

<script setup>

const statistics = [
    {
        title: 'MS Build X',
        desc: 'Important stats',
        data: 2,
        icon: 'i-heroicons-arrow-trending-down',
        background: 'bg-purple-400'
    },
    {
        title: 'MS Build Y',
        desc: 'MS Build Stats',
        data: 12,
        icon: 'i-heroicons-exclamation-circle',
        background: 'bg-red-400'
    },
    {
        title: 'MS Build Z',
        desc: 'MS Build Stats',
        data: 4,
        icon: 'i-heroicons-arrow-path-rounded-square',
        background: 'bg-green-400'
    },
    {
        title: 'MS Build U',
        desc: 'MS Build Stats',
        data: 24,
        icon: 'i-heroicons-variable',
        background: 'bg-gray-800'
    }
]
</script>