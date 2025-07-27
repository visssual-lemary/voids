from typing import Union
import sqlite3
import datetime

from fastapi import FastAPI

from pydantic import BaseModel

class Customer(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip_code: str
    registration_date: datetime.date
    customer_type: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Leslie"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/customers")
def read_customers():
    connection = sqlite3.connect('business_data.db')
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    res = cur.execute("SELECT * FROM customers")
    result = res.fetchall()
    connection.close()
    return result

    

    



