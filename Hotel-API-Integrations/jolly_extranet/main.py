import ast
from datetime import datetime
from time import sleep

import requests

from jolly_extranet_login import Login
from jolly_extranet_search import Search
from jolly_extranet_get_quota import Get_Quota
from jolly_extranet_update_quota import Update_Quota
from jolly_extranet_add_price import Add_Price
from jolly_extranet_update_price import Update_Price

# from jtest import jtest


def main():
    s = requests.Session()
    s = Login(s)

    # jollyextranet_search(s)

    # Get Rooms
    # print(Get_Quota(s, HotelId="14056", date=datetime(2023, 10, 1)))

    # Update Quota ( Start, Stop )
    # Update_Quota(
    #     s,
    #     HotelRoomId="38315",
    #     Quota=5,
    #     QuotaDate=datetime(2023, 10, 31),
    #     Deadline=0,
    #     SaleStatus=0,
    # )

    # Add Price
    args = {
        "HotelId": "4957",
        "HotelRoomId": "9027",
        "IsSingleMaleRestriction": True,  # Tek Bay Kısıtlaması
        "PriceTitle": "K",  # Fiyat Adı
        "MinNight": "3",
        "pension type": "1013",  # Pansiyon Tipi,
        "Currency": "TRY",
        "HotelCancelPolicyId": "1",  # İptal Politikası
        "HotelRoomTypeName": "Standart Oda",
        "Double": {
            "RateCost": "1800.00",
            "ExtraBedCost": "",
            "Child1Cost": "450.00",
            "Child2Cost": "450.00",
            "Child3Cost": "",
            "Child4Cost": "",
        },
        "Single": {
            "RateCost": "1800.00",
            "ExtraBedCost": "600",
            "Child1Cost": "450.00",
            "Child2Cost": "450.00",
            "Child3Cost": "",
            "Child4Cost": "700",
        },
        "Triple": {
            "RateCost": "2430.00",
            "ExtraBedCost": "",
            "Child1Cost": "450.00",
            "Child2Cost": "450.00",
            "Child3Cost": "550.00",
            "Child4Cost": "",
        },
        "CheckinStartDate": datetime(2023, 11, 12).strftime("%d.%m.%Y"),
        "CheckinEndDate": datetime(2023, 11, 15).strftime("%d.%m.%Y"),
        "weekdays": [True, True, True, True, True, True, True],  # Pzt, Salı, Çarş, Perş, Cuma, Cumartesi, Pazar
        "ScopePath": "/",  # Kanal
        "ExcludeScopePaths": [""],  # Harici Kanal
    }

    hotel_price_id = Add_Price(session=s, params=args)
    print(hotel_price_id)

    sleep(5)

    # Update Price

    # Add HotelPriceId key to args for Update
    args.update({"HotelPriceId": hotel_price_id})
    # args.update({"HotelPriceId": "43459737"})
    args["Single"]["RateCost"] = "3333.00"
    args["Double"]["RateCost"] = "3333.00"
    args["Triple"]["Child4Cost"] = "3333.00"
    args["MinNight"] = "1"
    args["HotelCancelPolicyId"] = "133"
    args["ExcludeScopePaths"] = ["//B2B/Corporate"]

    Update_Price(session=s, params=args)


if __name__ == "__main__":
    main()
