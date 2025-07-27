import sqlite3
import datetime


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

        
        
stmt = "INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, registration_date, customer_type) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
customer = Customer(first_name= "Hallo", last_name= "Voids", email= "seeyousoon@zoom.de", phone= "01010101010", address= "wonderland", city= "wo", state= "allesmöglich", zip_code= "ist", registration_date= datetime.datetime.now(), customer_type= "Individual")
connection = sqlite3.connect('business_data.db')
connection.row_factory = sqlite3.Row
cur = connection.cursor()
res = cur.execute(stmt, (
    customer.first_name,
    customer.last_name,
    customer.email,
    customer.phone,
    customer.address,
    customer.city,
    customer.state,
    customer.zip_code,
    customer.registration_date.isoformat(),
    customer.customer_type
))
customer_id = res.lastrowid
connection.commit()
connection.close()
print (customer_id)

