-- SQL-команды для создания таблиц:
CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100)
);

CREATE TABLE employee
(
	employee_id smallint PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id smallint REFERENCES employee(employee_id),
	order_date date,
	ship_city varchar(100)
);

