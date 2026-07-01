package com.restapi.test.client;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ClassicHttpResponse;
import org.apache.hc.core5.http.ContentType;
import org.apache.hc.core5.http.io.entity.StringEntity;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.stream.Collectors;

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
            
            return new HttpResponse(statusCode, url, "");
        }
    }

    /**
     * Send a POST request with JSON body and return the response
     *
     * @param url the URL to send the POST request to
     * @param jsonBody the JSON body as a string
     * @return HttpResponse object containing status code and response body
     * @throws Exception if the request fails
     */
    public static HttpResponse sendPostRequest(String url, String jsonBody) throws Exception {
        HttpPost httpPost = new HttpPost(url);
        httpPost.setEntity(new StringEntity(jsonBody, ContentType.APPLICATION_JSON));
        
        try (CloseableHttpClient client = HttpClients.createDefault()) {
            ClassicHttpResponse response = client.executeOpen(null, httpPost, null);
            int statusCode = response.getCode();
            
            String responseBody = "";
            if (response.getEntity() != null) {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()))) {
                    responseBody = reader.lines().collect(Collectors.joining());
                }
            }
            
            return new HttpResponse(statusCode, url, responseBody);
        }
    }

    /**
     * Simple wrapper class for HTTP response
     */
    public static class HttpResponse {
        private final int statusCode;
        private final String url;
        private final String body;

        public HttpResponse(int statusCode, String url, String body) {
            this.statusCode = statusCode;
            this.url = url;
            this.body = body;
        }

        public int getStatusCode() {
            return statusCode;
        }

        public String getUrl() {
            return url;
        }

        public String getBody() {
            return body;
        }

        public JsonObject getJsonBody() {
            return JsonParser.parseString(body).getAsJsonObject();
        }
    }
}
