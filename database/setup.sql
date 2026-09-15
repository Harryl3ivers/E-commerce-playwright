CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);


CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price float NOT NULL
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total float NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price float NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);

INSERT INTO users(id,username,first_name,last_name)
VALUES (1,"standard_user","Noah","Shaw");

INSERT INTO products(id,name,price)
VALUES(1, 'Sauce Labs Backpack', 29.99);

INSERT INTO products (id, name, price)
VALUES (2, 'Sauce Labs Bike Light', 9.99);

INSERT INTO products (id, name, price)
VALUES (3, "Sauce Labs Onesie",7.99);

INSERT INTO orders(id,user_id,total,status)
VALUES(1,1,29.99,"completed");

INSERT INTO order_items(id,order_id,product_id,quantity,price)
VALUES(1,1,1,1,29.99);