<template>
    <div class="px-2 py-4 sm:px-0 self-center w-full">
        <TabGroup>
            <TabList class="flex space-x-1 rounded-xl  p-1 bg-gray-100 dark:bg-sky-900">
                <Tab v-for="category in _elements" as="template" :key="category.uid" v-slot="{ selected }">
                    <button :class="[
                        'w-full rounded-lg py-2.5 text-sm font-bold leading-5 text-sky-700 dark:text-gray-100',
                        selected
                            ? 'bg-sky-400 shadow'
                            : 'text-blue-100 hover:bg-sky-200 hover:text-sky-900',
                    ]">
                        {{ category.name }}
                    </button>
                </Tab>
            </TabList>

            <TabPanels class="mt-2">
                <TabPanel>
                    <DashboardNuget />
                </TabPanel>
                <TabPanel>
                    <DashboardMsBuild />
                </TabPanel>
                <TabPanel>
                    <DashboardFSharp />
                </TabPanel>
                <TabPanel>
                    <DashboardCSharp />
                </TabPanel>
            </TabPanels>
        </TabGroup>
    </div>
</template>

<script setup>
import { ref } from 'vue'
// const components = [
//     DashboardNuget,
//     DashboardMsBuild,
//     DashboardFSharp,
//     DashboardCSharp,
// ]
const config = await useDataConfig()
useLogger("[CONFIG]", config.display)
const _elements = computed(() => config.components)
const categories = computed(() => ["NuGet", "MS Build", "F#", "C#",])
</script>
