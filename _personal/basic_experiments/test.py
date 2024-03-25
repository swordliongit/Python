d1 = {
    "meterValue": [
        {
            "sampledValue": [
                {
                    "context": "Sample.Periodic",
                    "measurand": "Energy.Active.Import.Register",
                    "unitOfMeasure": {"multiplier": 0, "unit": "kWh"},
                    "value": 0.57,
                },
                {
                    "context": "Sample.Periodic",
                    "measurand": "Current.Import",
                    "unitOfMeasure": {"unit": "A"},
                    "value": 24.0673828125,
                },
                {
                    "context": "Sample.Periodic",
                    "measurand": "Voltage",
                    "unitOfMeasure": {"unit": "V"},
                    "value": 396.7783203125,
                },
                {
                    "context": "Sample.Periodic",
                    "measurand": "Power.Active.Import",
                    "unitOfMeasure": {"unit": "W"},
                    "value": 9549.415726661682,
                },
                {
                    "context": "Sample.Periodic",
                    "measurand": "SoC",
                    "unitOfMeasure": {"unit": "Percent"},
                    "value": 41.0,
                },
            ],
            "timestamp": "2023-01-04T15:19:43Z",
        }
    ]
}

d2 = {"transactionInfo": {"chargingState": "Charging", "transactionId": "b341832e-2558-4d3b-aab2-539a1d11ec8d"}}
d2['transactionInfo'].update({'id': "1007"})
d3 = {**d1, **d2}
print(d3)
