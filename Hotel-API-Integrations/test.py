import requests

url = "https://extranet.jollytur.ws/HotelPrice/HotelPrice"

payload = {}
headers = {
    "authority": "extranet.jollytur.ws",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,tr;q=0.8",
    "cookie": "..Extranet.Cookies=CfDJ8PsoeErJew1MrsMrjL_wQwuwuaRycJY6paJmVOk1Jzdd5evO8Npe1e5dHRkZ0CElo_85u5mB9U3ycNg0sSgZkneDkm8dvEPRkwlX2nwSmETG9Abo2BfVEpJO99M256ggOIbTPkMUyPnkTIkAZU-qEuKHxA5X3Bs_XaCK9ZwFYuYnGumGgMpH5mc2yI9a5tsOaDcOq0GHpx83mgie5WrFqNubpkhIbTujs36detRLWvEY0QA5coBu3J0v_BaG71k_vDIU-wiqEUp3jc2tt5tCjZE0ImnP7XaJfJ-5TZgDd6yxOJv_z0-OVldYKDXd4CzBaA; ..Extranet.Session=CfDJ8PsoeErJew1MrsMrjL%2FwQwtu3uxEYub6yGMCkKMNeZWK9tP7Vxtob01it9v23fQu3LkeFuhp0wiuwdhXQ22RaPLJjaCd16yRIWLa09G3hoa6c3lw2VVKILwd%2F%2FsBTysWCGbSC3PxzUPBexRI25gpZgO01eMHJnMLq0SIl2bGz9tR",
    "referer": "https://extranet.jollytur.ws/HotelReservation",
    "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
