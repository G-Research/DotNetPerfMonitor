<template>
    <div :class="display">
        <UCard class="cursor-pointer">
            <div class="flex flex-row items-center gap-3">
                <UAvatar :src="regression.userAvatar" alt="github-icon self-center" class="bg-red-200" size="lg" />
                <div class="flex flex-col gap-2">
                    <div class="flex flex-row gap-2">
                        <h1 class="text-sky-400 text-xl sm:text-lg">{{ regression.title }}</h1>
                        <UBadge class="bg-sky-500 text-white">#{{ regression.number }}</UBadge>
                    </div>
                    <p class="text-gray-800 dark:text-white">Since {{ regression.date }} </p>

                    <div class="flex flex-row gap-2">
                        <RegressionIssueBadge v-for="label in regression.labels" :name="label.name" :id="label.id"
                            :color="label.color" />
                    </div>
                </div>
            </div>

        </UCard>
        <div class="py-2"></div>
    </div>
</template>

<script setup>

const regression = defineProps({
    url: String,
    number: Number,
    title: String,
    date: String,
    status: String,
    user: String,
    userAvatar: String,
    status: String,
    locked: Boolean,
    labels: Array,

})

const display = regression.user === 'github-actions[bot]' ? 'block' : 'hidden';
const mode = useColorMode()
const src = ref('')
watch(mode, (theme) => {
    src.value = theme.preference === 'dark' ? '/images/logo.png' : 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg'
})

</script>