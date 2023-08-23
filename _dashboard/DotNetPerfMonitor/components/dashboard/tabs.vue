<template>
    <div class="px-2 py-4 sm:px-0 self-center w-full">
        <TabGroup>
            <TabList class="flex space-x-1 rounded-xl  p-1 bg-gray-100 dark:bg-sky-900">
                <Tab v-for="element in _elements" as="template" :key="element[0]" v-slot="{ selected }">
                    <button :class="[
                        'w-full rounded-lg py-2.5 text-sm font-bold leading-5 text-sky-700 dark:text-gray-100',
                        selected
                            ? 'bg-sky-400 shadow'
                            : 'text-blue-100 hover:bg-sky-200 hover:text-sky-900',
                    ]">
                        {{ element[0] }}
                    </button>
                </Tab>
            </TabList>

            <TabPanels class="mt-2">
                <TabPanel v-for="element in _elements">
                    <DashboardTab :path="element[1]" />
                </TabPanel>
            </TabPanels>
        </TabGroup>
    </div>
</template>

<script setup>
const _elements = [
        ["NuGet", "data/nuget.csv"],
        ["MSBuild", "data/msbuild.csv"],
        ["F#", "data/fsharp.csv"],
        ["C#", "data/csharp.csv"],
    ]
</script>
