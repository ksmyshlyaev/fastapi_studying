from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/bookings")


class BookingScheme(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@router.post("")
def add_booking(booking: BookingScheme):
    pass
