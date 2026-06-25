package com.restapi.test.client;

import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ClassicHttpResponse;

/**
 * Utility class for making HTTP requests
 */
public class HttpClientUtil {

    /**
     * Send a GET request and return the response
     *
     * @param url the URL to send the GET request to
     * @return HttpResponse object containing status code and response body
     * @throws Exception if the request fails
     */
    public static HttpResponse sendGetRequest(String url) throws Exception {
        HttpGet httpGet = new HttpGet(url);
        
        try (CloseableHttpClient client = HttpClients.createDefault()) {
            ClassicHttpResponse response = client.executeOpen(null, httpGet, null);
            int statusCode = response.getCode();
            
            return new HttpResponse(statusCode, url);
        }
    }

    /**
     * Simple wrapper class for HTTP response
     */
    public static class HttpResponse {
        private final int statusCode;
        private final String url;

        public HttpResponse(int statusCode, String url) {
            this.statusCode = statusCode;
            this.url = url;
        }

        public int getStatusCode() {
            return statusCode;
        }

        public String getUrl() {
            return url;
        }
    }
}
