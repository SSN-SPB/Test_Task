package com.restapi.test;

import com.restapi.test.client.HttpClientUtil;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Test class for validating REST GET requests return HTTP 200 status code
 */
@DisplayName("REST GET Status Code Tests")
public class RestGetStatusCodeTest {

    private static final int EXPECTED_STATUS_CODE = 200;

    @Test
    @DisplayName("Google homepage should return 200 status code")
    public void testGoogleStatusCode() throws Exception {
        // Arrange
        String url = "https://www.google.com";

        // Act
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendGetRequest(url);

        // Assert
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                "Google homepage should return HTTP 200 status code");
    }

    @Test
    @DisplayName("Python.org homepage should return 200 status code")
    public void testPythonOrgStatusCode() throws Exception {
        // Arrange
        String url = "https://www.python.org";

        // Act
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendGetRequest(url);

        // Assert
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                "Python.org homepage should return HTTP 200 status code");
    }

    @ParameterizedTest
    @ValueSource(strings = {"https://www.google.com", "https://www.python.org"})
    @DisplayName("All websites should return 200 status code")
    public void testMultipleWebsitesStatusCode(String url) throws Exception {
        // Act
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendGetRequest(url);

        // Assert
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                url + " should return HTTP 200 status code");
    }


    @Test
    @DisplayName("The https://www.schultetable.com/ website should return 200 status code")
    public void testNewWebsiteStatusCode() throws Exception {
        String url = "https://www.schultetable.com";
        HttpClientUtil.HttpResponse response = HttpClientUtil.sendGetRequest(url);
        assertEquals(EXPECTED_STATUS_CODE, response.getStatusCode(),
                "New website should return HTTP 200 status code");
    }
}
