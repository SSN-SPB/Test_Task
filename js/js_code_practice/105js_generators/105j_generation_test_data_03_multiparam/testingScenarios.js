import { scenarioGenerator } from "./test_data_generator_multi.js";

const basicGenerator = scenarioGenerator();
console.log(basicGenerator.next().value);
console.log(basicGenerator.next().value);
console.log(basicGenerator.next().value);
const basicGeneratorLateEvening = scenarioGenerator({ dayTime: "lateEvening" });
console.log(basicGeneratorLateEvening.next().value);
console.log(basicGeneratorLateEvening.next().value);
console.log(basicGeneratorLateEvening.next().value);
const basicGeneratorLateEveningCulture = scenarioGenerator({ dayTime: "Evening", typeOfScenario: "NewsOfCulture" });
console.log(basicGeneratorLateEveningCulture.next().value);
console.log(basicGeneratorLateEveningCulture.next().value);
console.log(basicGeneratorLateEveningCulture.next().value);
