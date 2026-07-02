from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_time(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    print(f"Time: {time.time() - start:.2f} seconds")

    return response


# Here:
# A request arrives.
# Middleware starts a timer.
# call_next(request) passes the request to the actual application (your AI endpoint).
# After the response comes back, the middleware logs how long it took.
# Finally, the response is sent back to the user.