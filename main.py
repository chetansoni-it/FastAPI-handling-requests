# main.py
from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Sequential Method
@app.get("/1")
async def endpoint1():
    print("Hello")
    # Blocking I/O Operation: Pauses the function execution for 5 seconds.
    # The function cannot be awaited, so the event loop is blocked during this period.
    time.sleep(5)
    print("bye")
    # This endpoint does not contain any non-blocking I/O operations.
    # Requests to this endpoint are processed sequentially. If multiple requests
    # are made, each one is processed only after the previous one is fully completed.

# Concurrent Method
@app.get("/2")
async def endpoint2():
    print("Hello")
    # Non-Blocking I/O Operation: Pauses the function execution for 5 seconds.
    # Unlike time.sleep, this can be awaited, allowing other tasks to be processed
    # during the wait time.
    await asyncio.sleep(5)
    print("bye")
    # This endpoint contains a non-blocking I/O operation (asyncio.sleep).
    # Multiple requests to this endpoint can be handled concurrently,
    # meaning they can be processed simultaneously during I/O operations.

# Parallel Method
@app.get("/3")
def endpoint3():
    print("Hello")
    # Blocking I/O Operation: Pauses the function execution for 5 seconds.
    # As a normal function, it runs in a separate thread from the main event loop.
    time.sleep(5)
    print("bye")
    # This endpoint is defined as a normal function.
    # Requests to this endpoint are handled in parallel using separate threads.
    # Each request is processed independently in its own thread, allowing multiple
    # requests to be processed at the same time.

