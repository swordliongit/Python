


import requests
import datetime
import json
import requests

PAXIMUM_ID = 100826

def H2S_Login():
    user = "ARTIN_TP"
    passw = "RQUJFZAH"
    
    response = requests.get(
                url=f"https://admin.hotel2sejour.com/api/system/login?user={user}&pass={passw}"
            )
    cookie = json.loads(response.content)
    return cookie

def H2S_Push(cookie):
    
    url = "https://admin.hotel2sejour.com/api/pax/pushreservationsforthirdparty"
    
    headers = {
        "cookie": cookie
    }
    
    params = {
        'Hotel': "H2S",
        'HotelName': "H2S Test Hotel",
        'Region': "AYT",
        'HotelPaximumID': 100826,
        'DatabaseName': "ARTINSYSTEMS",
        "UniqueID": 1,
        "UserName": "ARTIN_TP"
    }
    
    response = requests.post(url, json=params, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Request was successful.")
    else:
        print(f"Request failed with status code {response.status_code}:")
        print(response.text)    
 

def main():
    
    cookie = H2S_Login()
    
    # H2S_Push(cookie)
    H2S_Push(cookie)
    

main()