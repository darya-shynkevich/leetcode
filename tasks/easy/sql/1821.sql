# Write an SQL query to report the customers with postive revenue in the year 2021.
#
# Return the result table in any order.

DROP TABLE IF EXISTS Customers;

Create table If Not Exists Customers (customer_id int, year int, revenue int);

insert into Customers (customer_id, year, revenue) values ('1', '2018', '50');
insert into Customers (customer_id, year, revenue) values ('1', '2021', '30');
insert into Customers (customer_id, year, revenue) values ('1', '2020', '70');
insert into Customers (customer_id, year, revenue) values ('2', '2021', '-50');
insert into Customers (customer_id, year, revenue) values ('3', '2018', '10');
insert into Customers (customer_id, year, revenue) values ('3', '2016', '50');
insert into Customers (customer_id, year, revenue) values ('4', '2021', '20');


SELECT customer_id
FROM Customers
WHERE year = '2021' AND revenue > 0;
