<script lang="ts" setup>
import ref from 'vue'
const mode = useColorMode()
const src = useRuntimeConfig().app.baseURL + (mode.value === 'dark' ? 'images/logo.png' : 'images/logo-bg.png')
const links = [{
    label: 'Dashboard',
    icon: 'i-heroicons-squares-plus',
    to: '/',

}, {
    label: 'Regressions',
    icon: 'i-heroicons-chart-bar',
    to: '/regressions',
    //badge: `${useRegressionsNumber().value}`,
},

// {
// label: 'Notifications',
// icon: 'i-heroicons-bell',
// to: '/notifications',
// badge: 14
// },

{
    label: 'Data Explorer',
    // icon: 'i-heroicons-sparkles',
    icon: 'i-heroicons-circle-stack',
    to: '/documentation',
},
    // {
    // label: 'Settings',
    // icon: 'i-heroicons-cog',
    // to: '/settings'
    // },
]

const preset = {
    "padding": "px-3 py-3",
    "width": "w-full",
    "rounded": "rounde-xl",
    "font": "font-normal",
    "size": "text-md",
    "active": "text-gray-900 dark:text-white before:bg-gray-100 dark:before:bg-sky-900",
    "inactive": "text-gray-200 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:before:bg-gray-50 dark:hover:before:bg-sky-900",
    "icon": {
        "base": "flex-shrink-0 w-7 h-7 text-xl",
        "active": "text-gray-700 dark:text-gray-200 text-xl",
        "inactive": "text-gray-100 dark:text-gray-100 group-hover:text-gray-600 dark:group-hover:text-gray-200 text-lg"
    },
}

</script>
<template>
    <div class="h-screen bg-sky-500 dark:bg-sky-950">
        <div class="flex flex-row py-4 px-4 text-ellipsis">
            <UAvatar :src="src" alt="logo" class="" size="sm" />
            <h2 class="dark:text-sky-400 text-white font-bold xl:text-2xl sm:text-lg xs:text-xs text-sm xs:hidden px-1">
                G-Research
            </h2>
        </div>
        <UVerticalNavigation :links="links" :ui="preset" class="px-1" />
    </div>
</template>
