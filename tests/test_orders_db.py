from database.queries import get_order_by_id, get_order_product

def test_order_total_matches_product_price(database_connection):
    order = get_order_by_id(1,database_connection)
    # (1, 1, 29.99, 'completed')
    product = get_order_product(1,database_connection)
    assert order is not None
    assert product is not None
    order_total = order[2]
    product_total = product[3]
    quantity = product[2]

    expected_total = product_total * quantity
    assert order_total == expected_total