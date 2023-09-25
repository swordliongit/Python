import asyncio
import random

async def async_generator_1():
    for i in range(3):
        await asyncio.sleep(random.randint(0, 5))
        yield i*i

async def async_generator_2():
    for i in range(3):
        await asyncio.sleep(random.randint(0, 5))
        yield i*i*i

async def gen1_executor():
    async for i in async_generator_1():
        print(f"Generator 1: {i}")
        
async def gen2_executor():
    async for i in async_generator_2():
        print(f"Generator 2: {i}")

async def main():
    await asyncio.gather(gen1_executor(), gen2_executor())
        
if __name__ == "__main__":
    asyncio.run(main())