export default function useColumnsetExtractor(
  data: Array<any>,
  column: string
) {
  return [...new Set(data.map(d => d[column]))];
}
