# Write an SQL query to report the number of customers who had at least one bill with an amount strictly greater than 500.
#
# The query result format is in the following example.

DROP TABLE IF EXISTS Store;

Create table If Not Exists Store (bill_id int, customer_id int, amount int);

Truncate table Store;
insert into Store (bill_id, customer_id, amount) values (6, 1, 549);
insert into Store (bill_id, customer_id, amount) values (8, 1, 834);
insert into Store (bill_id, customer_id, amount) values (4, 2, 394);
insert into Store (bill_id, customer_id, amount) values (11, 3, 657);
insert into Store (bill_id, customer_id, amount) values (13, 3, 257);


SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500;
