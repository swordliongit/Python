import requests
from headers import headers4


def Search(session):
    data = {
        "ProductType": "CityHotel",
        "HotelId": "594593",
        "IsAgencyRequest": "False",
        "BookingCode": "",
        "BookingDate": "",
        "BookingDateFrom": "",
        "BookingDateTo": "",
        "StartDateFrom": "",
        "EndDateTo": "",
        "BookingStatus": "",
        "ConfirmationStatus": "",
        "CancelDateFrom": "",
        "CancelDateTo": "",
        "PassengerSearchRequest.Name": "",
        "PassengerSearchRequest.Surname": "",
        "DataTableRequest[Page]": "1",
        "DataTableRequest[PageSize]": "25",
        "DataTableRequest[SortColumn]": "Id",
        "DataTableRequest[SortIsAscending]": "false",
        "DataTableRequest[Start]": "0",
    }

    response = session.post(
        "https://extranet.jollytur.ws/HotelReservation/Search",
        headers=headers4,
        data=data,
    )
    print(response.text)
