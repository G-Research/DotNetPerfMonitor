export default function useDataExtracter(
  data: Array<{ field: String; [key: string]: any }>
) {
  useLogger(data.map((item) => item.timestamp));
  return data.map((item) => item.timestamp);
}
