import asyncio
import random

Stock = 0


async def producer():
    global Stock
    await asyncio.sleep(random.randint(1, 5))
    Stock += 1
    print(Stock)

async def consumer():
    global Stock
    await asyncio.sleep(random.randint(1, 5))
    Stock -= 1
    print(Stock)

async def main():
    producers = [asyncio.create_task(producer()) for _ in range(500)]
    consumers = [asyncio.create_task(consumer()) for _ in range(500)]
    await asyncio.gather(*producers, *consumers)

if __name__ == "__main__":
    asyncio.run(main())
    print(Stock)