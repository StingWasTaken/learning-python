# Asynchronous programming in Python
##############################################
# Use asyncio for managing many waiting tasks
# Use threads for parallel tasks that share data with minimal cpu use
# Use processes for maximaxing performance on cpu intensive tasks

#Asyncio
# The event loop is the core of asyncio, it runs asynchronous tasks and callbacks, performs network IO operations, and runs subprocesses.
import asyncio

from asyncio import Coroutine


async def main() -> Coroutine:  # Usually, you would not specify the return type as Coroutine, but for clarity, we do it here.
    print("Start of main coroutine")
    

print(main())  # This prints the coroutine object, not the result of the coroutine.

# Because it's an asynchronous function, it returns a coroutine object when called.
# To run the coroutine, we need to use an event loop.
# The asyncio.run() function is a high-level API for running the main coroutine.

# Run the main coroutine
# This starts the event loop and runs the main coroutine until it completes.
asyncio.run(main())