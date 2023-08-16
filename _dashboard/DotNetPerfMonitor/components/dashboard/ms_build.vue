<template>
    <div class="flex flex-col justify-between gap-8">
        <div class="flex flex-row w-full gap-8">
            <DashboardStatsBox v-for="(stat, index) in statistics" :key="index" :title="stat.title" :data="stat.data"
                :icon="stat.icon" :background="stat.background" :desc="stat.desc" />
        </div>

        <!-- <DashboardLineChart /> -->

        <div class="flex flex-col gap-4">
            <div class="flex flex-row justify-between py-4">
                <p class="text-2xl text-sky-400 dark:text-sky-300">Filter</p>
                <UButton icon="i-heroicons-rectangle-group" size="sm" color="primary" variant="solid" label="Filter"
                    trailing @click="isOpen = true" />

                <!-- <div class="flex flex-row gap-4 justify-center">
                        <UIcon :name="selected.icon" class="text-4xl " />
                        <div class="text-3xl font-semibold text-sky-400">{{ selected.label }} Scenario</div>
                    </div> -->

                <!-- <USelectMenu v-model="selected" :options="scenarios" :searchable="searchable"
                        searchable-placeholder="Search...">
                        <template #label>
                            <UIcon :name="selected.icon" class="w-4 h-4 text-sky-400" />
                            {{ selected.label }}
                        </template>
                    </USelectMenu> -->


            </div>
            <!-- <DashboardPlotly /> -->

            <div v-for="scenario, index in scenariosList" :key="index">
                <div v-if="selectedScenarios[index]" class="flex flex-col gap-2">
                    <h1 class="text-2xl first-letter:capitalize">{{ scenario }}</h1>
                    <DashboardLineChart :scenario="scenario" />
                </div>
            </div>
        </div>
        <USlideover v-model="isOpen">
            <div class="flex flex-col gap-2 px-6 py-8">

                <UCard>
                    <p class="self-center text-2xl py-2">Apply filter for scenarios</p>
                    <UCheckbox v-for="scenario, index in scenariosList" :key="index" v-model="selectedScenarios[index]"
                        :name="scenario" :label="scenario" cl />
                </UCard>
            </div>
        </USlideover>
    </div>
</template>

<script setup>
const searchable = true
const isOpen = ref(false)

const generateBooleans = (length) => {
    const arr = [];
    for (let i = 0; i < length; i++) arr.push(true)
    return arr;
}
const path = "https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/data/msbuild.csv"
const converted = await useCsvConverter(path)

const scenariosList = useColumnsetExtractor(converted, 'scenario')
const selectedScenarios = ref(generateBooleans(scenariosList.length))
//['noop', 'force', 'cold', 'arctic', 'warmup']

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
const scenario = useAlphaScenario()
watch(selected, (fresh, old) => {
    scenario.value = fresh.id
})



const benchmarks = useColumnsetExtractor(converted, 'solution')

const statistics = [
    {
        title: 'Scenarios',
        desc: 'Scenarios used in benchmarks',
        data: scenariosList.length,
        icon: 'i-heroicons-variable',
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
        data: benchmarks.length,
        icon: 'i-heroicons-beaker',
        background: 'bg-gray-800'
    }
]

</script>
