# import datetime


# {
#     "ReservationList": [
#         {
#             "OperatorName": "ZEN TOUR TURIZM A.Ş. ANKARA",
#             "ResType": "Y",
#             "ResConf": "W",
#             "Hotel": "H2S",
#             "HotelName": "H2S Test Hotel",
#             "HotelPaximumID": PAXIMUM_ID,
#             "CinDate": datetime(2023, 9, 2).strftime("%Y.%m.%d"),
#             "CoutDate": datetime(2023, 9, 4).strftime("%Y.%m.%d"),
#             "Day": 2,
#             "RoomCode": "SNG",
#             "RoomName": "SINGLE",
#             "RoomCount": 1,
#             "AccomCode": "STD",
#             "AccomName": "STANDART ODA",
#             "BoardCode": "ALL",
#             "BoardName": "ALL INCLUSIVE (AI)",
#             "Adl": 2,
#             "ExtBed": 0,
#             "Chd": 0,
#             "Inf": 0,
#             "TotalPax": 2,
#             "ResNote": "TEST NOTE",
#             "ResAmount": 100.0,
#             "ResAmountCurr": "TR",
#             "SellingDate": datetime(2023, 9, 2).strftime("%Y.%m.%d"),
#             "AllotmentType": "G",
#             "ResUser": "ARTIN",
#             "OperatorCode": "TUROP",
#             "ResNo": "123abc",
#             "ResOrder": 1,
#             "DatabaseName": "ARTINSYSTEMS",
#             "ChgDate": datetime(2023, 9, 4).strftime("%Y.%m.%d"),
#             "UniqueID": 1001,
#             "UserName": "ARTINSYSTEMS",
#         }
#     ]
# }


from datetime import datetime

# Base Id and date
base_id = 14925582
base_date = datetime(2023, 10, 31)

# Given date
given_date = datetime(2023, 10, 31)  # Change this to your desired date
# Calculate the number of days between the given date and the base date
day_difference = (given_date - base_date).days
# Calculate the Id value based on the pattern
id_value = base_id + day_difference

print(id_value)
