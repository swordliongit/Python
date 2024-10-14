from tmdbv3api import TMDb, Movie
import asyncio
import json

# Initialize TMDb
tmdb = TMDb()
tmdb.api_key = '0661914bcccd169542192e49a431b25e'
tmdb.language = 'en'
tmdb.debug = True

# Initialize Movie object
movie = Movie()


def extract_titles_from_m3u(file_path, limit=1000):
    titles = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#EXTINF:") and len(titles) < limit:
                # Extract title part
                title = line.split(",")[1].strip()
                titles.append(title)
            if len(titles) >= limit:
                break
    return titles


async def fetch_movie_data(movie_title):
    search_result = movie.search(movie_title)
    if not search_result or len(search_result) == 0:
        print(f"No results found for: {movie_title}")
        return None

    # Print the search result to understand its structure
    print(f"Search result for '{movie_title}': {search_result}")

    movie_id = search_result[0].id
    movie_details = movie.details(movie_id)
    return {
        'title': movie_details.title,
        'id': movie_id,
        'summary': movie_details.overview,
        'thumbnail': movie_details.poster_path,
    }


async def process_movies(movie_titles):
    tasks = [fetch_movie_data(title) for title in movie_titles]
    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]


def save_results_to_file(results, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


# Example usage
file_path = 'list.m3u'
output_file_path = 'output_file.json'
movie_titles = extract_titles_from_m3u(file_path, limit=100)
result = asyncio.run(process_movies(movie_titles))

# Save results to file
save_results_to_file(result, output_file_path)

print(f"Results saved to {output_file_path}")
