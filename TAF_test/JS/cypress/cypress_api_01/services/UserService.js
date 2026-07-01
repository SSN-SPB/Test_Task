 import BaseService from "./BaseService";

class UserService extends BaseService {

  createUser(user) {
    return this.request(
      "POST",
      "/users",
      user
    );
  }

  getUser(id) {
    return this.request(
      "GET",
      `/users/${id}`
    );
  }

}

export default new UserService();