# Write an SQL query to find the price of each product in each store.
#
# Return the result table in any order.
#
# The query result format is in the following example.


DROP table If Exists Products;

Create table If Not Exists Products (product_id int, store ENUM('store1', 'store2', 'store3'), price int);
Truncate table Products;
insert into Products (product_id, store, price) values ('0', 'store1', '95');
insert into Products (product_id, store, price) values ('0', 'store3', '105');
insert into Products (product_id, store, price) values ('0', 'store2', '100');
insert into Products (product_id, store, price) values ('1', 'store1', '70');
insert into Products (product_id, store, price) values ('1', 'store3', '80');


SELECT
  product_id,
  MAX(CASE WHEN store = 'store1' THEN price END) AS store1,
  MAX(CASE WHEN store = 'store2' THEN price END) AS store2,
  MAX(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products GROUP BY product_id;
