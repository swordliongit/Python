import requests

# Replace 'YOUR_TMDB_API_KEY' with your actual TMDB API key
api_key = '0661914bcccd169542192e49a431b25e'


def search_series(series_name):
    url = f'https://api.themoviedb.org/3/search/tv?api_key={api_key}&query={series_name}'
    response = requests.get(url)

    # Check for a successful response
    if response.status_code == 200:
        try:
            data = response.json()
            if data['results']:
                return data['results'][0]  # Return the first matching series
            else:
                return None
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None


def get_series_details(series_id):
    url = f'https://api.themoviedb.org/3/tv/{series_id}?api_key={api_key}'
    response = requests.get(url)

    # Check for a successful response
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None


def get_episodes(series_id, season_number):
    url = f'https://api.themoviedb.org/3/tv/{series_id}/season/{season_number}?api_key={api_key}'
    response = requests.get(url)

    # Check for a successful response
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None


# Example usage
series_name = 'Kukuli'  # Replace with the series name you want to search
series = search_series(series_name)

if series:
    print(f"Found series: {series['name']} (ID: {series['id']})")
    series_details = get_series_details(series['id'])

    if series_details:
        # Get all seasons
        seasons = series_details.get('seasons', [])
        for season in seasons:
            season_number = season['season_number']
            episodes = get_episodes(series['id'], season_number)
            if episodes:
                print(f"Season {season_number}:")
                for episode in episodes['episodes']:
                    print(f"  Episode {episode['episode_number']}: {episode['name']}")
else:
    print("Series not found.")
