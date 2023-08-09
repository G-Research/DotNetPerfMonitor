// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,
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
  // vite: {
  //   optimizeDeps: {
  //     include: ["plotly.js-dist-min"],
  //   },
  // },
  experimental: {
    payloadExtraction: true,
  },
});
