import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

def create_database():
    """Create SQLite database and tables"""
    conn = sqlite3.connect('business_data.db')
    cursor = conn.cursor()
    
    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            registration_date DATE,
            customer_type TEXT CHECK(customer_type IN ('Individual', 'Business'))
        )
    ''')
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            cost DECIMAL(10,2) NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            supplier TEXT,
            description TEXT
        )
    ''')
    
    # Create Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            department TEXT,
            position TEXT,
            salary DECIMAL(10,2),
            hire_date DATE,
            status TEXT CHECK(status IN ('Active', 'Inactive', 'On Leave'))
        )
    ''')
    
    # Create Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            employee_id INTEGER,
            order_date DATE NOT NULL,
            total_amount DECIMAL(10,2) NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')),
            shipping_address TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        )
    ''')
    
    # Create Order Items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (order_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        )
    ''')
    
    conn.commit()
    return conn

def populate_customers(cursor, num_customers=100):
    """Populate customers table with sample data"""
    customer_types = ['Individual', 'Business']
    
    for _ in range(num_customers):
        cursor.execute('''
            INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, registration_date, customer_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            fake.first_name(),
            fake.last_name(),
            fake.unique.email(),
            fake.phone_number(),
            fake.street_address(),
            fake.city(),
            fake.state_abbr(),
            fake.zipcode(),
            fake.date_between(start_date='-2y', end_date='today'),
            random.choice(customer_types)
        ))

def populate_products(cursor, num_products=50):
    """Populate products table with sample data"""
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Toys', 'Health & Beauty']
    suppliers = ['TechCorp', 'FashionInc', 'HomeSupply', 'SportsPro', 'BookWorld', 'ToyFactory', 'BeautyPlus']
    
    for _ in range(num_products):
        cost = round(random.uniform(5, 200), 2)
        price = round(cost * random.uniform(1.2, 3.0), 2)  # Markup between 20% and 200%
        
        cursor.execute('''
            INSERT INTO products (product_name, category, price, cost, stock_quantity, supplier, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            fake.catch_phrase(),
            random.choice(categories),
            price,
            cost,
            random.randint(0, 500),
            random.choice(suppliers),
            fake.text(max_nb_chars=200)
        ))

def populate_employees(cursor, num_employees=25):
    """Populate employees table with sample data"""
    departments = ['Sales', 'Marketing', 'IT', 'HR', 'Finance', 'Operations', 'Customer Service']
    positions = ['Manager', 'Specialist', 'Coordinator', 'Analyst', 'Representative', 'Director', 'Associate']
    statuses = ['Active', 'Inactive', 'On Leave']
    
    for _ in range(num_employees):
        cursor.execute('''
            INSERT INTO employees (first_name, last_name, email, phone, department, position, salary, hire_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            fake.first_name(),
            fake.last_name(),
            fake.unique.email(),
            fake.phone_number(),
            random.choice(departments),
            random.choice(positions),
            round(random.uniform(35000, 120000), 2),
            fake.date_between(start_date='-5y', end_date='today'),
            random.choice(statuses)
        ))

