import { Logger } from "../support/logger";

export default class BaseService {

  request(method, endpoint, body = null) {

    Logger.request(method, endpoint, body);

    return cy.request({
      method,
      url: endpoint,
      body,
      failOnStatusCode: false
    })
    .then((response) => {

      Logger.response(response);

      return response;
    });
  }

}