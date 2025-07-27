from typing import Union
import sqlite3

from fastapi import FastAPI

class Customer:
    def __init__(self, first_name, last_name, email, phone, address, city, state, zip_code, registration_date, customer_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.registration_date = registration_date
        self.customer_type = customer_type

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

@app.post("/customer")
def create_customer(customer):
    stmt = "INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, registration_date, customer_type) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    connection = sqlite3.connect('business_data.db')
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    res = cur.execute(stmt, customer)
    customer_id = res.lastrowid
    connection.close()
    
    return {"customer_id": customer_id, "message": "Customer created successfully"}
    



