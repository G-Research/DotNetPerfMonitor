import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component("TabGroup", TabGroup);
  nuxtApp.vueApp.component("TabList", TabList);
  nuxtApp.vueApp.component("Tab", Tab);
  nuxtApp.vueApp.component("TabPanels", TabPanels);
  nuxtApp.vueApp.component("TabPanel", TabPanel);
});
