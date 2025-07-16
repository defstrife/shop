import databasemanager

db_manager = databasemanager.DatabaseManager("shop.db")

customer_id = db_manager.add_customer("Customer1", "customer1@mail.ru")
product_id = db_manager.add_product("Laptop", 999.99)
order_id = db_manager.add_order(customer_id)
db_manager.add_order_item(order_id, product_id, 1)

# print("Customers:", db_manager.get_customers())
# print()
# print("Products:", db_manager.get_products())
# print()
# print("Orders:", db_manager.get_orders())
# print()
# print("Order items:", db_manager.get_order_items())
print("Orders by customer:", db_manager.get_orders_by_customer(1))

db_manager.close()