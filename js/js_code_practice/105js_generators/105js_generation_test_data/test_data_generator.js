export function* userGenerator(user_prefix = "test_user") {
  let user_id = 1;
  while (true) {
    yield {
      userName: `${user_prefix}_${user_id}`,
      userEmail: `${user_prefix}_${user_id}@email.com`,
    };
    user_id++;
  }
}
