from fastapi import FastAPI, status, HTTPException
from models import Id_queue
from database import sessionLocal
from psycopg2._psycopg import connection as PSQLConnection
import psycopg2

app = FastAPI()

con = psycopg2.connect("dbname=abo_Mohammed user=postgres password=123456")


def query2(query, parameter=(), db: PSQLConnection = con):
    cur = db.cursor()
    cur.callproc(query, parameter)
    row = cur.fetchone()
    cur.execute(f'FETCH ALL IN "{row[0]}"')
    results = cur.fetchall()
    db.close()
    return results

class Config:
    orm_mode = True


db = sessionLocal()


@app.get('/card_person/{id}')
def id_queue(id : str):
    try:
        result = query2("view_id_queue",[id], db=con)
        result_list = [Id_queue(card_id=i[1], civil_name=i[2], station_name=i[3], done=i[0]) for i in result]
        print(result)
        return {'view_id_queue': result_list}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
