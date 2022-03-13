from fastapi import FastAPI, status, HTTPException
from psycopg2.extras import RealDictCursor

from models import s as model_s
from database import sessionLocal
from psycopg2._psycopg import connection as PSQLConnection
import uvicorn
import psycopg2

app = FastAPI()

con = psycopg2.connect("dbname=abo_Mohammed user=postgres password=123456")


def querytable(query, parameter=(), db: con = None):
        cur = db.cursor(cursor_factory=RealDictCursor)
        cur.callproc(query, parameter)
        results = cur.fetchall()
        con.commit()
        return results


class Config:
    orm_mode = True


db = sessionLocal()


@app.get('/card_person/{id}')
def id_queue(id: str):
    try:
        result = querytable("view_id_queue", [id], db=con)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.get('/card_record/{id}')
def id_queue(id: str):
    try:
        result = querytable("view_reception_queue_date", [id], db=con)
        return result

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error")
