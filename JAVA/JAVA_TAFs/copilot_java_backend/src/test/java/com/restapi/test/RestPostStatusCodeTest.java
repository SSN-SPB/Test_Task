package com.restapi.test;

import com.google.gson.JsonObject;
import com.restapi.test.client.HttpClientUtil;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for validating REST POST requests return HTTP 200 status code
 * and response contains expected data
 */
@DisplayName("REST POST Status Code Tests")
public class RestPostStatusCodeTest {

    private static final int EXPECTED_STATUS_CODE = 200;

    @Test
    @DisplayName("POST request to postman-echo should return 200 and contain correct data")
    public void testPostmanEchoPostRequest() throws Exception {
        // Arrange
        String url = "https://postman-echo.com/post";
        String jsonBody = "{\"name\": \"John\", \"age\": 30, \"city\": \"London\"}";

        // Act
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendPostRequest(url, jsonBody);

        // Assert - Status Code
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                "POST request to postman-echo should return HTTP 200 status code");

        // Assert - Response body contains data
        assertNotNull(response.getBody(), "Response body should not be null");
        assertFalse(response.getBody().isEmpty(), "Response body should not be empty");

        // Parse the response JSON
        JsonObject responseJson = response.getJsonBody();
        assertNotNull(responseJson, "Response JSON should be parseable");

        // Verify the data object contains the correct values
        assertTrue(responseJson.has("data"), "Response should contain 'data' field");
        JsonObject dataObject = responseJson.getAsJsonObject("data");

        assertEquals("John", dataObject.get("name").getAsString(),
                "Response data should contain name 'John'");
        assertEquals(30, dataObject.get("age").getAsInt(),
                "Response data should contain age '30'");
        assertEquals("London", dataObject.get("city").getAsString(),
                "Response data should contain city 'London'");
    }

    @Test
    @DisplayName("POST request with different data should echo back correctly")
    public void testPostmanEchoPostRequestWithDifferentData() throws Exception {
        // Arrange
        String url = "https://postman-echo.com/post";
        String jsonBody = "{\"name\": \"Alice\", \"age\": 25, \"city\": \"Paris\"}";

        // Act
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendPostRequest(url, jsonBody);

        // Assert - Status Code
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                "POST request should return HTTP 200");

        // Parse and verify the response
        JsonObject responseJson = response.getJsonBody();
        JsonObject dataObject = responseJson.getAsJsonObject("data");

        assertEquals("Alice", dataObject.get("name").getAsString(),
                "Response data should contain name 'Alice'");
        assertEquals(25, dataObject.get("age").getAsInt(),
                "Response data should contain age '25'");
        assertEquals("Paris", dataObject.get("city").getAsString(),
                "Response data should contain city 'Paris'");
    }
}
