<template>
    <div class="flex flex-col justify-between gap-8">
        <div class="flex flex-row w-full gap-8">
            <DashboardStatsBox v-for="(stat, index) in statistics" :key="index" :title="stat.title" :data="stat.data"
                :icon="stat.icon" :background="stat.background" :desc="stat.desc" />
        </div>
        <!-- <DashboardLineChart /> -->
        <UCard>
            <div class="flex flex-col gap-6">
                <div class="flex flex-row justify-between">
                    <div class="flex flex-row gap-4 justify-center">
                        <UIcon :name="selected.icon" class="text-4xl " />
                        <div class="text-3xl font-semibold text-sky-400">{{ selected.label }} Scenario</div>
                    </div>

                    <USelectMenu v-model="selected" :options="scenarios" searchable="true"
                        searchable-placeholder="Search a scenario...">
                        <template #label>
                            <UIcon :name="selected.icon" class="w-4 h-4 text-sky-400" />
                            {{ selected.label }}
                        </template>
                    </USelectMenu>


                </div>

                <DashboardLineChart />
            </div>
        </UCard>

    </div>
</template>

<script setup>
const scenarios = [{
    id: 'cold',
    label: 'Cold',
    icon: 'i-heroicons-cloud'
},
{
    id: 'warmup',
    label: 'Warmup',
    icon: 'i-heroicons-fire'
},
{
    id: 'noop',
    label: 'Noop',
    icon: 'i-heroicons-stop-circle'
},
{
    id: 'force',
    label: 'Force',
    icon: 'i-heroicons-bolt'
},
{
    id: 'arctic',
    label: 'Arctic',
    icon: 'i-heroicons-cube-transparent'
}
]
const selected = ref(scenarios[0])
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
