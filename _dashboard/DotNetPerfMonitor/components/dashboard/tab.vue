<template>
    <div class="flex flex-col justify-between gap-8">

        <div class="flex flex-col gap-4">

            <div class="flex flex-row justify-between py-4">
                <p class="text-2xl text-sky-400 dark:text-sky-300">Filter</p>
                <UButton icon="i-heroicons-rectangle-group" size="sm" color="primary" variant="solid" label="Filter"
                    trailing @click="isOpen = true" />
            </div>

            <div v-for="scenario, index in scenariosList" :key="index">
                <div v-if="selectedScenarios[index]" class="flex flex-col gap-2">
                    <h1 class="text-2xl first-letter:capitalize">{{ scenario }}</h1>
                    <DashboardLineChart :scenario="scenario" :groupedData="groupedData" />
                </div>
            </div>
        </div>
        <USlideover v-model="isOpen">
            <div class="flex flex-col gap-2 px-6 py-8">

                <UCard>
                    <p class="self-center text-2xl py-2">Apply filter for scenarios</p>
                    <UCheckbox v-for="scenario, index in scenariosList" :key="index" v-model="selectedScenarios[index]"
                        :name="scenario" :label="scenario" />
                </UCard>
            </div>
        </USlideover>
    </div>
</template>

<script setup>

const props = defineProps({
    path: String
})

const isOpen = ref(false)

const data = await useCsvConverter("https://raw.githubusercontent.com/G-Research/DotNetPerfMonitor/main/" + props.path)
const groupedData = groupBy(data, 'scenario')
const scenariosList = [...groupedData.keys()]
const selectedScenarios = ref(new Array(scenariosList.length).fill(true))
</script>
