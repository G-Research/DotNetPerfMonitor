<template>
  <div class="flex h-screen">
    <div class="sidebar bg-gray-100">
      <!-- Sidebar content -->
      <DashboardLeftSidebar />
    </div>
    <div class="main-section bg-blue-500">
      <!-- Main section content -->
      <NuxtPage />
    </div>
    <div class="right-sidebar bg-green-500">
      <!-- Right sidebar content -->
      <div class="flex items-center justify-center h-screen">
        <p class="text-2xl">Utils Section</p>
      </div>

    </div>
  </div>
  <div class="footer bg-yellow-500">
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