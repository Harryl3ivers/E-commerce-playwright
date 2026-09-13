from database.connection import get_connection

def get_product_by_name(product_name):
    connection  = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE NAME = ?",(product_name,))
    product = cursor.fetchone()
    connection.close()
    return product

def get_product_by_price(product_name):
    connection  = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT price from products WHERE NAME = ?",(product_name,))
    product = cursor.fetchone()
    connection.close()
    return product

def get_order_by_id(order_id):
    connection  = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?",(order_id,))
    order = cursor.fetchone()
    connection.close()
    return order

def get_order_product(order_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT orders.id,products.name,order_items.quantity,order_items.price
    FROM orders 
    JOIN order_items ON orders.id = order_items.order_id
    JOIN products ON order_items.product_id = products.id
    WHERE orders.id = ?""",(order_id))
    order_product = cursor.fetchone
    connection.close()
    return order_product