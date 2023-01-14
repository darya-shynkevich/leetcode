# Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
#
# Return the result table in any order.
#
# The query result format is in the following example.

DROP TABLE IF EXISTS SalesPerson;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Orders;

Create table If Not Exists SalesPerson (sales_id varchar(255), name varchar(255), salary int, commission_rate varchar(255), hire_date varchar(255));
Create table If Not Exists Company (com_id varchar(255), name varchar(255), city varchar(255));
Create table If Not Exists Orders (order_id varchar(255), order_date varchar(255), com_id varchar(255), sales_id varchar(255), amount varchar(255));

Truncate table SalesPerson;
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('1', 'John', '100000', '6', '4/1/2006');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('2', 'Amy', '12000', '5', '5/1/2010');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('3', 'Mark', '65000', '12', '12/25/2008');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('4', 'Pam', '25000', '25', '1/1/2005');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('5', 'Alex', '5000', '10', '2/3/2007');

Truncate table Company;
insert into Company (com_id, name, city) values ('1', 'RED', 'Boston');
insert into Company (com_id, name, city) values ('2', 'ORANGE', 'New York');
insert into Company (com_id, name, city) values ('3', 'YELLOW', 'Boston');
insert into Company (com_id, name, city) values ('4', 'GREEN', 'Austin');

Truncate table Orders;
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('1', '1/1/2014', '3', '4', '10000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('2', '2/1/2014', '4', '5', '5000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('3', '3/1/2014', '1', '1', '50000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('4', '4/1/2014', '1', '4', '25000');


SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.name not in (SELECT SalesPerson.name
 FROM SalesPerson
          LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
          LEFT JOIN Company on Orders.com_id = Company.com_id
 WHERE Company.name = 'RED'
 GROUP BY SalesPerson.name)


