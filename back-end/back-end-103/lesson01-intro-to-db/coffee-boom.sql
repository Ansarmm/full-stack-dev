CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    product_description VARCHAR(300),
    price INTEGER,
    category VARCHAR(50),
    product_status VARCHAR(15),
    created_at DATE
)

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(20),
    customer_surname VARCHAR (20),
    email VARCHAR(50),
    phone VARCHAR(20),
    register_date DATE,
    bonus_points INTEGER
)

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES customers(id),
    amount INTEGER,
    order_status VARCHAR(15)
    created_at TIMESTAMP,
    payment_method VARCHAR(30)
)

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    price INTEGER
)
