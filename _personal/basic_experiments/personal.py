import requests
import json

url = "https://dd.swordlion.org/dd/log_status"

payload = json.dumps({
  "trigger": True
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'frontend_lang=en_US; session_id=cb0ff9827c4a8a8a3ff8bb9b37bd14b17a950e33'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
