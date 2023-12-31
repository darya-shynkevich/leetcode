# Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.
#
# Return the result table in any order.

DROP TABLE If Exists Warehouse;

DROP TABLE If Exists Products;

Create table If Not Exists Warehouse (name varchar(50), product_id int, units int);

Create table If Not Exists Products (product_id int, product_name varchar(50), Width int,Length int,Height int);

insert into Warehouse (name, product_id, units) values ('LCHouse1', '1', '1');
insert into Warehouse (name, product_id, units) values ('LCHouse1', '2', '10');
insert into Warehouse (name, product_id, units) values ('LCHouse1', '3', '5');
insert into Warehouse (name, product_id, units) values ('LCHouse2', '1', '2');
insert into Warehouse (name, product_id, units) values ('LCHouse2', '2', '2');
insert into Warehouse (name, product_id, units) values ('LCHouse3', '4', '1');

insert into Products (product_id, product_name, Width, Length, Height) values ('1', 'LC-TV', '5', '50', '40');
insert into Products (product_id, product_name, Width, Length, Height) values ('2', 'LC-KeyChain', '5', '5', '5');
insert into Products (product_id, product_name, Width, Length, Height) values ('3', 'LC-Phone', '2', '10', '10');
insert into Products (product_id, product_name, Width, Length, Height) values ('4', 'LC-T-Shirt', '4', '10', '20');

SELECT Warehouse.name as warehouse_name, SUM(units * P.Width * P.Length * P.Height) AS volume
FROM Warehouse JOIN Products P on Warehouse.product_id = P.product_id
GROUP BY warehouse_name;

