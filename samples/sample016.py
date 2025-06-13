# Asynchronous programming in Python : create_task
import asyncio
import time

# Define a couroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print(f"Data fetched, id: {id}")
    return {"data": "Some Data", "id": id} # Return some data


#Define another couroutine that calls the first coroutine
async def main():
    start = time.time()
    
    # If this ran synchrounously, it would takes 6 seconds to complete
    # But with asyncio, it runs concurrently and completes in ? seconds (you can guess it!)
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))
    
    result1 = await task1
    print(f"Result from task1: {result1}")
    result2 = await task2
    print(f"Result from task2: {result2}")
    result3 = await task3
    print(f"Result from task3: {result3}")
    
    elapsed = time.time() - start
    print(f"Results: {result1}, {result2}, {result3}")
    # It takes only 3 seconds to complete all tasks concurrently
    print(f"Total elapsed time: {elapsed:.2f} seconds") 
    
# Run the main coroutine
asyncio.run(main())
