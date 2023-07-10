<template>
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
        <p class="text-md py-1 text-md">Theme mode</p>
        <UtilsThemeSwitcher />
      </div>
      <div class="flex items-center justify-center h-screen">
      </div>

    </div>
  </div>
  <div class="footer">
    <!-- Footer content -->

    <p class="text-center text-2xl">Dashboard Footer</p>


  </div>
</template>


<style>
.sidebar,
.right-sidebar {
  width: 15%;
  height: 80vh;
}

.main-section {
  width: 70%;
  height: 80vh;
}

.header,
.footer {
  height: 10vh;
}
</style>