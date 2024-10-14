import os
import json
import time
import asyncio
import aiohttp
from aiohttp import ClientSession
from urllib.parse import quote

# Load the TMDB API key from environment variable
TMDB_API_KEY = "0661914bcccd169542192e49a431b25e"

# Rate limiting parameters
MAX_REQUESTS_PER_SECOND = 40
DELAY_BETWEEN_REQUESTS = 1 / MAX_REQUESTS_PER_SECOND
MAX_CONCURRENT_REQUESTS = 40  # Adjust this based on your needs


async def get_metadata_from_tmdb(session, movie_title, semaphore, retries=3):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={quote(movie_title)}"
    async with semaphore:
        for attempt in range(retries):
            try:
                async with session.get(search_url) as response:
                    if response.status == 429:
                        # If we hit the rate limit, wait and retry
                        retry_after = int(response.headers.get("Retry-After", 1))
                        print(f"Rate limit exceeded, retrying after {retry_after} seconds")
                        await asyncio.sleep(retry_after)
                        continue
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                print(f"Error fetching data for {movie_title}: {e}")
                if attempt < retries - 1:
                    await asyncio.sleep(2**attempt)  # Exponential backoff
                else:
                    print(f"Failed to fetch data for {movie_title} after {retries} attempts")
                    return None
            await asyncio.sleep(DELAY_BETWEEN_REQUESTS)


def parse_m3u_file(m3u_file_path):
    with open(m3u_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    movie_titles = []
    for line in lines[:25000]:  # Only process the first 100 lines
        if line.startswith('#EXTINF'):
            title = line.split(',')[1].strip()
            movie_titles.append(title)
    return movie_titles


async def main():
    m3u_file_path = 'list.m3u'
    movie_titles = parse_m3u_file(m3u_file_path)

    metadata_list = []
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with ClientSession() as session:
        tasks = [get_metadata_from_tmdb(session, title, semaphore) for title in movie_titles]
        metadata_results = await asyncio.gather(*tasks)
        for metadata in metadata_results:
            if metadata:
                metadata_list.append(metadata)

    with open('movie_metadata.json', 'w', encoding='utf-8') as outfile:
        json.dump(metadata_list, outfile, indent=4)


if __name__ == '__main__':
    asyncio.run(main())
