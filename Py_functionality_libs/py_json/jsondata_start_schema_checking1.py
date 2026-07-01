
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
                    "KPIParameter": [
                        {
                            "time": "2025/10/29 08:39:18.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000957264972385019,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000957264972385019,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0.000140350879519247,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 6.39999998384155e-05,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -121.890625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -123.5234375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -122.46875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -123.5390625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.71875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -16.28125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.33333349227905,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00437956210225821,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000957264972385019,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000957264972385019,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:19.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00120000005699694,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00120000005699694,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -120.890625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -120.8125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.1953125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -123.78125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -119.6875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.671875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.66666650772095,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:20.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00120000005699694,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00120000005699694,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -121.3359375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -121.3984375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.5859375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.3515625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -118.2109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.9921875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.66666650772095,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:21.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000768000027164817,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000768000027164817,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -120.2109375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -120.046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.515625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -122.296875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.2265625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.59375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.5,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            50,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            50,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00249999994412065,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000768000027164817,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000768000027164817,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:22.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00112000002991408,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00112000002991408,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -121.1640625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -122.875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -122.125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -124.171875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -119.7421875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -16.09375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.33333349227905,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00112000002991408,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00112000002991408,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:23.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.0015442359726876,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.0015442359726876,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -120.5546875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -120.3046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.578125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -125.3046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -120.96875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.984375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00357142859138548,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.0015442359726876,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.0015442359726876,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:24.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00120000005699694,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00120000005699694,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -120.5234375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -120.3828125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.6640625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -124.359375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -117.2578125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.953125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.66666650772095,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:25.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00120000005699694,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00120000005699694,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -121.125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -122.015625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.1875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -127.4609375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -118.0078125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.71875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.66666650772095,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:26.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000985714257694781,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000985714257694781,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -120.96875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -122.65625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -120.9140625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -128.71875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -120.3359375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -15.5078125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.6666660308838,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.33333349227905,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00267857150174677,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000985714257694781,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "QPSK",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000985714257694781,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:27.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 6,
                                        "M_TMSI": "0xE00B59D5"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 1894,
                                        "UL PDCP PDU(Total)": 15
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00120000005699694,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00120000005699694,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -121.5234375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -121.6875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -124.125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -124.8046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -121.9921875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -16.515625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25.3333339691162,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            4.66666650772095,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            33.3333320617676,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            66.6666641235352,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00120000005699694,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE01259E3",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        }
                    ]
                },
                {
                    "index": 2,
                    "KPIParameter": [
                        {
                            "time": "2025/10/29 08:39:18.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00115405162796378,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00115405162796378,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -111.8515625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -111.9921875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -113.859375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -129.1953125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -115.8359375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.84375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -3.03582167625427,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -1.96052360534668,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -11.2948637008667,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -3.01879048347473,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            -1.96052360534668,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00374765763990581,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00115405162796378,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00115405162796378,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:19.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -111.109375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -111.109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.453125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -150,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -116.421875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.9296875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -2.96809411048889,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -1.40481746196747,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -9.76876163482666,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -3.29058718681335,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            -1.40481746196747,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:20.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -111.2890625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -111.328125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.3984375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -128.765625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -116.109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -12.0703125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                1.00289750099182,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.03988695144653,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -10.3717212677002,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.67734360694885,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            3.67734360694885,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3.33333325386047,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:21.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000864000001456589,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000864000001456589,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -111.40625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -111.6484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -115.4609375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -131.9921875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -119.1171875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -12.0234375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -1.19878935813904,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.79751539230347,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -16.6787719726562,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                2.31246519088745,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            3.79751539230347,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00249999994412065,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:22.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -110.9453125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -110.7578125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.2734375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -128.4609375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -115.84375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -12.0234375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -2.78711199760437,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -0.570236206054687,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -9.49602127075195,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -2.87666034698486,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            -0.570236206054687,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:23.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00154285714961588,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00154285714961588,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -110.390625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -110.1484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.4765625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -127.9375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.84375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.984375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -0.722808599472046,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.73694825172424,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                2.69822931289673,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            3.73694825172424,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00357142859138548,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00154285714961588,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00154285714961588,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:24.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -111.171875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -111.21875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -124.5,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -116.3203125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.9140625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -0.253228306770325,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.95217156410217,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -12.0411996841431,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                2.20404362678528,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            3.95217156410217,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:25.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -110.78125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -110.640625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -114.3203125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -130.3359375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -117.5234375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.8359375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -0.479306221008301,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                3.77445697784424,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -10.0597858428955,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                2.19637727737427,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            3.77445697784424,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:26.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00115714280400425,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00115714280400425,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -110.703125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -110.609375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -113.84375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -127.5703125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -115.3671875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.9609375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -2.73107314109802,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -0.546122074127197,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -9.27514553070068,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -3.03582167625427,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            -0.546122074127197,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3.33333325386047,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00267857150174677,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00115714280400425,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00115714280400425,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:27.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "Signaling Message": {
                                        "MME_Code": 194,
                                        "M_TMSI": "0xF0056895"
                                    },
                                    "PDCP Statistics Summary": {
                                        "DL PDCP PDU(Total)": 47726,
                                        "UL PDCP PDU(Total)": 173
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SCS": [
                                            "30kHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -112.25,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -112.8125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -113.78125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -128.515625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -117.109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.8046875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-SINR 0/1/2/3": [
                                            [
                                                -2.73903465270996,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -1.57210421562195,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -10.1466474533081,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -3.59992432594299,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-SINR(Max)": [
                                            -1.57210421562195,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            3.33333325386047,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xF0056896",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "LTE RRC Idle",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        }
                    ]
                },
                {
                    "index": 3,
                    "KPIParameter": [
                        {
                            "time": "2025/10/29 08:39:19.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.40625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -108.3125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.8671875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.2578125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.6015625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:20.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00191920856013894,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00191920856013894,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -107.890625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.7890625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.8203125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.46875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.5625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.8359375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                24.625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            7.25,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            75,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            25,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00329218106344342,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00191920856013894,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00191920856013894,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:21.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.578125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -108.484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.1875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.640625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.59375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00346820801496506,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:22.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00115611066576093,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00115611066576093,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.703125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -108.6953125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.3046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.1171875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.40625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00267857150174677,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00115611066576093,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00115611066576093,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:23.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.0859375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.8671875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.6015625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.78125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.765625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:24.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.25,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -108.078125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.21875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.7578125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.4296875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.6875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:25.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00115611066576093,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00115611066576093,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -107.8125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.3046875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.6484375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.4609375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.859375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00267857150174677,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00115611066576093,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00115611066576093,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:26.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0.000171171166584827,
                                        "PHY PUSCH TP(Total)": 0.0028800000436604,
                                        "MAC DL TP(Total)": 0.000171171166584827,
                                        "MAC UL TP(Total)": 0.0028800000436604,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "DL BLER(%)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -108.875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -108.8984375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.1015625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -112.75,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.765625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.609375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                24.25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "PUCCH Power 0/1": [
                                            [
                                                9,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "DL MCS(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL MCS(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL QPSK Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 16QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Inc0)": [
                                            0.00100000004749745,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            9.25,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            50,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            50,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00432432442903519,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Init BLER": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0.000171171166584827,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.0028800000436604,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Modulation Type": [
                                            "QPSK",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "64QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0.000171171166584827,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.0028800000436604,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:27.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000432000000728294,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000432000000728294,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0.000859701482113451,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0.000827860669232905,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -109.125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -109.0625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -110.5078125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -111.078125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -109.1328125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -11.4296875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00148148147854954,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000432000000728294,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000432000000728294,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892209152
                                }
                            }
                        }
                    ]
                },
                {
                    "index": 4,
                    "KPIParameter": [
                        {
                            "time": "2025/10/29 08:39:18.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -105.0625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.390625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -105.109375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.7734375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00468384055420756,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:19.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0.000876018078997731,
                                        "PHY PUSCH TP(Total)": 0.00243571423925459,
                                        "MAC DL TP(Total)": 0.000876018078997731,
                                        "MAC UL TP(Total)": 0.00243571423925459,
                                        "RLC DL TP(Total)": 0.000798387103714049,
                                        "RLC UL TP(Total)": 0.000542857160326093,
                                        "PDCP DL TP(Total)": 0.000774193555116653,
                                        "PDCP UL TP(Total)": 0.000435714289778844,
                                        "DL BLER(%)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -104.9453125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.0234375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.9140625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.7109375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "PUCCH Power 0/1": [
                                            [
                                                7,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "DL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL MCS(Avg)": [
                                            5.5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Avg)": [
                                            3,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Inc0)": [
                                            0.00300000002607703,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Mode)": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            6.80000019073486,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00446428591385484,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Init BLER": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0.000876018078997731,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00243571423925459,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0.000876018078997731,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00243571423925459,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:20.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0.000887958100065589,
                                        "PHY PUSCH TP(Total)": 0.000864000001456589,
                                        "MAC DL TP(Total)": 0.000887958100065589,
                                        "MAC UL TP(Total)": 0.000864000001456589,
                                        "RLC DL TP(Total)": 0.000563300156500191,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0.000546230468899012,
                                        "PDCP UL TP(Total)": 0,
                                        "DL BLER(%)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -105.171875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.0625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -105.1796875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "DL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Avg)": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Inc0)": [
                                            0.0020000000949949,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Mode)": [
                                            4,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00208333344198763,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Init BLER": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0.000887958100065589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0.000887958100065589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:21.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.000864000001456589,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.000864000001456589,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -105.0859375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.2734375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -105.09375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.765625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00249999994412065,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.000864000001456589,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:22.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -105.171875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.3203125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -105.1953125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.8046875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:23.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0.000134513276861981,
                                        "PHY PUSCH TP(Total)": 0.00198047910816967,
                                        "MAC DL TP(Total)": 0.000134513276861981,
                                        "MAC UL TP(Total)": 0.00198047910816967,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0.000576303340494633,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0.000462559255538508,
                                        "DL BLER(%)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -104.859375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.1328125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.78125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.7421875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "PUCCH Power 0/1": [
                                            [
                                                7,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "DL MCS(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL MCS(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL QPSK Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 16QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Inc0)": [
                                            0.00100000004749745,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5.19999980926514,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00444444455206394,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Init BLER": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0.000134513276861981,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00198047910816967,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL Modulation Type": [
                                            "QPSK",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0.000134513276861981,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00198047910816967,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:24.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -107.3125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.984375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.84375,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00314136128872633,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:25.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -104.6640625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -106.8515625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.6171875,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.8125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:26.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00115508015733212,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00115508015733212,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -104.625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -106.6640625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.5859375,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.8046875,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00267857150174677,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00115508015733212,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00115508015733212,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        },
                        {
                            "time": "2025/10/29 08:39:27.000",
                            "KPIParameter": {
                                "LTE": {
                                    "ML1 Downlink Info": {
                                        "DL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    },
                                    "ML1 Uplink Info": {
                                        "UL Modulation Type(PCell...)": [
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            "",
                                            ""
                                        ]
                                    }
                                },
                                "5GNR": {
                                    "Throughput": {
                                        "PHY PDSCH TP(Total)": 0,
                                        "PHY PUSCH TP(Total)": 0.00129599997308105,
                                        "MAC DL TP(Total)": 0,
                                        "MAC UL TP(Total)": 0.00129599997308105,
                                        "RLC DL TP(Total)": 0,
                                        "RLC UL TP(Total)": 0,
                                        "PDCP DL TP(Total)": 0,
                                        "PDCP UL TP(Total)": 0,
                                        "UL BLER(%)": 0
                                    },
                                    "RF": {
                                        "PCI": [
                                            110,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "NR-ARFCN": [
                                            654048,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "Frequency": [
                                            3810.71997070313,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SSB ID": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "SS-RSRP0": [
                                            -104.953125,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RSRP 0/1/2/3": [
                                            [
                                                -106.7890625,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                -104.9453125,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "SS-RSRQ": [
                                            -10.8515625,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "RI": [
                                            1,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "CQI": [
                                            6,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Power 0/1": [
                                            [
                                                25,
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ],
                                            [
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null",
                                                "null"
                                            ]
                                        ],
                                        "5G UE State": "5GNR",
                                        "Band": [
                                            "n77",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "DL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BW": [
                                            "100MHz",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer1": {
                                        "UL MCS(Mode)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL MCS(Avg)": [
                                            5,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Pi/2 BPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL QPSK Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 16QAM Rate": [
                                            100,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 64QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL 256QAM Rate": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Avg)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Inc0)": [
                                            0.00312500004656613,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL RB Num(Mode)": [
                                            2,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL BLER(%)": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PDSCH Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "PUSCH Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "UL Modulation Type": [
                                            "16QAM",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Layer2": {
                                        "MAC DL Throughput": [
                                            0,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ],
                                        "MAC UL Throughput": [
                                            0.00129599997308105,
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null",
                                            "null"
                                        ]
                                    },
                                    "Signaling Message": {
                                        "5G TMSI": "0xE0034E93",
                                        "5G AMF Set ID": 63,
                                        "5G AMF Pointer": 2,
                                        "5G AMF Region ID": 161,
                                        "5GNR System Info": {
                                            "5GBand": 77,
                                            "5GNRARFCN_PointA": 653388,
                                            "5GBW": "100MHz(273)",
                                            "5Gn_TimingAdvanceOffset": "n25600",
                                            "5GSSB_Periodicity": "ms20",
                                            "5GDMRS_TypeA_Position": "pos2",
                                            "5GSSB_PositionInBurst": " 11001111 00000000 00000000 00000000  00000000 00000000 00000000 00000000"
                                        },
                                        "5GNR TDD UL-DL Configuration": {
                                            "Pattern1": {
                                                "5Gdl_UL_TransmissionPeriodicity_P1": "ms0p5",
                                                "5GnrofDownlinkSlots_P1": 3,
                                                "5GnrofDownlinkSymbols_P1": 6,
                                                "5GnrofUplinkSlots_P1": 2,
                                                "5GnrofUplinkSymbols_P1": 4
                                            },
                                            "Pattern2": {
                                                "5Gdl_UL_TransmissionPeriodicity_P2": "ms2",
                                                "5GnrofDownlinkSlots_P2": 4,
                                                "5GnrofDownlinkSymbols_P2": 0,
                                                "5GnrofUplinkSlots_P2": 0,
                                                "5GnrofUplinkSymbols_P2": 0
                                            }
                                        }
                                    }
                                },
                                "Common": {
                                    "RRC State": {
                                        "NSA Current State": "Unknown",
                                        "RRC Current State": "NR RRC Connected"
                                    },
                                    "Operator": {
                                        "Operator": "Verizon"
                                    }
                                },
                                "Android Status": {
                                    "EMM State/Sub": [],
                                    "Android Data State": 2,
                                    "IMSI": 311479987339264,
                                    "Min": 7892208640
                                }
                            }
                        }
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
                                                                          "LTE": {
                                                                          "ML1 Downlink Info": {"required": ["DL Modulation Type(PCell...)", ],},
                                                                          "ML1 Uplink Info": {"required": ["UL Modulation Type(PCell...)", ],},
                                                                              "required": ["ML1 Downlink Info","ML1 Uplink Info", ],},
                                                                              },
                                                                      "required": ["LTE","5GNR","Common", "Android Status"],
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
        validate(instance=tr2, schema=xcal_reports_kpi_schema2)
        print("Response matches schema")
        assert True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        assert False


if __name__ == "__main__":
    main()
