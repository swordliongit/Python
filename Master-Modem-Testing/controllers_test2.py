import requests
import json

url = "https://modem.nitrawork.com/create/create_or_update_record"

headers = {
    "authority": "modem.nitrawork.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,tr;q=0.8",
    "content-type": "application/json",
    "origin": "https://modem.nitrawork.com",
    "referer": "https://modem.nitrawork.com/web",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Cookie": "session_id=25ee2aad43e84758c4fd5ae3019a7880d03765f5",
}

raw_data = {
    "name": "test",
    "x_site": "artinsite",
    "x_uptime": "test",
    "x_channel": "test",
    "x_mac": "test",
    "x_device_info": "test",
    "x_ip": "test",
    "x_subnet": "test",
    "x_gateway": "test",
    "x_enable_wireless": False,
    "x_ssid1": "test",
    "x_passwd_1": False,
    "x_ssid2": False,
    "x_passwd_2": False,
    "x_ssid3": False,
    "x_passwd_3": False,
    "x_enable_ssid1": False,
    "x_enable_ssid2": False,
    "x_enable_ssid3": False,
    "x_lostConnection": False,
    "x_ram": False,
    "x_cpu": False,
    "x_disk": False,
    "x_log": False,
    "x_vlanId": "1",
    "x_lastTimeLogTrimmed": False,
    "x_monitor": False,
    "pra": True,
    "x_firmwareVersion": "0.9.9.7",
}

payload = json.dumps(raw_data)


response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
