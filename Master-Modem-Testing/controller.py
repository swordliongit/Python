import json
import requests

cookie = ""


def odoo_login():
    url = "http://89.252.165.116:8069/web/session/authenticate"
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json",
    }
    myobj = {
        "jsonrpc": "2.0",
        "params": {"login": "admin", "password": "Artin.modem", "db": "modem"},
    }
    x = requests.post(url, json=myobj, headers=headers)
    global cookie
    cookie = ((x.headers)["Set-Cookie"])[0:51]

    print(cookie)


def odooPost():
    global cookie
    # need to check this for multiple databases position
    url = "http://89.252.165.116:8069/create/create_or_update_record"
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
        "Cookie": cookie,
    }

    modem_data = {
        "name": "test",
        "x_site": "artinsite",
        "x_uptime": "test",
        "x_channel": "test",
        "x_mac": "test2",
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
        "x_log": "sadasdasdasdasda",
        "x_vlanId": "1",
        "x_lastTimeLogTrimmed": False,
        "x_monitor": "asdadsadas",
        "pra": True,
        "x_firmwareVersion": "0.9.9.7",
    }

    payload = json.dumps(modem_data)

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)


odoo_login()
odooPost()
