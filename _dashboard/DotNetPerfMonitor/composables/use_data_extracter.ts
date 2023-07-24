export default function useDataExtracter(
  data: Array<{ field: String; [key: string]: any }>
) {
  return data.map((item) => item.timestamp);
}
