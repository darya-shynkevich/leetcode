# Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
#
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.
#
# The query result format is in the following example.

DROP TABLE IF EXISTS orders;

Create table If Not Exists orders (order_number int, customer_number int);

Truncate table orders;
insert into orders (order_number, customer_number) values ('1', '1');
insert into orders (order_number, customer_number) values ('2', '2');
insert into orders (order_number, customer_number) values ('3', '3');
insert into orders (order_number, customer_number) values ('4', '3');
