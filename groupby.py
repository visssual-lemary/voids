import sqlite3

stmt = "SELECT customer_type, Count(*) AS total FROM customers GROUP BY customer_type"
connection = sqlite3.connect('business_data.db')
connection.row_factory = sqlite3.Row
cur = connection.cursor()
res = cur.execute(stmt)
# connection.commit()
for row in res:
    print(dict(row))
connection.close()



