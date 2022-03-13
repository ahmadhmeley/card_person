from datetime import time, date

from database import base
from pydantic import BaseModel


class s(BaseModel):
    card_id: str
    civil_name: str
    station_name: str
    done: bool


class reception_queue(BaseModel):
    record_id: str
    civil_name: str
    station_name: str
    civil_date: date
    start_at: time
    end_at: time
    times_num: str
    done: bool
