import uvicorn
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

from hotels.hotels import router as router_hotels

app = FastAPI()

app.include_router(router_hotels)


class BookingScheme(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: BookingScheme):
    pass
