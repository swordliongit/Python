import requests
from datetime import datetime
from headers import headers_quota


def Update_Quota(
    session: requests.Session,
    HotelRoomId: str,
    Quota: int,
    QuotaDate: datetime,
    Deadline: datetime,
    SaleStatus: int,
):
    """_summary_

    Args:
        session (requests.Session): _description_

        HotelRoomId (str):
        >>> 9027 -> Hotel Çamyuva Beach - Standart
        >>> 38314 -> Alexius Beach Hotel - Standart
        >>> 38315 -> Alexius Beach Hotel - Family

        Quota (int): _description_
        QuotaDate (datetime): _description_
        Deadline (datetime): _description_

        SaleStatus (int):
        >>> 0 -> Satışa Açık
        >>> 1 -> Serbest Satış  (Girilen deadline bile olsa satışa açacaktır)
        >>> 2 -> Satışı Durdur
        >>> 3 -> Sor Sat
    """
    base_id = 0
    base_date = datetime(2023, 10, 23)
    if HotelRoomId == "38314":
        # Base Id and date
        base_id = 14925582
    elif HotelRoomId == "38315":
        base_id = 14925761
    elif HotelRoomId == "9027":
        base_id = 14927121

    # Given date
    given_date = QuotaDate  # Change this to your desired date
    # Calculate the number of days between the given date and the base date
    day_difference = (given_date - base_date).days
    # Calculate the Id value based on the pattern
    id_value = base_id + day_difference
    payload = {
        "HotelRoomQuotaItemDto[0][Id]": id_value,
        "HotelRoomQuotaItemDto[0][Quota]": Quota,
        "HotelRoomQuotaItemDto[0][QuotaDate]": QuotaDate.strftime("%d.%m.%Y %H:%M:%S"),
        "HotelRoomQuotaItemDto[0][Deadline]": Deadline,
        "HotelRoomQuotaItemDto[0][HotelRoomQuotaSaleStatus]": SaleStatus,
    }

    # Send the POST request
    response = session.post(
        "https://extranet.jollytur.ws/HotelQuota/HotelRoomQuotaItemUpdate",
        headers=headers_quota,
        data=payload,
    )

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}")
