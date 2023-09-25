



import requests

def odoo_login():
    url = 'https://modem.nitrawork.com/web/session/authenticate'
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json"
    }
    myobj = {
        "jsonrpc": "2.0",
        "params": {
            "login": "admin",
            "password": "Artin.modem",
            "db": "modem"
        }
    }
    x = requests.post(url, json=myobj, headers=headers)
    global cookie
    cookie = ((x.headers)['Set-Cookie'])[0:51]

    print(cookie)

def Get():
    # need to check this for multiple databases position
    url = 'https://www.jollytur.com/Shared/Search?type=HotelPlanner&key=emily%20&_=1694593478310'
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json"
    }
    proxies = {
        'http': 'http://snapproxy:DsQWzRwjVM@89.43.67.180:3128',
        'https': 'http://snapproxy:DsQWzRwjVM@89.43.67.180:3128',
    }

    response = requests.post(url=url, headers=headers, proxies=proxies)
    print(response.text)
    

data = {"name":"sefsef","x_site":"DED","x_device_update":False,"x_update_date":"05-09-2023 14:50:17","x_uptime":False,"x_channel":False,"x_mac":"1c:18:4a:23:2f:6d","x_device_info":False,"x_ip":False,"x_subnet":False,"x_gateway":False,"x_upgrade":False,"x_new_password":False,"x_reboot":False,"x_enable_wireless":False,"x_enable_ssid1":False,"x_ssid1":False,"x_passwd_1":False,"x_enable_ssid2":False,"x_ssid2":False,"x_passwd_2":False,"x_enable_ssid3":False,"x_ssid3":False,"x_passwd_3":False,"x_enable_ssid4":False,"x_ssid4":False,"x_passwd_4":False}

Get()