-- task_5.sql

-- Use the alx_book_store database
USE alx_book_store;

-- Insert a single row into the 'customer' table
-- Note: The table name used here is 'customer' as specifically requested.
-- Please ensure your actual table name in the database matches this (e.g., if it was created as 'Customers',
-- you might need to adjust this script to 'Customers' or rename your table).
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
