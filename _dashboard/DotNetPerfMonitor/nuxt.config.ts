// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/google-fonts",
    "@nuxthq/ui",
    "@element-plus/nuxt",
  ],
  googleFonts: {
    families: {
      Releway: true,
    },
    display: "swap",
  },
  css: ["@/assets/css/global.css"],
});