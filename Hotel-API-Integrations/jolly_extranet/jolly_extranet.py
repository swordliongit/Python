import ast
from datetime import datetime

import requests

from jolly_extranet_login import Login
from jolly_extranet_search import Search
from jolly_extranet_get_quota import Get_Quota
from jolly_extranet_update_quota import Update_Quota
from jolly_extranet_add_price import Add_Price
from jtest import jtest


def main():
    s = requests.Session()
    s = Login(s)

    # jollyextranet_search(s)

    # Get Rooms
    # print(Get_Quota(s, HotelId="14056", date=datetime(2023, 10, 1)))

    # Add Price
    params = {
        "HotelId": "4957",
        "HotelRoomId": "9027",
        "IsSingleMaleRestriction": True,
        "PriceTitle": "B",
        "MinNight": "3",
        "pension type": "1013",
        "Currency": "TRY",
        "HotelCancelPolicyId": "1",
        "HotelRoomTypeName": "Standart Oda",
        "Double": {"RateCost": "1800.00", "IsExtrabedDisable": True, "Child1Cost": "450.00", "Child2Cost": "450.00"},
        "Single": {"RateCost": "1800.00", "IsExtrabedDisable": True, "Child1Cost": "450.00", "Child2Cost": "450.00"},
        "Triple": {"RateCost": "2430.00", "IsExtrabedDisable": True, "Child1Cost": "450.00", "Child2Cost": "450.00"},
        "CheckinStartDate": datetime(2023, 11, 12).strftime("%d.%m.%Y"),
        "CheckinEndDate": datetime(2023, 11, 15).strftime("%d.%m.%Y"),
        "weekdays": [True, True, True, True, True, True, True],
        "IsSelectedAllWeekDay": True,
    }
    # Add_Price(s, params)
    jtest(s)

    # Update Quota ( Start, Stop )
    # Update_Quota(
    #     s,
    #     HotelRoomId="38315",
    #     Quota=5,
    #     QuotaDate=datetime(2023, 10, 31),
    #     Deadline=0,
    #     SaleStatus=0,
    # )


if __name__ == "__main__":
    main()
