import time
import asyncio
from aiohttp import ClientSession
from requests.exceptions import HTTPError


URLS = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1,101)]
RESULTS = []


async def get(url, session):
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
        # print(f"Response status ({url}): {response.status}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


async def run_program(url, session):
    try:
        response = await get(url, session)
        RESULTS.append(response)
    except Exception as err:
        print(f"Exception occured: {err}")
        pass


async def main():
    async with ClientSession() as session:
        await asyncio.gather(*[run_program(url, session) for url in URLS])


s = time.perf_counter()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

elapsed = time.perf_counter() - s

print(f"Completed {len(URLS)} requests with {len(RESULTS)} results")
print(elapsed)