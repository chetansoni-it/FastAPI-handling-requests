# FastAPI Endpoint Behavior Explanation

This README explains the behavior of different FastAPI endpoints and how they handle requests based on their implementation. We will cover sequential, concurrent, and parallel request handling methods.

## Youtube link
> https://www.youtube.com/watch?v=tGD3653BrZ8
## Explanation of the Concepts in the Code

The code defines three endpoints in FastAPI, each demonstrating a different method of handling requests:

1. **Sequential Method**:
    - **Endpoint**: `/1`
    - **Function**: `endpoint1`
    - **Behavior**: This function uses `time.sleep(5)`, which is a blocking I/O operation. When a request is made to this endpoint, the function execution is halted for 5 seconds. Since this is a blocking operation, the event loop cannot process any other requests or tasks during this time.
    - **Result**: Requests to this endpoint are processed sequentially. If multiple requests are made, each one will only start processing after the previous request has been fully completed.

2. **Concurrent Method**:
    - **Endpoint**: `/2`
    - **Function**: `endpoint2`
    - **Behavior**: This function uses `await asyncio.sleep(5)`, a non-blocking I/O operation. This allows the function to pause for 5 seconds without blocking the event loop, which can continue processing other tasks or requests.
    - **Result**: Multiple requests to this endpoint can be handled concurrently, meaning they can overlap in time. While one request is waiting for the non-blocking operation to complete, other requests can be processed simultaneously.

3. **Parallel Method**:
    - **Endpoint**: `/3`
    - **Function**: `endpoint3`
    - **Behavior**: This function uses `time.sleep(5)` like in the sequential method, but it is defined as a normal function (not a coroutine). Each request to this endpoint runs in its own thread, separate from the main event loop.
    - **Result**: Requests to this endpoint are handled in parallel, with each request being processed independently in its own thread. This allows multiple requests to be processed at the same time without waiting for each other.

## Key Points

### Blocking vs. Non-Blocking I/O:

- **Blocking I/O**:
    - Operations like `time.sleep` that halt the function execution and prevent any other operations from being processed until they are completed.
    - Example: `time.sleep(5)` blocks the function for 5 seconds.
    
- **Non-Blocking I/O**:
    - Operations like `await asyncio.sleep` that pause the function execution but allow the event loop to continue processing other tasks.
    - Example: `await asyncio.sleep(5)` allows the event loop to handle other tasks during the 5-second wait.

### Request Handling Methods:

- **Sequential Processing**:
    - Requests are processed one after another.
    - Each request waits for the previous one to finish before starting.
    - Example: Endpoint `/1` processes requests sequentially due to the blocking `time.sleep`.

- **Concurrent Processing**:
    - Requests are processed in a manner that allows them to overlap in time.
    - Utilizes non-blocking operations to handle multiple requests simultaneously.
    - Example: Endpoint `/2` handles requests concurrently using `await asyncio.sleep`.

- **Parallel Processing**:
    - Requests are processed independently in separate threads.
    - Allows multiple requests to be handled at the same time without blocking each other.
    - Example: Endpoint `/3` processes requests in parallel with each request running in a different thread.

### Best Practices:

- Use `async def` for endpoints involving non-blocking I/O operations, such as database queries or external API calls.
- Avoid using `async def` for endpoints with blocking I/O operations to prevent blocking the event loop.
- Use normal functions (`def`) for endpoints with blocking I/O operations to leverage threading and handle requests in parallel.

This README provides a comprehensive understanding of how different request handling methods work in FastAPI and the scenarios where each method is appropriate.

---

Feel free to update or modify this file as needed to better fit your project's documentation style.
