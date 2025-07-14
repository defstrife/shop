import databasemanager

db_manager = databasemanager.DatabaseManager("shop.db")

customer_id = db_manager.add_customer("Customer1", "customer1@mail.ru")
product_id = db_manager.add_product("Laptop", 999.99)
order_id = db_manager.add_order(customer_id)
db_manager.add_order_item(order_id, product_id, 1)

print("Customer id:", db_manager.get_customer_id())
print("Customer name:", db_manager.get_customer_name())
print("Customer email:", db_manager.get_customer_email())
print("Product id:", db_manager.get_product_id())
print("Product title:", db_manager.get_product_title())
print("Product price:", db_manager.get_product_price())
print("Order id:", db_manager.get_order_id())
print("Order date:", db_manager.get_order_date())
print("Order item id:", db_manager.get_order_item_id())
print("Customer1 info:", db_manager.get_customer1_info())

db_manager.close()