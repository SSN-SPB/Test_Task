import { test, expect } from "@playwright/test";

type User = {
  id: number;
  name: string;
};

test.describe("Users API", () => {
  test("returns HTTP 200", async ({ request }) => {
    const response = await request.get("/api/users");

    expect(response.status()).toBe(200);
  });

  test("returns the expected users", async ({ request }) => {
    const response = await request.get("/api/users");
    const users = (await response.json()) as User[];

    expect(users).toEqual([
      { id: 1, name: "John" },
      { id: 2, name: "Jane" },
      { id: 3, name: "Robert" },
    ]);
  });
});
