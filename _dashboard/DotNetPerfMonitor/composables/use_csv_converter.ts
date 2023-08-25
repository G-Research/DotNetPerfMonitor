
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

  parsed.data.forEach(row => {
    row["timestamp"] = new Date(row["timestamp"]);
    row["relative duration"] = Number(row["relative duration"]).toFixed(2); 
    row["duration"] = Number(row["duration"]).toFixed(2);
    row["base duration"] = Number(row["base duration"]).toFixed(2);
});

  return parsed.data;
}
