# Async Programming
import asyncio
import time


async def fetch_data(delay, data_id):  # type:ignore
    print(f"Fetching data {data_id}...")
    await asyncio.sleep(delay)  # Simulate I/O bound operation #type:ignore
    print(f"Finished fetching data {data_id}.")
    return f"Data {data_id} after {delay} seconds"


async def main():
    start_time = time.time()
    task1 = asyncio.create_task(fetch_data(2, "A"))
    task2 = asyncio.create_task(fetch_data(1, "B"))
    task3 = asyncio.create_task(fetch_data(3, "C"))

    results = await asyncio.gather(task1, task2, task3)
    print("All data fetched:")
    for res in results:
        print(res)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
