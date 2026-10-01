import { setWorldConstructor } from "@cucumber/cucumber";

export class CustomWorld {
  constructor() {
    this.browser = undefined;
    this.context = undefined;
    this.page = undefined;
    this.loginPage = undefined;
  }
}

setWorldConstructor(CustomWorld);
