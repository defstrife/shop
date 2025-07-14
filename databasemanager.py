import sqlite3
from typing import List, Optional, Tuple 

class DatabaseManager:
    def __init__(self, db_name: str = ":memory"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            price REAL NOT NULL
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );

        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            UNIQUE(order_id, product_id)
        );
        """)
        self.connection.commit()

    def add_customer(self, name: str, email: str) -> int:
        self.cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def add_product(self, title: str, price: float) -> int:
        self.cursor.execute("INSERT INTO products (title, price) VALUES (?, ?)", (title, price))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def add_order(self, customer_id: int) -> int:
        self.cursor.execute("INSERT INTO orders (customer_id) VALUES (?)", (customer_id,))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def add_order_item(self, order_id: int, product_id: int, quantity: int) -> int:
        self.cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, product_id, quantity))
        self.connection.commit()
        return self.cursor.lastrowid
    

    
    def get_customer_id(self) -> List[Tuple]:
        self.cursor.execute("SELECT id FROM customers")
        return self.cursor.fetchall()
    
    def get_customer_name(self) -> List[Tuple]:
        self.cursor.execute("SELECT name FROM customers")
        return self.cursor.fetchall()
    
    def get_customer_email(self) -> List[Tuple]:
        self.cursor.execute("SELECT email FROM customers")
        return self.cursor.fetchall()
    
    def get_product_id(self) -> List[Tuple]:
        self.cursor.execute("SELECT id FROM products")
        return self.cursor.fetchall()
    
    def get_product_title(self) -> List[Tuple]:
        self.cursor.execute("SELECT title FROM products")
        return self.cursor.fetchall()
    
    def get_product_price(self) -> List[Tuple]:
        self.cursor.execute("SELECT price FROM products")
        return self.cursor.fetchall()
    
    def get_order_id(self) -> List[Tuple]:
        self.cursor.execute("SELECT id FROM orders")
        return self.cursor.fetchall()
    
    def get_order_date(self) -> List[Tuple]:
        self.cursor.execute("SELECT order_date FROM orders")
        return self.cursor.fetchall()
    
    def get_order_item_id(self) -> List[Tuple]:
        self.cursor.execute("SELECT id FROM order_items")
        return self.cursor.fetchall()
    
    def get_customer1_info(self) -> List[Tuple]:
        self.cursor.execute(SELECT *
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id) 
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()