import json
import requests

cookie = ""


def odoo_login():
    url = "http://localhost:8070/web/session/authenticate"
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


def send_datato_odoo_one_by_one():
    url = "http://localhost:8070/web/dataset/search_read"
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json",
        "Cookie": cookie,
    }
    myobj = {
        "id": 39,
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "model": "modem.profile",
            "domain": [["x_mac", "=", "1c:18:4a:5a:34:6F"]],
            "fields": [
                "name",
                "x_lostConnection",
                "x_site",
                "x_update_date",
                "x_uptime",
                "x_channel",
                "x_mac",
                "x_ip",
                "x_subnet",
                "x_gateway",
                "x_enable_wireless",
                "x_enable_ssid1",
                "x_ssid1",
                "x_passwd_1",
                "x_enable_ssid2",
                "x_ssid2",
                "x_passwd_2",
                "x_enable_ssid3",
                "x_ssid3",
                "x_passwd_3",
                "x_vlanId",
                "x_ram",
                "x_cpu",
                "x_disk",
                "x_firmwareVersion",
            ],
            "limit": 80,
            "sort": "",
            "context": {
                "lang": "en_US",
                "tz": "Europe/Istanbul",
                "uid": 2,
                "allowed_company_ids": [1],
                "params": {
                    "id": 24,
                    "cids": 1,
                    "menu_id": 111,
                    "action": 159,
                    "model": "modem.profile",
                    "view_type": "form",
                },
                "bin_size": True,
            },
        },
    }  # this will be filled with our data

    x = requests.post(url, json=myobj, headers=headers)

    print(x.text)


odoo_login()
send_datato_odoo_one_by_one()
