import requests
from datetime import datetime
from headers import headers_price


def Add_Price(session: requests.Session, params):
    payload = {
        "HotelPrice": {
            "HotelId": params["HotelId"],  # "4957",
            "HotelRateTypeId": "2",
            "IsIncludeBreakfast": "True",
            "IsIncludeKDV": "True",
            "IsGroupRate": "False",
            "Remark": "",
            "UserId": "",
            "IsActionRate": "False",
            "IsOpportunity": "False",
            "IsSpecialPeriod": "False",
            "IsPackageRate": "False",
            "EarlyBooking": "False",
            "AlternativePrice": "False",
            "HotelPriceComissionList": [
                {"MarkupCommissionTypeId": "1", "Commission": "15,00", "ComissionAmountTypeId": "1"},
                {"MarkupCommissionTypeId": "2", "Commission": "", "ComissionAmountTypeId": "1"},
            ],
            "HotelPriceRateTypeId": "1",
            "IsSingleMaleRestriction": params["IsSingleMaleRestriction"],  # "true",
            "PriceTitle": params["PriceTitle"],  # "B",
            "MinNight": params["MinNight"],  # "3",
            "MealTypeId": params["pension type"],  # "1013",
            "Currency": params["Currency"],  # "TRY",
            "CurrencySale": "",
            "HotelCancelPolicyId": params["HotelCancelPolicyId"],  # "1", -> Standart İptal
            "Id": "0",
            "HotelPriceItemGroupedList": [
                {
                    "IsDisable": "true",
                    "HotelRoomId": params["HotelRoomId"],  # "9027",
                    "HotelRoomTypeName": params["HotelRoomTypeName"],  # "Standart Oda",
                    "HotelPriceItemList": [
                        {
                            "HotelRoomId": params["HotelRoomId"],
                            "HotelId": params["HotelId"],
                            "HotelPriceId": "0",
                            "HotelAccommodationOptionTypeValue": "1",
                            "ChildRanges": {
                                "1Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "1", "AgeFrom": "0,00", "AgeTo": "6,99"},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "2Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "3Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "4Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                ],
                            },
                            "RateCost": params["Double"]["RateCost"],  # "1800,00",
                            "RateSale": "",
                            "IsExtrabedDisable": params["Double"]["IsExtrabedDisable"],  # "true",
                            "Child1Cost": params["Double"]["Child1Cost"],  # "450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Double"]["Child2Cost"],  # "450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "IsChild3Disable": "true",
                            "IsChild4Disable": "true",
                        },
                        {
                            "HotelRoomId": params["HotelRoomId"],
                            "HotelId": params["HotelId"],
                            "HotelPriceId": "0",
                            "HotelAccommodationOptionTypeValue": "2",
                            "ChildRanges": {
                                "1Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "1", "AgeFrom": "0,00", "AgeTo": "6,99"},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "2Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "3Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "4Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                ],
                            },
                            "RateCost": params["Single"]["RateCost"],  # "1800,00",
                            "RateSale": "",
                            "IsExtrabedDisable": params["Single"]["IsExtrabedDisable"],
                            "Child1Cost": params["Single"]["Child1Cost"],  # ""450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Single"]["Child2Cost"],  # ""450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "IsChild3Disable": "true",
                            "IsChild4Disable": "true",
                        },
                        {
                            "HotelRoomId": params["HotelRoomId"],
                            "HotelId": params["HotelId"],
                            "HotelPriceId": "0",
                            "HotelAccommodationOptionTypeValue": "3",
                            "ChildRanges": {
                                "1Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "1", "AgeFrom": "0,00", "AgeTo": "6,99"},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "1", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "2Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "2", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "3Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "3", "AgeFrom": "", "AgeTo": ""},
                                ],
                                "4Cocuk": [
                                    {"Id": "0", "ChildPriceGroupTypeId": "1", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "2", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                    {"Id": "0", "ChildPriceGroupTypeId": "3", "ChildTypeId": "4", "AgeFrom": "", "AgeTo": ""},
                                ],
                            },
                            "RateCost": params["Triple"]["RateCost"],  # "2430,00",
                            "RateSale": "",
                            "IsExtrabedDisable": params["Triple"]["IsExtrabedDisable"],
                            "Child1Cost": params["Triple"]["Child1Cost"],  # "450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Triple"]["Child2Cost"],  # "450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "IsChild3Disable": "true",
                            "IsChild4Disable": "true",
                        },
                    ],
                }
            ],
        },
        "HotelId": params["HotelId"],  # "4957",
        "MarketId": "1",
        "CheckinStartDate": params["CheckinStartDate"],  # "12.11.2023",
        "CheckinEndDate": params["CheckinEndDate"],  # "15.11.2023",
        "ScopePath": "/",
        "ExcludeScopePaths": [""],
        "HotelPriceValidDays": {
            "WeekdayMonday": params["weekdays"][0],  # "true",
            "WeekdayTuesday": params["weekdays"][1],
            "WeekdayWednesday": params["weekdays"][2],
            "WeekdayThursday": params["weekdays"][3],
            "WeekdayFriday": params["weekdays"][4],
            "WeekdaySaturday": params["weekdays"][5],
            "WeekdaySunday": params["weekdays"][6],
            "IsSelectedAllWeekDay": params["IsSelectedAllWeekDay"],
        },
    }

    # Send the POST request
    response = session.post(
        "https://extranet.jollytur.ws/HotelPrice/CreateHotelPrice",
        headers=headers_price,
        data=payload,
    )

    if response.status_code == 200:
        print(response.text)
    else:
        print(response.text)
        print(f"Request failed with status code {response.status_code}")
