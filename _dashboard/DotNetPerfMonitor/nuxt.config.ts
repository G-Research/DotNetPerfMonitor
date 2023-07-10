// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  app: {
    baseURL: "/DotNetPerfMonitor/_dashboard/DotNetPerfMonitor/",
  },
  modules: ["@nuxtjs/google-fonts", "@nuxthq/ui", "@element-plus/nuxt"],
  googleFonts: {
    families: {
      Releway: true,
    },
  },
  css: ["@/assets/css/global.css"],
});
