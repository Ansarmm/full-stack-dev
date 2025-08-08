CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(30) NOT NULL,
    model VARCHAR(30) NOT NULL,
    year INTEGER NOT NULL,
    price INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    iin INTEGER UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    car_id INTEGER REFERENCES cars(id),
    client_id INTEGER REFERENCES clients(id),
    sale_date DATE DEFAULT CURRENT_DATE,
    amount INTEGER NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO cars (brand, model, year, price, status)
VALUES 
    ('Tesla', 'Model X', '2020', '25000', 'for sale'),
    ('Toyota', 'Corolla', '2012', '20000', 'for sale'),
    ('Mazda', 'Gorilla', '2010', '21000', 'sold out'),
    ('Chevrolet', 'Camaro', '2007', '13000', 'for sale'),
    ('Lamborghini', 'Urus', '2021', '200000', 'for sale');

INSERT INTO clients (first_name, last_name, iin, phone, email)
VALUES  
    ('Альтаир', 'Абдрахманов', '12345', '+7 777 130 64 22', 'alta@gmail.com'),
    ('Алия', 'Сатпаева', '43221', '+7 777 130 64 21', 'aliya@mail.com'),
    ('Алинур', 'Нурланов', '12343', '+7 777 130 64 20', 'ali@gmail.com');

INSERT INTO employees (first_name, last_name, position)
VALUES
    ('Алексей', 'Шпак', 'СММ менеджер'),
    ('Турбек', 'Маратов', 'Junior developer');

INSERT INTO sales (amount)
VALUES 
    ('200000'),
    ('21000');