import { test, expect } from "@playwright/test";

type HealthResponse = {
  status: string;
  service: string;
};

test.describe("Health API", () => {
  test("returns HTTP 200", async ({ request }) => {
    const response = await request.get("/api/health");

    expect(response.status()).toBe(200);
  });

  test("returns an OK status", async ({ request }) => {
    const response = await request.get("/api/health");
    const body = (await response.json()) as HealthResponse;

    expect(body.status).toBe("ok");
  });

  test("returns the Flask training service name", async ({ request }) => {
    const response = await request.get("/api/health");
    const body = (await response.json()) as HealthResponse;

    expect(body.service).toBe("flask-training");
  });
});
