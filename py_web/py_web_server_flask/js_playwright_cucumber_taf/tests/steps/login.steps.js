import { Given, When, Then } from "@cucumber/cucumber";
import { expect } from "@playwright/test";
import { LoginPage } from "../pages/LoginPage.js";

Given("I am on the login page", async function () {
  this.loginPage = new LoginPage(this.page);

  await this.loginPage.open();
});

When(
  "I log in with username {string} and password {string}",
  async function (username, password) {
    await this.loginPage.login(username, password);
  },
);

Then("I should see the data page", async function () {
  await expect(this.page).toHaveURL(/\/data$/);
});
