# Asynchronous programming: Task Groups
import asyncio
import time

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulate an I/O operation with a sleep
    # REturn some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    start = time.time()
    tasks = []
    
    # async with create an asynchronous context manager that allows us to run multiple coroutines concurrently
    async with asyncio.TaskGroup() as tg:
        # Create tasks for each coroutine
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
            
    # After the Task Group block, all the tasks have completed
    results = [task.result() for task in tasks]
    
    for result in results:
        print(f"Result from coroutine {result['id']}: {result['data']}")
        
    elapsed = time.time() - start
    print(f"Total elapsed time: {elapsed:.2f} seconds") 
    
# Run the main coroutine
asyncio.run(main())