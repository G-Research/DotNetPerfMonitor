export default async function useDataConfig() {
  const data: any = await $fetch("/app_config.json");
  return data;
}
