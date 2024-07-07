from typing import Optional
from fastapi import FastAPI, Query
from datetime import date

app = FastAPI()


@app.get("/hotels")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
):
    return "List of all hotels"


@app.get("/hotels/{hotel_id}")
def get_hotel(hotel_id: int):
    return hotel_id
