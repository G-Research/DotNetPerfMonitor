import { log } from "console";
import * as Papa from "papaparse";
export default async function useCsvConverter(csvPath: string) {
  const response = await fetch(csvPath);
  const csvText = await response.text();

  //console.log(`csvText: ${csvText}`);

  const parsed = Papa.parse(csvText, {
    dynamicTyping: true,
    //preview: 365 * 6,
    header: true,
  });
  const str = JSON.stringify(parsed.data);
  const json = JSON.parse(str);
  //console.log(`json: ${str}`);
  return json;
}
