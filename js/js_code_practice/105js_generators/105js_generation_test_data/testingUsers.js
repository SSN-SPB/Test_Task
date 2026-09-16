import { userGenerator } from "./test_data_generator.js";

const generatorOfUsers = userGenerator();
console.log(generatorOfUsers.next().value);
console.log(generatorOfUsers.next().value);
console.log(generatorOfUsers.next().value);
const generatorOfAdminUsers = userGenerator("admin_user");
console.log(generatorOfAdminUsers.next().value);
console.log(generatorOfAdminUsers.next().value);
console.log(generatorOfAdminUsers.next().value);
