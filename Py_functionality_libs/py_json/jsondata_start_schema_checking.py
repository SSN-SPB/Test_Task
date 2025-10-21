
import requests
import json
from jsonschema import validate, ValidationError
import sys


xcal_reports_kpi_schema = {
    "type": "object",
    "properties": {
        "mts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},  # mismatch: response has int
                    "name": {"type": "string"},
                    "mobile": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {"index": {"type": "integer"}},
                            "required": ["index"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["index", "name", "mobile"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["mts"],
    "additionalProperties": False,
}
geo_schema={
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/usgs-earthquake-feed.schema.json",
  "title": "USGS Earthquake GeoJSON Feed",
  "type": "object",
  "required": ["type", "metadata", "features", "bbox"],
  "properties": {
    "type": {
      "type": "string",
      "const": "FeatureCollection"
    },
    "metadata": {
      "type": "object",
      "required": ["generated", "url", "title", "status", "api", "count"],
      "properties": {
        "generated": { "type": "integer" },
        "url": { "type": "string", "format": "uri" },
        "title": { "type": "string" },
        "status": { "type": "integer" },
        "api": { "type": "string" },
        "count": { "type": "integer" }
      },
      "additionalProperties": True
    },
    "features": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "properties", "geometry", "id"],
        "properties": {
          "type": {
            "type": "string",
            "const": "Feature"
          },
          "properties": {
            "type": "object",
            "required": ["mag", "place", "time", "updated", "status", "type", "title"],
            "properties": {
              "mag": { "type": ["number", "null"] },
              "place": { "type": ["string", "null"] },
              "time": { "type": ["integer", "null"] },
              "updated": { "type": ["integer", "null"] },
              "tz": { "type": ["integer", "null"] },
              "url": { "type": ["string", "null"], "format": "uri" },
              "detail": { "type": ["string", "null"], "format": "uri" },
              "felt": { "type": ["integer", "null"] },
              "cdi": { "type": ["number", "null"] },
              "mmi": { "type": ["number", "null"] },
              "alert": { "type": ["string", "null"] },
              "status": { "type": "string" },
              "tsunami": { "type": ["integer", "null"] },
              "sig": { "type": ["integer", "null"] },
              "net": { "type": ["string", "null"] },
              "code": { "type": ["string", "null"] },
              "ids": { "type": ["string", "null"] },
              "sources": { "type": ["string", "null"] },
              "types": { "type": ["string", "null"] },
              "nst": { "type": ["integer", "null"] },
              "dmin": { "type": ["number", "null"] },
              "rms": { "type": ["number", "null"] },
              "gap": { "type": ["number", "null"] },
              "magType": { "type": ["string", "null"] },
              "type": { "type": "string" },
              "title": { "type": "string" }
            },
            "additionalProperties": True
          },
          "geometry": {
            "type": "object",
            "required": ["type", "coordinates"],
            "properties": {
              "type": { "type": "string", "const": "Point" },
              "coordinates": {
                "type": "array",
                "items": { "type": "number" },
                "minItems": 2,
                "maxItems": 3
              }
            }
          },
          "id": { "type": "string" }
        },
        "additionalProperties": False
      }
    },
    "bbox": {
      "type": "array",
      "items": { "type": "number" },
      "minItems": 6,
      "maxItems": 6
    }
  },
  "additionalProperties": False
}

geo_schema_simple = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Simplified USGS Feed Snippet",
  "type": "object",
  "required": ["type", "metadata"],
  "properties": {
    "type": {
      "type": "string",
      "const": "FeatureCollection"
    },
    "metadata": {
      "type": "object",
      "required": ["generated", "url", "title", "status", "api", "count"],
      "properties": {
        "generated": {
          "type": "integer",
          "pattern": "^[0-9]{13}$"
        },
        "url": {
          "type": "string",
          "pattern": "^https://earthquake\\.usgs\\.gov/.*"
        },
        "title": { "type": "string" },
        "status": { "type": "integer", "const": 200 },
        "api": { "type": "string", "const": "1.14.1" },
        "count": { "type": "integer" }
      },
      "additionalProperties": True
    }
  },
  "additionalProperties": True
}

def main():
    sys._debugmallocstats()
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    # webUrl = urllib.request.urlopen(urlData)
    # print("result code: " + str(webUrl.getcode()))
    # print("result code: " + webUrl.)
    get_request = requests.get(urlData,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    print(requested_data)
    print(type(requested_data))
    print(get_request.status_code)
    print(get_request.json())
    print(type(get_request.json()))
    try:
        validate(instance=requested_data, schema=geo_schema)
        print("Response matches schema")
        assert True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        assert False
    assert get_request.status_code == 200

    try:
        validate(instance=requested_data, schema=geo_schema_simple)
        print("Response matches schema")
        assert True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        assert False
    assert get_request.status_code == 200

if __name__ == "__main__":
    main()
