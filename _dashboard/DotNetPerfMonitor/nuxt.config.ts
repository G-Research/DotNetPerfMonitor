// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxtjs/google-fonts", "@nuxthq/ui"],
  googleFonts: {
    families: {
      Releway: true,
    },
    display: "swap",
  },
  css: ["@/assets/css/global.css"],
});
