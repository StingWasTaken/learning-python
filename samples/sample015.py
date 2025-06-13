# Asynchronous programming in Python
import asyncio

# Define a couroutine that simulates a time-consuming task
async def fetch_Data(delay, id):
    print(f"Fetching data... id: {id}")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data fetched, id: {id}")
    return {"data": "Some Data", "id": id} # Return some data


#Define another couroutine that calls the first coroutine
async def main():
    import time
    start = time.time()
    # Out of the box couroutines won't run in parallel, so this will takes 4 secodns to run
    result1 = await fetch_Data(2, 1)
    result2 = await fetch_Data(2, 2)
    elapsed = time.time() - start
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Total elapsed time: {elapsed:.2f} seconds")
    
    
# Run the main coroutine
asyncio.run(main())
