<template>
    <div class="flex flex-col px-4 py-4">
        <UtilsSearchBox class="self-center" />
        <div class="py-2">

            <h1 class="text-sky-500 font-bold xl:text-3xl sm:text-2xl xs:text-xs text-lg">Active Performance Regressions
            </h1>
        </div>
        <div class="py-4"></div>


        <div v-if="pending" v-for="x in 10" :key="x">
            <DashboardCardSkeleton class="py-2" />
        </div>
        <div v-else>

            <RegressionTile v-for="issue in issues" :key="issue.id" :title="issue.title" :number="issue.number"
                :user="issue.user.login" :labels="issue.labels" :userAvatar="issue.user.avatar_url"
                :date=useDateformat(issue.created_at) :locked="issue.locked" />

        </div>

    </div>
</template>

<script setup>
const { data: issues, pending, error } = await useLazyAsyncData('active_regressions', async () => {
    return $fetch('https://api.github.com/repos/G-Research/DotNetPerfMonitor/issues', {
        transform: async (response) => {
            const data = await response.json()
            console.log(data)
            const filtered = data.filter((issue) => {
                return issue.user.type === "Bot"
            })
            console.log(filtered)
            return filtered
        }
    })
})

</script>