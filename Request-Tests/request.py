import requests

import json

url = "https://panel.xsarj.com/led/get_action"

payload = json.dumps({"master_mac": "8C:CE:4E:8C:64:44"})
headers = {
    'Content-Type': 'application/json',
    # 'Cookie': 'frontend_lang=en_US; session_id=cb0ff9827c4a8a8a3ff8bb9b37bd14b17a950e33',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
