-- SQL-команды для создания таблиц:
CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100)
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) NOT NULL,
	employee_id smallint NOT NULL,
	order_date date,
	ship_city varchar(100)
);

