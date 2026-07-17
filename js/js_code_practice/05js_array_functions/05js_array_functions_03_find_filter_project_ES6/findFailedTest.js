export const findFailedTest = (test) => {
  return test.status === "Failed";
};
