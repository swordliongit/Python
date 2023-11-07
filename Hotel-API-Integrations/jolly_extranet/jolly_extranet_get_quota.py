from functools import wraps
from datetime import datetime
from headers import headers_quota
from bs4 import BeautifulSoup
import requests
import re
import html

# Define a mapping between Hotel IDs, Room IDs, and Room Types
ROOM_MAPPING = {
    "14056": [
        {"RoomId": "38314", "RoomType": "Standart"},
        {"RoomId": "38315", "RoomType": "Family"},
    ],
    "4957": [
        {"RoomId": "9027", "RoomType": "Standart"},
    ],
    "11623": [{"RoomId": "28293", "RoomType": "Standart"}],
    "12008": [
        {"RoomId": "29864", "RoomType": "Ekonomik"},
        {"RoomId": "29865", "RoomType": "Standart"},
    ],
    "13083": [{"RoomId": "34463", "RoomType": "Standart"}],
}


def GetRooms(func):
    @wraps(func)
    def wrapper(session, HotelId, date, *args, **kwargs):
        # Get the corresponding room mappings based on the HotelId
        room_mappings = ROOM_MAPPING.get(HotelId, [])
        all_data = {}
        for room_mapping in room_mappings:
            room_id = room_mapping["RoomId"]
            room_data = func(
                session,
                room_id,
                HotelId,
                date,
                room_mapping["RoomType"],
                *args,
                **kwargs,
            )
            all_data[room_id] = room_data
        return all_data  # Return the accumulated data

    return wrapper


@GetRooms
def Get_Quota(
    session: requests.Session,
    HotelRoomId: str,
    HotelId: str,
    date: datetime,
    room_type: str,
):
    """_summary_
    Args:
        session (requests.Session): _description_
        HotelRoomId (str): _description_
        HotelId (str): _description_
        >>> 14056 -> Alexius Beach Hotel
        >>> 4957 -> Hotel Çamyuva Beach
        >>> 11623 -> Ares Blue Hotel
        >>> 12008 -> Emily Rose Hotel
        >>> 13083 -> Elamir Resort Hotel
        >>> ... -> Ares City
        date (datetime): _description_
        room_type (str): _description_

    Returns:
        _type_: _description_
    """
    payload = {
        "HotelId": HotelId,
        "HotelRoomId": HotelRoomId,
        "MarketId": "1",
        "ScopePath": "%2F",
        "Year": date.year,
        "MonthId": date.month,
    }

    # Send the POST request
    response = session.post(
        "https://extranet.jollytur.ws/HotelQuota/HotelRoomQuotaDetail",
        headers=headers_quota,
        data=payload,
    )

    if response.status_code == 200:
        html_response = response.text

        cleaned_html = html_response

        cleaned_html = re.sub(r"\n+", "", cleaned_html)
        cleaned_html = re.sub(r"\s+", " ", cleaned_html)
        cleaned_html = re.sub(r"\\+", "", cleaned_html)
        # Unescape special characters
        cleaned_html = html.unescape(cleaned_html)
        soup = BeautifulSoup(cleaned_html, "html.parser")
        # print(soup)
        # Extract data from the HTML
        data = []
        quota_columns = soup.find_all("div", class_="quotaColumn")

        for column in quota_columns:
            quota_date = column.find("div", class_="quotaBox quotaDate").text.strip()
            total_quota = column.find("div", class_="quotaBox total").text.strip()
            sold_quota = column.find("div", class_="quotaBox sold").text.strip()
            remaining_quota = column.find(
                "div", class_="quotaBox remaining"
            ).text.strip()
            deadline = column.find("div", class_="quotaBox deadline").text.strip()
            current_status = column.find(
                "div", class_="quotaBox currentStatus"
            ).text.strip()

            data.append(
                {
                    "Date": quota_date,
                    "Total Quota": total_quota,
                    "Sold Quota": sold_quota,
                    "Remaining Quota": remaining_quota,
                    "Deadline": deadline,
                    "Current Status": current_status,
                    "Room Id": HotelRoomId,
                    "Room Type": room_type,
                }
            )

        # Display the extracted data
        for entry in data:
            print(f'Date: {entry["Date"]}')
            print(f'Total Quota: {entry["Total Quota"]}')
            print(f'Sold Quota: {entry["Sold Quota"]}')
            print(f'Remaining Quota: {entry["Remaining Quota"]}')
            print(f'Deadline: {entry["Deadline"]}')
            print(f'Current Status: {entry["Current Status"]}')
            print(f'Room Id: {entry["Room Id"]}')
            print(f'Room Type: {entry["Room Type"]}')
            print("-" * 40)

        return data

    else:
        print(f"Request failed with status code {response.status_code}")
