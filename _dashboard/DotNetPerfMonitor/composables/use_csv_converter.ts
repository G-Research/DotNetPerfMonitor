
import * as Papa from "papaparse";
export default async function useCsvConverter(csvPath: string) {
  
  console.log(`Fetching: ${csvPath}`);
  const response: any = await fetch(csvPath);
  const csvText: any = await response.text();


  const parsed = Papa.parse(csvText, {
    dynamicTyping: true,
    //preview: 4500,
    skipEmptyLines: true,
    fastMode: true,
    header: true,
  });
  const str = JSON.stringify(parsed.data);
  const json = JSON.parse(str);

  return json;
}
