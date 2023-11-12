import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from headers import headers_price, headers_price_followup


def Add_Price(session: requests.Session, params):
    """_summary_

    Args:
        pension type/MealTypeId:
            >>> 2108 -> 24 Saat Alkollü Ultra Her Şey Dahil
            >>> 2037 -> 24 Saat Alkolsüz Her Şey Dahil
            >>> 2106 -> 24 Saat Alkolsüz Ultra Her Şey Dahil
            >>> 2109 -> 24 Saat Her Şey Dahil
            >>> 2035 -> 24 Saat Ultra Her Şey Dahil
            >>> 2097 -> A La Carte Inclusive-Premium Paket
            >>> 2099 -> A La Carte Yarım Pansiyon
            >>> 2085 -> A'la Carte Her Şey Dahil
            >>> 1024 -> Alacarte Her Şey Dahil
            >>> 2056 -> Alacarte Oda Kahvaltı
            >>> 2054 -> Alacarte Tam Pansiyon
            >>> 2057 -> Alacarte Yarım Pansiyon
            >>> 2051 -> Alkol Extra Her şey Dahil
            >>> 2077 -> Alkol Hariç Her Şey Dahil
            >>> 1025 -> Alkollü Her Şey Dahil
            >>> 2048 -> Alkollü Tam Pansiyon Plus
            >>> 2092 -> Alkollü Ultra Her Şey Dahil
            >>> 2029 -> Alkolsüz Her Şey Dahil
            >>> 2044 -> Alkolsüz Tam Pansiyon
            >>> 2058 -> Alkolsüz Tam Pansiyon Plus
            >>> 2038 -> Alkolsüz Ultra Her Şey Dahil
            >>> 2090 -> Alkolsüz Yarım Pansiyon
            >>> 2084 -> Alkolsüz Yarım Pansiyon Plus
            >>> 2111 -> Blokajı Otele Ait Oda
            >>> 1016 -> Deluxe Her Şey Dahil
            >>> 1027 -> Deluxe Her Şey Dahil Plus
            >>> 2094 -> Diamond Ultra Herşey Dahil
            >>> 2034 -> Ela Her Şey Dahil
            >>> 2096 -> Euphoria Her Şey Dahil
            >>> 2079 -> Excellence Her Şey Dahil
            >>> 2039 -> Fame Style Her Şey Dahil
            >>> 2081 -> Fettah Can Konseri + Tam Pansiyon Konaklama
            >>> 2098 -> Gala + Her Şey Dahil
            >>> 2080 -> Gala + Tam Pansiyon Konaklama
            >>> 2045 -> Gala Programı
            >>> 2046 -> Gala Programı + Konaklama
            >>> 2086 -> Gala Programı + Yarım Pansiyon
            >>> 2049 -> Golden Her Şey Dahil
            >>> 2071 -> Half Board - All Inclusive
            >>> 1013 -> Her Şey Dahil
            >>> 1019 -> Her Şey Dahil Plus
            >>> 1017 -> High Class Her Şey Dahil
            >>> 1018 -> High Class Ultra Her Şey Dahil
            >>> 2103 -> İftar + Sahur
            >>> 2104 -> İftar Menüsü & Sahur
            >>> 2105 -> İftar Menüsü & Sahur Tabağı
            >>> 2053 -> İslami Halal Her Şey Dahil
            >>> 1026 -> Luxury Her Şey Dahil
            >>> 2042 -> Luxury Ultra Her Şey Dahil
            >>> 1015 -> Oda Kahvaltı
            >>> 2083 -> Oda Kahvaltı & Gala Dahil
            >>> 2082 -> Oda Kahvaltı / Yılbaşı Gala Dahil
            >>> 2088 -> Oda Kahvaltı + Yaz Paketi
            >>> 2063 -> Oda Kahvaltı Plus
            >>> 2060 -> Oda Kahvaltı+Yarım Pansiyon
            >>> 2047 -> Premium A La Carte Her Şey Dahil
            >>> 2070 -> Premium Her Şey Dahil
            >>> 2067 -> Premium Ultra Her Şey Dahil
            >>> 2101 -> Premium Yarım Pansiyon Plus
            >>> 2091 -> Ramazan Paketi + Konaklama
            >>> 2073 -> Royal Herşey Dahil
            >>> 2093 -> Royal Ultra Herşey Dahil
            >>> 2059 -> Sadece Bilet
            >>> 9 -> Sadece Oda
            >>> 2068 -> Sağlıklı & Lokal Her Şey Dahil
            >>> 2112 -> Sağlıklı Yoga Paketi
            >>> 2069 -> Second Home Package
            >>> 2095 -> Select Konsept
            >>> 2061 -> Self Catering
            >>> 2043 -> Soft Al
            >>> 2074 -> Soft Her Şey Dahil
            >>> 2087 -> Soft Her Şey Dahil ( Alkol Ücretli )
            >>> 1022 -> Superior Her Şey Dahil
            >>> 2 -> Tam Pansiyon
            >>> 2064 -> Tam Pansiyon Konser Dahil Paket
            >>> 10 -> Tam Pansiyon Plus
            >>> 2065 -> Tam Pansiyon Soft Plus
            >>> 2036 -> Tam Pansiyon Ultra Plus
            >>> 1023 -> Ultimate Her Şey Dahil
            >>> 4 -> Ultra Her Şey Dahil
            >>> 1021 -> Ultra Her Şey Dahil Plus
            >>> 15 -> Ultra Tam Pansiyon
            >>> 2066 -> Wellness Diyet Tam Pansiyon
            >>> 2055 -> Wellness Sağlıklı Yaşam Programı
            >>> 1014 -> Yarım Pansiyon
            >>> 2089 -> Yarım Pansiyon + Yaz Paketi
            >>> 2102 -> Yarım Pansiyon EB
            >>> 2110 -> Yarım Pansiyon Exclusive
            >>> 1020 -> Yarım Pansiyon Plus
            >>> 2052 -> Yarım Pansiyon Promosyon Uçaklı Paket
            >>> 2078 -> Yarım Pansiyon Soft
            >>> 2100 -> Yeni Ultra Her Şey Dahil
            >>> 2040 -> Yok
            >>> 2050 -> Yöresel & Sağlıklı Ultra Herşey Dahil
            >>> 2076 -> Yöresel Her Şey Dahil
        HotelCancelPolicyId:
            >>> 1 -> Standart
            >>> 2 -> İptal Edilemez Politika
            >>> 32 -> 5 Gün Kalaya Kadar İptal
            >>> 54 -> 30 Güne Kadar kesintisiz İptal Hakkı
            >>> 123 -> 3 Güne Kadar Kesintisiz İptal Hakkı
            >>> 124 -> Değişiklik ve İptal Kabul Edilemez
            >>> 133 -> 2 Gün Kalaya Kadar İptal
            >>> 134 -> 14 Gün Kalaya Kadar İptal Hakkı
            >>> 137 -> Giriş Gününe Kadar İptal Hakkı
            >>> 139 -> 1 Gün Kalaya Kadar İptal Hakkı
            >>> 141 -> 7 Güne Kadar İptal Hakkı
            >>> 165 -> 15 Gün Kalaya Kadar İptal hakkı
            >>> 192 -> 28 Güne Kadar Kesintisiz İptal Hakkı
            >>> 209 -> GORDION TEST
            >>> 296 -> 10 Gün Kalaya Kadar Kesintisiz İptal Hakkı
            >>> 477 -> 5 Gün Kalaya Kadar Kesintisiz İptal Hakkı
            >>> 478 -> 7 Güne Kadar Kesintisiz İptal Hakkı
            >>> 538 -> 21 Güne Kadar Kesintisiz İptal Hakkı
            >>> 650 -> 35 Güne Kadar Kesintisiz İptal hakkı
        ScopePath:
            >>> "//B2B/Corporate" -> Kurumsal
        ExcludeScopePaths:
            >>> ["//B2B/Corporate"] -> Kurumsal

    """
    raw_data = {
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
                            "ExtraBedCost": params["Double"]["ExtraBedCost"],
                            "ExtraBedSale": "",
                            "IsExtrabedDisable": True if params["Double"]["ExtraBedCost"] == "" else False,  # "true",
                            "Child1Cost": params["Double"]["Child1Cost"],  # "450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Double"]["Child2Cost"],  # "450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "Child3Cost": params["Double"]["Child3Cost"],  # "450,00",
                            "Child3Cost2": "",
                            "Child3Sale": "",
                            "Child3Sale2": "",
                            "Child4Cost": params["Double"]["Child4Cost"],  # "450,00",
                            "Child4Cost2": "",
                            "Child4Sale": "",
                            "Child4Sale2": "",
                            "IsChild1Disable": True if params["Double"]["Child1Cost"] == "" else False,
                            "IsChild2Disable": True if params["Double"]["Child2Cost"] == "" else False,
                            "IsChild3Disable": True if params["Double"]["Child3Cost"] == "" else False,
                            "IsChild4Disable": True if params["Double"]["Child4Cost"] == "" else False,
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
                            "ExtraBedCost": params["Single"]["ExtraBedCost"],
                            "ExtraBedSale": "",
                            "IsExtrabedDisable": True if params["Double"]["ExtraBedCost"] == "" else False,  # "true",
                            "Child1Cost": params["Single"]["Child1Cost"],  # "450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Single"]["Child2Cost"],  # "450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "Child3Cost": params["Single"]["Child3Cost"],  # "450,00",
                            "Child3Cost2": "",
                            "Child3Sale": "",
                            "Child3Sale2": "",
                            "Child4Cost": params["Single"]["Child4Cost"],  # "450,00",
                            "Child4Cost2": "",
                            "Child4Sale": "",
                            "Child4Sale2": "",
                            "IsChild1Disable": True if params["Single"]["Child1Cost"] == "" else False,
                            "IsChild2Disable": True if params["Single"]["Child2Cost"] == "" else False,
                            "IsChild3Disable": True if params["Single"]["Child3Cost"] == "" else False,
                            "IsChild4Disable": True if params["Single"]["Child4Cost"] == "" else False,
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
                            "ExtraBedCost": params["Double"]["ExtraBedCost"],
                            "ExtraBedSale": "",
                            "IsExtrabedDisable": True if params["Double"]["ExtraBedCost"] == "" else False,  # "true",
                            "Child1Cost": params["Triple"]["Child1Cost"],  # "450,00",
                            "Child1Cost2": "",
                            "Child1Sale": "",
                            "Child1Sale2": "",
                            "Child2Cost": params["Triple"]["Child2Cost"],  # "450,00",
                            "Child2Cost2": "",
                            "Child2Sale": "",
                            "Child2Sale2": "",
                            "Child3Cost": params["Triple"]["Child3Cost"],  # "450,00",
                            "Child3Cost2": "",
                            "Child3Sale": "",
                            "Child3Sale2": "",
                            "Child4Cost": params["Triple"]["Child4Cost"],  # "450,00",
                            "Child4Cost2": "",
                            "Child4Sale": "",
                            "Child4Sale2": "",
                            "IsChild1Disable": True if params["Triple"]["Child1Cost"] == "" else False,
                            "IsChild2Disable": True if params["Triple"]["Child2Cost"] == "" else False,
                            "IsChild3Disable": True if params["Triple"]["Child3Cost"] == "" else False,
                            "IsChild4Disable": True if params["Triple"]["Child4Cost"] == "" else False,
                        },
                    ],
                }
            ],
        },
        "HotelId": params["HotelId"],  # "4957",
        "MarketId": "1",
        "CheckinStartDate": params["CheckinStartDate"],  # "12.11.2023",
        "CheckinEndDate": params["CheckinEndDate"],  # "15.11.2023",
        "ScopePath": params["ScopePath"],  # "/"
        "ExcludeScopePaths": params["ExcludeScopePaths"],  # [""]
        "HotelPriceValidDays": {
            "WeekdayMonday": params["weekdays"][0],  # "true",
            "WeekdayTuesday": params["weekdays"][1],
            "WeekdayWednesday": params["weekdays"][2],
            "WeekdayThursday": params["weekdays"][3],
            "WeekdayFriday": params["weekdays"][4],
            "WeekdaySaturday": params["weekdays"][5],
            "WeekdaySunday": params["weekdays"][6],
            "IsSelectedAllWeekDay": all(params["weekdays"]),
        },
    }
    payload = json.dumps(raw_data)

    # Send the POST request
    response = session.post(
        "https://extranet.jollytur.ws/HotelPrice/CreateHotelPrice",
        headers=headers_price,
        data=payload,
    )

    if response.status_code == 200:
        print(response.text)
        # Proceed with the second GET request to the URL with headers
        second_response = session.get("https://extranet.jollytur.ws/HotelPrice/HotelPrice", headers=headers_price_followup)

        if second_response.status_code == 200:
            # Extract data from the second response as needed
            html_content = second_response.text

            soup = BeautifulSoup(html_content, "html.parser")

            # Find all forms with the class "form-panel"
            price_forms = soup.find_all("form", class_="form-panel")
            # print(price_forms)

            if price_forms:
                most_recent_form = price_forms[-1]  # Using -1 to get the last form in the list
                hotel_price_id = most_recent_form.find("input", {"id": "HotelPriceId"})["value"]

                print("Most Recent HotelPriceId:", hotel_price_id)
                return hotel_price_id
            else:
                print("No price forms found in the HTML.")
        else:
            print(f"Second request failed with status code {second_response.status_code}")
    else:
        print(f"Request failed with status code {response.status_code}")
