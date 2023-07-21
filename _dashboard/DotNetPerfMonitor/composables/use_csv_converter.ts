import * as csvToJson from "convert-csv-to-json";
import csvParser from "csv-parser";
export default async function useCsvConverter(csvPath: string) {
  //   const output = "/static/json/";
  //   const jsonData = await csvToJson.generateJsonFileFromCsv(csvPath, output);
  //   console.log(jsonData);
  //   return jsonData;
  const jsonData = [];
  const response = await fetch(csvPath);
  const csvText = await response.text();
  console.log(csvText);
  return csvText;

  // Parse the CSV string into a JSON array using csv-parser
  //   csvParser()
  //     .on("data", (data) => {
  //       jsonData.push(data);
  //     })
  //     .on("end", () => {
  //       console.log("CSV parsed into JSON:", jsonData);
  //     })
  //     .write(csvText);
}
