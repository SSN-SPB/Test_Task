
import requests
import json
from jsonschema import validate, ValidationError
import sys

# tr3 =

# noinspection LanguageDetectionInspection
tr2 = {
    "mts": [
        {
            "index": 1,
            "name": "XCAL",
            "mobile": [
                {
                    "index": 1,
                    "L3MSG": [
                        "QC5GNR_RRCMSG|2025-10-29 14:51:29.006877|5GNR rrcReconfiguration - 5GNR Security protected NAS Message / 5GNR Security protected NAS Message|2025-10-29 14:48:13.186781|16|144|DL DCCH|1|110|654048|478248|00 88 A0 4D 02 50 08 82 F1 D8 4D A0 4A 00 D4 00 0B 3E 03 1C 55 FC 81 20 E4 4E 80 00 40 56 BF 01 43 F0 05 42 61 E4 13 D8 87 7B 5F 2A F0 58 BC 18 71 ED 69 72 41 A9 54 02 B7 C7 D5 46 47 02 1E 37 04 7F 7B FC 5C 83 27 92 AF C0 21 8A 00 13 0A A8 64 41 D0 E2 19 E5 FC 4F 9C CE 76 67 18 90 C8 F8 F4 07 E4 51 71 29 AB 03 1C 12 61 F7 94 10 B0 C1 29 72 02 51 8D FC F4 26 F4 67 61 2C AB BE 75 A2 4A 95 EA EB 85 46 23 E8 14 8A 25 22 54 5C 1B E9 E1 78 9A C4 99 99 81 7C A3 5E 67 A4 2F 76 72 F1 3A EA 47 D1 F9 E3 76 67 31 4E 7C B8 90 E9 B7 F5 12 C3 82 AB 1D B8 56 D6 80 AC A8 93 FD A5 9C 44 70 85 A5 48 52 C7 F5 3D B0 C7 D2 80",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:29.087776|5GNR rrcReconfigurationComplete|2025-10-29 14:48:13.190149|16|144|UL DCCH|1|110|654048|478720|08 00",
                        "QC5GNR_NASMSG|2025-10-29 14:51:29.087798|5GNR DL NAS transport|2025-10-29 14:48:13.190880|15|4|0|DL|7E 00 68 01 00 9E 2E 04 55 C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 60 45 CD C8 18 BD 8F 59 0A A3 45 FB 22 04 01 00 00 07 75 00 0F 80 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 80 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70 12 04",
                        "QC5GNR_NASMSG|2025-10-29 14:51:29.087808|5GNR PDU session establishment accept|2025-10-29 14:48:13.190976|15|4|0|DL|2E 04 55 C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 60 45 CD C8 18 BD 8F 59 0A A3 45 FB 22 04 01 00 00 07 75 00 0F 80 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 80 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70"
                    ]
                },
                {
                    "index": 2,
                    "L3MSG": "null"
                },
                {
                    "index": 3,
                    "L3MSG": [
                        "QC5GNR_RRCMSG|2025-10-29 14:51:29.975193|5GNR rrcReconfiguration - 5GNR Security protected NAS Message / 5GNR Security protected NAS Message|2025-10-29 14:48:14.161480|16|144|DL DCCH|1|110|654048|12062281|00 88 A0 4D 01 50 08 1A F1 D8 4D A0 4A 00 D4 00 0B 44 63 1C 55 FC 81 20 E4 4E 80 00 40 56 BF 01 63 AE 84 F0 36 9A DC 6D 0E 28 1B F4 91 C3 55 D8 6E 6E 78 5E D4 9E BC 9B 99 F3 9B 9D 55 AF D3 9B 22 FB 12 EF 5E 29 1E C4 AA AF A0 18 0B EA 51 92 BA 12 BA D6 FA D9 57 2C DD 1B 03 E4 8E 3D 00 94 2D F6 AA 64 4E F6 53 11 C3 37 32 FD EC B7 E8 C4 41 83 48 49 08 8E 01 93 1D 3A ED 6B DB BB 30 44 B3 67 BA A9 C0 44 14 01 D8 23 A9 C5 7F 76 30 E4 A0 F2 81 62 5C 42 BA A3 2F C3 B8 3D C7 27 E1 50 8A E8 7F 9F 68 7A 6D 56 6C CA 8B E9 23 05 C0 D6 19 8E 9E 40 C6 B9 DE 84 C9 3C 96 EE AF 76 76 0C 4C 2C 44 17 5E AE 02 05 CB 9C FD 80",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.028046|5GNR rrcReconfigurationComplete|2025-10-29 14:48:14.164695|16|144|UL DCCH|1|110|654048|4129|08 00",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.028080|5GNR DL NAS transport|2025-10-29 14:48:14.165426|15|4|0|DL|7E 00 68 01 00 9E 2E 02 9C C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 61 72 AA D6 EE 14 AA C1 0A A3 45 FD 22 04 01 00 00 07 75 00 0F 60 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 60 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70 12 02",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.028090|5GNR PDU session establishment accept|2025-10-29 14:48:14.165525|15|4|0|DL|2E 02 9C C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 61 72 AA D6 EE 14 AA C1 0A A3 45 FD 22 04 01 00 00 07 75 00 0F 60 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 60 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.600475|5GNR PDU session release request|2025-10-29 14:48:14.740689|15|4|0|UL|2E 02 9D D1 59 24",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.600487|5GNR UL NAS transport|2025-10-29 14:48:14.740885|15|4|0|UL|7E 00 67 01 00 06 2E 02 9D D1 59 24 12 02",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.600758|5GNR ulInformationTransfer|2025-10-29 14:48:14.741279|16|144|UL DCCH|2|110|654048|33801|3A 0A BF 01 30 B8 92 B3 30 97 47 71 BD 75 6D FA E1 69 E8 57 93 BD 42 80",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.679032|5GNR dlInformationTransfer - 5GNR Security protected NAS Message / 5GNR Security protected NAS Message|2025-10-29 14:48:14.854927|16|144|DL DCCH|2|110|654048|39448|28 82 8F C0 46 2E 9F 33 ED D9 CF 07 24 A8 0A 30 3E 4D 5D 59 F9 0B 00",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.679044|5GNR DL NAS transport|2025-10-29 14:48:14.855780|15|4|0|DL|7E 00 68 01 00 05 2E 02 9D D3 24 12 02",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.679050|5GNR PDU session release command|2025-10-29 14:48:14.855881|15|4|0|DL|2E 02 9D D3 24",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.679357|5GNR rrcReconfiguration|2025-10-29 14:48:14.864813|16|144|DL DCCH|1|110|654048|39960|00 88 40 1C 00 19 00 04 00",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.738921|5GNR PDU session release complete|2025-10-29 14:48:14.867371|15|4|0|UL|2E 02 9D D4",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.738943|5GNR UL NAS transport|2025-10-29 14:48:14.867485|15|4|0|UL|7E 00 67 01 00 04 2E 02 9D D4 12 02",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.738961|5GNR rrcReconfigurationComplete|2025-10-29 14:48:14.867771|16|144|UL DCCH|1|110|654048|13147193|08 00",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.738972|5GNR ulInformationTransfer|2025-10-29 14:48:14.868763|16|144|UL DCCH|2|110|654048|13147201|3A 09 BF 01 64 23 30 B6 31 4B 48 4C 49 02 23 3C 0E B0 82 02 98 80"
                    ]
                },
                {
                    "index": 4,
                    "L3MSG": [
                        "QC5GNR_RRCMSG|2025-10-29 14:51:29.979942|5GNR rrcReconfiguration - 5GNR Security protected NAS Message / 5GNR Security protected NAS Message|2025-10-29 14:48:14.121416|16|144|DL DCCH|1|110|654048|11011657|00 88 A0 4D 01 D0 08 B2 F1 D8 4D A0 4A 00 D4 00 0B 2E C3 1C 55 FC 81 20 E4 4E 80 00 40 56 BF 01 7D 55 87 E8 37 A8 D3 01 73 10 78 14 97 B8 0D 46 B5 E3 DE CF 09 87 22 E3 90 12 F5 CA F2 9C 4D B1 CB A9 81 2F EE 2C CE 71 13 45 F8 AF 57 B1 DF EC 2F 8B 08 2E 19 A5 87 30 2C 3A 06 43 B1 95 B3 53 A3 DB F7 05 35 2B 51 B1 65 69 C7 34 E1 28 58 9A 71 76 55 92 66 E9 0B 90 9F E3 C9 0C 7B 49 6C C0 B7 37 58 83 ED AD AB B6 6A 24 36 7D 80 6A B4 88 EE 5C 1D C9 F2 90 20 09 0D F7 21 98 C1 81 C3 48 A7 AC A9 23 A8 9C BE 50 75 E3 92 EE D5 AF E9 F2 E0 BC 01 82 58 B8 D0 9E 95 CD 5E 05 43 46 E7 90 5A BB D0 99 FC 80 CA 48 8C F6 48 00",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:29.980741|5GNR rrcReconfigurationComplete|2025-10-29 14:48:14.124750|16|144|UL DCCH|1|110|654048|7866408|08 00",
                        "QC5GNR_NASMSG|2025-10-29 14:51:29.980792|5GNR DL NAS transport|2025-10-29 14:48:14.125488|15|4|0|DL|7E 00 68 01 00 9E 2E 03 84 C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 46 5C 5F CD 66 24 87 D6 0A A3 45 FC 22 04 01 00 00 07 75 00 0F 70 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 70 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70 12 03",
                        "QC5GNR_NASMSG|2025-10-29 14:51:29.980818|5GNR PDU session establishment accept|2025-10-29 14:48:14.125599|15|4|0|DL|2E 03 84 C2 13 00 09 08 00 06 31 20 01 01 FF 08 06 0B 00 05 0B 00 05 29 0D 03 46 5C 5F CD 66 24 87 D6 0A A3 45 FC 22 04 01 00 00 07 75 00 0F 70 00 0C 52 01 01 08 04 06 FE FE BE BE 13 13 79 00 09 08 20 42 01 01 08 07 01 70 7B 00 48 80 00 0D 04 0A A1 FA 0A 00 0D 04 0A AB FA 0A 00 03 10 26 00 08 0D 00 02 00 00 00 10 01 61 02 50 00 10 00 03 10 26 00 08 0D 00 02 F2 00 00 10 01 71 02 50 00 10 00 10 02 05 94 FF 00 04 13 01 84 00 FF 03 04 13 01 84 00 25 07 06 76 7A 77 61 70 70",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.480350|5GNR PDU session release request|2025-10-29 14:48:14.602702|15|4|0|UL|2E 03 85 D1 59 24",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.480377|5GNR UL NAS transport|2025-10-29 14:48:14.602896|15|4|0|UL|7E 00 67 01 00 06 2E 03 85 D1 59 24 12 03",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.480425|5GNR ulInformationTransfer|2025-10-29 14:48:14.603276|16|144|UL DCCH|2|110|654048|26649|3A 0A BF 01 3F D6 F5 E4 2E 83 94 F4 69 C1 D1 5B AD 4D 81 33 BF C9 02 80",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.578606|5GNR dlInformationTransfer - 5GNR Security protected NAS Message / 5GNR Security protected NAS Message|2025-10-29 14:48:14.748337|16|144|DL DCCH|2|110|654048|12092465|28 82 8F C0 5B C7 BC 3A 8E 04 12 06 74 9F 2D EE AE 63 3B 9C CA 13 A0",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.578652|5GNR DL NAS transport|2025-10-29 14:48:14.749224|15|4|0|DL|7E 00 68 01 00 05 2E 03 85 D3 24 12 03",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.578677|5GNR PDU session release command|2025-10-29 14:48:14.749338|15|4|0|DL|2E 03 85 D3 24",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.578979|5GNR rrcReconfiguration|2025-10-29 14:48:14.759863|16|144|DL DCCH|1|110|654048|9471552|00 88 40 B4 00 19 00 02 80",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.579040|5GNR PDU session release complete|2025-10-29 14:48:14.761946|15|4|0|UL|2E 03 85 D4",
                        "QC5GNR_NASMSG|2025-10-29 14:51:30.579067|5GNR UL NAS transport|2025-10-29 14:48:14.762066|15|4|0|UL|7E 00 67 01 00 04 2E 03 85 D4 12 03",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.620316|5GNR ulInformationTransfer|2025-10-29 14:48:14.762377|16|144|UL DCCH|2|110|654048|4753425|3A 09 BF 01 5B 24 61 C2 2F 32 E4 AA CE 75 5D 7D EE 28 9C CB 19 80",
                        "QC5GNR_RRCMSG|2025-10-29 14:51:30.620657|5GNR rrcReconfigurationComplete|2025-10-29 14:48:14.763419|16|144|UL DCCH|1|110|654048|15239193|08 00"
                    ]
                }
            ]
        }
    ]
}


