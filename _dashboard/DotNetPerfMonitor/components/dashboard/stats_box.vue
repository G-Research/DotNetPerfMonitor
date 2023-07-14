<template>
    <UCard class="w-1/4" :ui="preset" :background="statistic.background">
        <div class="flex flex-col gap-2">
            <div class="flex flex-row gap-4">
                <i :class="statistic.icon" class="text-4xl"></i>
                <p class="text-sky-800 dark:text-sky-300 text-xl font-normal">{{ statistic.title }}</p>
            </div>
            <p class="text-gray-300 text-sm">{{ statistic.desc }}</p>
            <h1 class="text-sky-800 dark:text-sky-300 text-xl font-bold big py-2">{{ statistic.data }}</h1>
        </div>
    </UCard>
</template>

<script lang="ts" setup>
const statistic = defineProps({
    title: String,
    data: Number,
    background: String,
    desc: String,
    icon: String,
});
const background = statistic.background
const preset = {
    "base": "overflow-hidden",
    "background": `dark:bg-gray-900`,
    "divide": "divide-y divide-gray-200 dark:divide-gray-800",
    "ring": "ring-1 ring-gray-200 dark:ring-gray-800",
    "rounded": "rounded-xl",
    "shadow": "shadow",
    "body": {
        "base": "",
        "background": "",
        "padding": "px-4 py-5 sm:p-6"
    },
    "header": {
        "base": "",
        "background": "",
        "padding": "px-2 py-4 sm:px-6"
    },
    "footer": {
        "base": "",
        "background": "",
        "padding": "px-4 py-4 sm:px-6"
    }
}

</script>

<style scoped>
.big {
    font-size: 3rem;
}
</style>