def populate_orders_and_items(cursor, num_orders=200):
    """Populate orders and order_items tables with sample data"""
    # Get customer and employee IDs
    cursor.execute('SELECT customer_id FROM customers')
    customer_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute('SELECT employee_id FROM employees WHERE status = "Active"')
    employee_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute('SELECT product_id, price FROM products')
    products = cursor.fetchall()
    
    statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
    
    for _ in range(num_orders):
        customer_id = random.choice(customer_ids)
        employee_id = random.choice(employee_ids)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        status = random.choice(statuses)
        
        # Insert order
        cursor.execute('''
            INSERT INTO orders (customer_id, employee_id, order_date, total_amount, status, shipping_address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            customer_id,
            employee_id,
            order_date,
            0,  # Will update after calculating total
            status,
            fake.address()
        ))
        
        order_id = cursor.lastrowid
        total_amount = 0
        
        # Add 1-5 items to each order
        num_items = random.randint(1, 5)
        selected_products = random.sample(products, min(num_items, len(products)))
        
        for product_id, price in selected_products:
            quantity = random.randint(1, 3)
            unit_price = price
            item_total = quantity * unit_price
            total_amount += item_total
            
            cursor.execute('''
                INSERT INTO order_items (order_id, product_id, quantity, unit_price)
                VALUES (?, ?, ?, ?)
            ''', (order_id, product_id, quantity, unit_price))
        
        # Update order total
        cursor.execute('UPDATE orders SET total_amount = ? WHERE order_id = ?', (total_amount, order_id))

def generate_business_reports(cursor):
    """Generate some basic business reports"""
    print("\n=== BUSINESS REPORTS ===\n")
    
    # Sales by month
    print("1. Monthly Sales Summary:")
    cursor.execute('''
        SELECT strftime('%Y-%m', order_date) as month, 
               COUNT(*) as order_count,
               ROUND(SUM(total_amount), 2) as total_sales
        FROM orders 
        WHERE status != 'Cancelled'
        GROUP BY strftime('%Y-%m', order_date)
        ORDER BY month DESC
        LIMIT 6
    ''')
    
    print("Month\t\tOrders\tTotal Sales")
    print("-" * 35)
    for row in cursor.fetchall():
        print(f"{row[0]}\t{row[1]}\t${row[2]:,.2f}")
    
    # Top selling products
    print("\n2. Top 5 Selling Products:")
    cursor.execute('''
        SELECT p.product_name, 
               SUM(oi.quantity) as total_sold,
               ROUND(SUM(oi.quantity * oi.unit_price), 2) as revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN orders o ON oi.order_id = o.order_id
        WHERE o.status != 'Cancelled'
        GROUP BY p.product_id, p.product_name
        ORDER BY total_sold DESC
        LIMIT 5
    ''')
    
    print("Product\t\t\t\tQty Sold\tRevenue")
    print("-" * 50)
    for row in cursor.fetchall():
        product_name = row[0][:25] + "..." if len(row[0]) > 25 else row[0]
        print(f"{product_name:<28}\t{row[1]}\t${row[2]:,.2f}")
    
    # Employee performance
    print("\n3. Employee Sales Performance:")
    cursor.execute('''
        SELECT e.first_name || ' ' || e.last_name as employee_name,
               COUNT(o.order_id) as orders_processed,
               ROUND(SUM(o.total_amount), 2) as total_sales
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        WHERE o.status != 'Cancelled' AND e.status = 'Active'
        GROUP BY e.employee_id, employee_name
        ORDER BY total_sales DESC
        LIMIT 5
    ''')
    
    print("Employee\t\t\tOrders\tTotal Sales")
    print("-" * 45)
    for row in cursor.fetchall():
        print(f"{row[0]:<20}\t{row[1]}\t${row[2]:,.2f}")

def main():
    """Main function to create and populate the database"""
    print("Creating business database...")
    
    # Create database and tables
    conn = create_database()
    cursor = conn.cursor()
    
    print("Populating tables with sample data...")
    
    # Populate tables
    populate_customers(cursor, 100)
    print("✓ Added 100 customers")
    
    populate_products(cursor, 50)
    print("✓ Added 50 products")
    
    populate_employees(cursor, 25)
    print("✓ Added 25 employees")
    
    populate_orders_and_items(cursor, 200)
    print("✓ Added 200 orders with items")
    
    conn.commit()
    
    # Generate reports
    generate_business_reports(cursor)
    
    # Show table counts
    print(f"\n=== DATABASE SUMMARY ===")
    tables = ['customers', 'products', 'employees', 'orders', 'order_items']
    for table in tables:
        cursor.execute(f'SELECT COUNT(*) FROM {table}')
        count = cursor.fetchone()[0]
        print(f"{table.capitalize()}: {count} records")
    
    conn.close()
    print(f"\nDatabase 'business_data.db' created successfully!")
    print("You can now connect to it using any SQLite client or Python sqlite3 module.")

if __name__ == "__main__":
    main()