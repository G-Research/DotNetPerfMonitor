// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  target: "static",
  app: {
    baseURL: "/DotNetPerfMonitor/",
  },

  generate: {
    routes: ["/notifications", "/settings", "/documentation", "/regressions"],
  },

  colorMode: {
    preference: "dark",
  },
  modules: ["@nuxthq/ui"],

  css: ["@/assets/css/global.css"],

  experimental: {
    payloadExtraction: false,
  },
});
