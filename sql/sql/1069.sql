# Write an SQL query that reports the total quantity sold for every product id.
#
# Return the resulting table in any order.
#
# The query result format is in the following example.

DROP table If Exists Sales;
DROP table If Exists Product;

Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar(10));

Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');

Truncate table Product;
insert into Product (product_id, product_name) values ('100', 'Nokia');
insert into Product (product_id, product_name) values ('200', 'Apple');
insert into Product (product_id, product_name) values ('300', 'Samsung');

SELECT S.product_id, SUM(quantity) as total_quantity
FROM Sales S LEFT JOIN Product P on P.product_id = S.product_id
GROUP BY S.product_id
