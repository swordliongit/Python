
import requests

base_url = "https://www.etstur.com/Otel/ajax/autocomplete"
search_terms = ["a", "r", "e", "s"]  # Include a space

proxies = {
    'http': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
    'https': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
    'Content-Type': 'application/json',
}

hotel_suggestions = set()

def generate_combinations(prefix, depth):
    if depth == 0:
        search_term = prefix.strip()  # Remove leading/trailing spaces
        params = {
            "pagetype": "SEARCH",
            "q": search_term
        }
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            suggestions = data.get("suggestions", [])
            hotel_suggestions.update((tuple(item.items()) for item in suggestions))
    else:
        for term in search_terms:
            generate_combinations(prefix + term, depth - 1)


def MassRequester():
    # Generate combinations of lengths from 1 to 3 (or any desired length)
    for length in range(1, 4):
        generate_combinations("", length)
        
    # Print the total list of hotel suggestions in JSON-like format
    turkey_hotels = []
    for suggestion in hotel_suggestions:
        formatted_suggestion = {
            item[0]: item[1] if isinstance(item[1], (str, int)) else item[1].get("name") if isinstance(item[1], dict) else None for item in suggestion
        }
        # Check if "country" is "Türkiye"
        if formatted_suggestion.get("country") == "Türkiye":
            turkey_hotels.append(formatted_suggestion)
            
    for hotel in turkey_hotels:
        print(hotel)

    print(len(turkey_hotels))
    
MassRequester()