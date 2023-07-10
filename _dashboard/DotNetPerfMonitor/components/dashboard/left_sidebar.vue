<script setup>
const links = [{
    label: 'Dashboard',
    icon: 'i-heroicons-squares-plus',
    to: '/'
}, {
    label: 'Regressions',
    icon: 'i-heroicons-chart-bar',
    to: '/regressions'
}, {
    label: 'Notifications',
    icon: 'i-heroicons-bell',
    to: '/notifications',
    badge: 14
}, {
    label: 'Settings',
    icon: 'i-heroicons-cog',
    to: '/settings'
}]

const preset = {
    "padding": "px-3 py-2",
    "width": "w-full",
    "rounded": "rounded-lg",
    "font": "font-medium",
    "size": "text-lg",
    "icon": {
        "base": "flex-shrink-0 w-7 h-7 text-xl",
        "active": "text-gray-700 dark:text-gray-200 text-xl",
        "inactive": "text-gray-400 dark:text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-200 text-xl"
    },
}

</script>
<template>
    <div class="flex flex-col h-screen">
        <h2 class="text-2xl text-center py-3 text-blue-300">G-Research</h2>
        <UVerticalNavigation :links="links" :ui="preset" />
    </div>
</template>
