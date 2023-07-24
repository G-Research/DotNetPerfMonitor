<template>
  <NuxtLayout>
    <div class="flex h-screen">
      <div class="sidebar">
        <!-- Sidebar content -->
        <DashboardLeftSidebar />
      </div>
      <div class="main-section">
        <!-- Main section content -->
        <NuxtPage />
      </div>
      <div class="right-sidebar">
        <!-- Right sidebar content -->
        <div class="px-8 py-4 flex flex-row">
          <UtilsThemeSwitcher />
        </div>
        <div class="flex items-center justify-center h-screen">
        </div>

      </div>
    </div>

  </NuxtLayout>
</template>


<style>
.sidebar,
.right-sidebar {
  width: 15%;
  height: 100vh;
}

.main-section {
  width: 70%;
  height: 100vh;
}

.header {
  height: 10vh;
}
</style>