<template>
    <div class="flex flex-col px-4 py-4">
        <UtilsSearchBox />
        <DashboardCronjobsTracer class="py-8" />
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
            <el-tab-pane label="F#" name="first">F#</el-tab-pane>
            <el-tab-pane label="C#" name="third">C# Compiler</el-tab-pane>
            <el-tab-pane label=".NET" name="fourth">.NET</el-tab-pane>
        </el-tabs>


    </div>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
import type { TabsPaneContext } from 'element-plus'

const activeName = ref('first')
const handleClick = (tab: TabsPaneContext, event: Event) => {
    console.log(tab, event)
}
</script>