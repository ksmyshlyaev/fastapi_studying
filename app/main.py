import uvicorn
from fastapi import FastAPI

from bookings.bookings import router as router_bookings
from hotels.hotels import router as router_hotels

app = FastAPI()

app.include_router(router_hotels)
app.include_router(router_bookings)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
