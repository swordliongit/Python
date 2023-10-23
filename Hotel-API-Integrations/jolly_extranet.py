import ast
from datetime import datetime
import re
from pyquery import PyQuery as pq
import requests

from bs4 import BeautifulSoup
import html

headers = {
    "authority": "extranet.jollytur.ws",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "tr,en-US;q=0.9,en;q=0.8,ru;q=0.7",
    "referer": "https://extranet.jollytur.ws/",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

headers2 = {
    "authority": "identity.jollytur.ws",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "tr",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://identity.jollytur.ws",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

headers3 = {
    "authority": "extranet.jollytur.ws",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "tr,en-US;q=0.9,en;q=0.8,ru;q=0.7",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "null",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

headers4 = {
    "authority": "extranet.jollytur.ws",
    "accept": "*/*",
    "accept-language": "tr,en-US;q=0.9,en;q=0.8,ru;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://extranet.jollytur.ws",
    "referer": "https://extranet.jollytur.ws/HotelReservation",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "ui-request-type": "html",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

headers_quota = {
    "authority": "extranet.jollytur.ws",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,tr;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "cookie": "your-cookie-data-here",  # Add your cookie data
    "origin": "https://extranet.jollytur.ws",
    "referer": "https://extranet.jollytur.ws/HotelQuota",
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "ui-request-type": "html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}


def jollyextranet_login(session):
    login_page = session.get("https://extranet.jollytur.ws/Dashboard", headers=headers)
    login_result = pq(login_page.content.decode("utf-8"))
    token = login_result.find('input[name="__RequestVerificationToken"]').attr("value")
    return_url = login_result.find('input[name="ReturnUrl"]').attr("value")

    data = {
        "ReturnUrl": return_url,
        "ScopeCode": "PEN333",
        "Username": "kanal@snapturizm.com.tr",
        "Password": "snap23",
        "LanguageId": "1",
        "__RequestVerificationToken": token,
        "RememberLogin": "false",
    }

    login_post = session.post(login_page.url, headers=headers2, data=data)

    login_param = pq(login_post.content.decode("utf-8"))

    data = {
        "code": login_param.find('input[name="code"]').attr("value"),
        "id_token": login_param.find('input[name="id_token"]').attr("value"),
        "scope": "openid email profile corporate_profile offline_access",
        "state": login_param.find('input[name="state"]').attr("value"),
        "session_state": login_param.find('input[name="session_state"]').attr("value"),
    }

    session.post(
        "https://extranet.jollytur.ws/signin-oidc", headers=headers3, data=data
    )

    return session


def jollyextranet_search(session):
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


def jollyextranet_Get_Quota(
    session: requests.Session, HotelId: str, HotelRoomId: str, date: datetime
):
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
            print("-" * 40)

    else:
        print(f"Request failed with status code {response.status_code}")


def jollyextranet_Update_Quota(
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


def main():
    s = requests.Session()
    s = jollyextranet_login(s)

    jollyextranet_search(s)

    # Get Rooms
    jollyextranet_Get_Quota(
        s, HotelId="14056", HotelRoomId="38315", date=datetime(2023, 10, 1)
    )

    # Update Quota ( Start, Stop )
    jollyextranet_Update_Quota(
        s,
        HotelRoomId="38315",
        Quota=5,
        QuotaDate=datetime(2023, 10, 31),
        Deadline=0,
        SaleStatus=0,
    )


if __name__ == "__main__":
    main()
