import { log } from "console";
import * as Papa from "papaparse";
export default async function useCsvConverter(csvPath: string) {
  const response: any = await fetch(csvPath);
  const csvText: any = await response.text();

  const parsed = Papa.parse(csvText, {
    dynamicTyping: true,
    //preview: 4500,
    skipEmptyLines: true,
    fastMode: true,
    header: true,
  });

  return parsed.data;
}
