import { formattedLogText } from "./serviceFunctions.js";

export const printEach = (testLog) => {
  const formatted_text = formattedLogText(testLog);
  console.log(formatted_text);
};
