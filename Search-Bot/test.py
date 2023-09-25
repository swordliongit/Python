import requests
import json

# Define the URL and headers
url = "https://www.setur.com.tr/api/services/v2/SearchesService/searchesHotel"
headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'referer': 'https://www.setur.com.tr/',
    }

proxies = {
        'http': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
        'https': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
    }

proxies_ovh =  {
            'http': "http://snapproxy:DsQWzRwjVM@188.165.56.45:3128",
            'https': "http://snapproxy:DsQWzRwjVM@188.165.56.45:3128",
        }

# Define the JSON data to send in the request body
data = {
    "args": [{"s": "linda"}]
}

# Convert the data to a JSON string
json_data = json.dumps(data)

session = requests.Session()

# Perform the POST request
response = session.post(url, headers=headers, data=json_data, proxies=proxies)

# Check the response
if response.status_code == 200:
    # Request was successful
    parsed_data = json.loads(response.content)
    print(parsed_data)
    # Process the parsed_data as needed
else:
    # Request failed
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for debugging
