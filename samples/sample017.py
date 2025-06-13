# Asynchronous programming: gather
import asyncio
import time

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulate an I/O operation with a sleep
    # REturn some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    start = time.time()
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    )
    
    for result in results:
        print(f"Result from coroutine {result['id']}: {result['data']}")
        
    # Gather  allows us to run multiple coroutines concurrently and wait for all of them to complete.
    # The drawnback is that if one coroutine fails,it won't cancell the other coroutines.
    
    elapsed = time.time() - start
    print(f"Total elapsed time: {elapsed:.2f} seconds")     
    
# Run the main coroutine
asyncio.run(main())