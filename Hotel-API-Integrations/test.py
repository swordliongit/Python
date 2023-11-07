from datetime import datetime


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

print(params["weekdays"][0])
