<template>
    <div class="flex flex-col px-4 py-4">
        <UtilsSearchBox />
        <UDivider />

        <div
            class="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700">
            <ul class="flex flex-wrap -mb-px">
                <li class="mr-2">
                    <a href="#"
                        class="inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300">NuGet</a>
                </li>
                <li class="mr-2">
                    <a href="#"
                        class="inline-block p-4 text-blue-600 border-b-2 border-blue-600 rounded-t-lg active dark:text-blue-500 dark:border-blue-500"
                        aria-current="page">F#</a>
                </li>
                <li class="mr-2">
                    <a href="#"
                        class="inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300">.NET
                        SDK</a>
                </li>

            </ul>
        </div>
        <DashboardLineChart />
    </div>
</template>


<script setup>
const { metaSymbol } = useShortcuts()
</script>