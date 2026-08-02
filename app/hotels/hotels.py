from typing import Optional
from datetime import date
from fastapi import APIRouter, Query, Depends

router = APIRouter(prefix="/hotels")


class HotelsSearchArgs:
    def __init__(self,
                 location: str,
                 date_from: date,
                 date_to: date,
                 has_spa: Optional[bool] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5)
                 ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@router.get("")
def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    return search_args


@router.get("/{hotel_id}")
def get_hotel(hotel_id: int):
    return hotel_id
