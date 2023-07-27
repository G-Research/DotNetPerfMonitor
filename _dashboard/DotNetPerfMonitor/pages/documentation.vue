<template>
    <div class="flex flex-col gap-4 px-12 py-12">
        <UInput v-model="q" placeholder="Filter data..." />
        <UTable :columns="columns" :rows="rows" sort-asc-icon="i-heroicons-arrow-up-20-solid"
            sort-desc-icon="i-heroicons-arrow-down-20-solid"
            :sort-button="{ icon: 'i-heroicons-sparkles-20-solid', color: 'primary', variant: 'outline', size: '2xs', square: false, ui: { rounded: 'rounded-full' } }"
            :loading-state="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }" />
        <UPagination v-model="page" :page-count="pageCount" :total="data.length" />
    </div>
</template>

<script setup>
const page = ref(1)
const pageCount = 12

const source = useDataSource()
const data = await useCsvConverter(source.value)
const columns = [
    { key: 'version', label: 'Version' },
    { key: 'base version', label: 'Base version' },
    { key: 'scenario', label: 'Scenario', sortable: true },
    { key: 'solution', label: 'Solution', sortable: true },
    { key: 'timestamp', label: 'Timestamp', sortable: true },
    { key: 'duration', label: 'Duration', sortable: true },
    { key: 'base duration', label: 'Base duration', sortable: true },
    { key: 'relative duration', label: 'Relative duration', sortable: true }
];


const q = ref('')
const rows = computed(() => {
    return data.slice((page.value - 1) * pageCount, (page.value) * pageCount)
})
const filteredRows = computed(() => {
    if (!q.value) {
        return rows
    }

    return rows.filter((entry) => {
        return Object.values(entry).some((value) => {
            return String(value).toLowerCase().includes(q.value.toLowerCase())
        })
    })
})
</script>