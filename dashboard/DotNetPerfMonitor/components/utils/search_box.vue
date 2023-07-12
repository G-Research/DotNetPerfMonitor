<template>
    <div class="justify-end float-right">
        <UInput icon="i-heroicons-magnifying-glass-20-solid" size="sm" color="white" :trailing="false" placeholder="Search">
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
</script>