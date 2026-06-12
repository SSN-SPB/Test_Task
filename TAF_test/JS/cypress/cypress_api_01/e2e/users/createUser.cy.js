import UserService from "../../services/UserService";
import User from "../../models/User";

describe("Users API", () => {

  it("should create user", () => {

    cy.fixture("users").then((data) => {

      const user = new User(
        data.validUser.name,
        data.validUser.job
      );

      UserService.createUser(user)
        .then((response) => {

          expect(response.status).to.eq(201);

          expect(response.body).to.have.property("name");
          expect(response.body).to.have.property("job");
          expect(response.body).to.have.property("id");
          expect(response.body).to.have.property("createdAt");

          expect(response.body.name)
            .to.eq(user.name);

          expect(response.body.job)
            .to.eq(user.job);

        });

    });

  });

  it("should get existing user", () => {

    UserService.getUser(2)
      .then((response) => {

        expect(response.status).to.eq(200);

        expect(response.body.data.id)
          .to.eq(2);

        expect(response.body.data.email)
          .to.include("@reqres.in");

      });

  });

});