xcal_l3_report_schema = {
    "type": "object",
    "properties": {
        "mts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},  # mismatch: response has int
                    "name": {"type": "string","const": "XCAL"},
                    "mobile": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "index": {"type": "integer"},
                                "L3MSG": {},
                            },
                            "required": ["index", "L3MSG"],
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

xcal_reports_kpi_schema2 = {
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
                            "properties": {
                                "index": {"type": "integer"},
                                "KPIParameter": {"type": "array",
                                                 "items": {"type": "object",
                                                 "properties": {
                                                     "time": {"type": "string"},
                                                     "KPIParameter": {"type": "object",
                                                                      "properties": {
                                                                          "LTE": {"type": "object",
                                                                              "properties": {
                                                                                  "ML1 Downlink Info": {"type": "object"},
                                                                              },
                                                                              "required": ["ML1 Downlink Info",],},
                                                                              },
                                                                      "required": ["LTE",],
                                                                      },
                                                 },
                                                 "required": ["time", "KPIParameter"],
                                                 }
                                                 },
                            },
                            "required": ["index", "KPIParameter"],
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

xcal_reports_kpi_schema2bu = {
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
                            "properties": {
                                "index": {"type": "integer"},
                                "KPIParameter": {"type": "array"}
                            },
                            "required": ["index", "KPIParameter"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["index", "name", "mobile"],
                "additionalProperties": False,
            },
        }
    },
    # "required": ["mts"],
    "required": ["mts"],
    "additionalProperties": False,
}


def main():
    try:
        validate(instance=tr2, schema=xcal_l3_report_schema)
        print("Response matches schema")
        assert True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        assert False


if __name__ == "__main__":
    main()
