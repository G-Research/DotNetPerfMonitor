// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  colorMode: {
    preference: "dark",
  },
  modules: ["@nuxthq/ui"],

  css: ["@/assets/css/global.css"],
  
  experimental: {
	payloadExtraction: "false",
  },
  target: 'static',
  router: {
    base: '/DotNetPerfMonitor/'
  }
});
