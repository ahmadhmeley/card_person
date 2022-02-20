from datetime import time , date

from database import base
from pydantic import BaseModel


class Id_queue(BaseModel):
    card_id: str
    civil_name: str
    station_name: str
    done: bool


class reception_queue(BaseModel):
    card_id: int
    civil_name: str
    station_name: str
    civil_date: date
    start_at: time
    end_at: time
    times_num: int
    done: bool
