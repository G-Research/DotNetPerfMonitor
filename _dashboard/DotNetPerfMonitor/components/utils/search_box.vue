<template>
    <div class="justify-end float-right w-2/4">
        <UInput icon="i-heroicons-magnifying-glass-20-solid" size="sm" color="white" :trailing="false" placeholder="Search"
            :ui="preset">
            <template #trailing>
                <div class="flex items-center gap-0.5">
                    <UKbd>{{ metaSymbol }}</UKbd>
                    <UKbd>K</UKbd>
                </div>
            </template>
        </UInput>
    </div>
</template>


<script setup>
const { metaSymbol } = useShortcuts()

const preset = {
    'size': 'text-xl',
    'font': 'font-bold',
    'icon': {
        'size': 'text-md',
        'color': 'text-red-200 dark:text-gray-300',
    },

}
</script>