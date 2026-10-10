export const isCode200 = (response) => response.status === 200;
export const isCode201 = (response) => response.status === 201;
export const allResponsesLess300 = (response) => response.status < 300;
export const endpointContactHasStatus200 = (response) => response.some( (response) => response.endpoint === "/contracts" && response.status === 200);
