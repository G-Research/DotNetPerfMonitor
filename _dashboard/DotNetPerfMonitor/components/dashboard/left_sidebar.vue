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

</script>
<template>
    <div class="flex flex-col h-screen">
        <UVerticalNavigation :links="links" />
    </div>
</template>
