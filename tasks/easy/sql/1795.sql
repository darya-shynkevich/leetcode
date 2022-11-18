# Write an SQL query to rearrange the Products table so that each row has (product_id, store, price).
# If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
#
# Return the result table in any order.


Create table If Not Exists Products (product_id int, store1 int null, store2 int, store3 int);

insert into Products (product_id, store1, store2, store3) values ('0', '95', '100', '105');
insert into Products (product_id, store1, store2, store3) values ('1', '70', null, '80');

SELECT product_id, 'store1' as store, store1 AS price FROM Products
    WHERE store1 IS NOT NULL
    UNION
SELECT product_id, 'store2' as store, store2 AS price FROM Products
    WHERE store2 IS NOT NULL
    UNION
SELECT product_id, 'store3' as store, store3 AS price FROM Products
    WHERE store3 IS NOT NULL;

DROP TABLE Products;
