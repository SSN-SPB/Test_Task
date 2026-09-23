export function* scenarioGenerator({
  typeOfScenario = "basic",
  name = "default_name",
  dayTime = "morning",
} = {}) {
  let idNumber = 1;

  while (true) {
    yield {
      type: `${typeOfScenario}_${dayTime}_${idNumber}`,
      name: `${name}_${dayTime}_${idNumber}`,
    };
    idNumber++;
  }
}
