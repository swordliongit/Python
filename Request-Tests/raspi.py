import requests

cookies = {
    'session_id': '234f2161ef07c4dda12d70a18495c0cd5b31b057',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'api_key': '0d8dd2dc1c8f7a47d5c5',
    'username': 'calimeraapi@artinwifi.com',
    'password': 'x13161918a',
    'survey_id': '227',
    'limit': '50',
    'start_date': '2024-07-01 15:24:45',
    'end_date': '2024-07-30 15:24:45',
}

response = requests.post('https://hs.artinwifi.com/api/survey/input', cookies=cookies, headers=headers, data=data)

print(response.json())
