# Write an SQL query to find for each date the number of different products sold and their names.
#
# The sold products names for each date should be sorted lexicographically.
#
# Return the result table ordered by sell_date.
#
# The query result format is in the following example.


DROP table If Exists Activities;
Create table If Not Exists Activities (sell_date date, product varchar(20));
Truncate table Activities;

insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');


SELECT sell_date, COUNT(distinct product) AS num_sold, GROUP_CONCAT(distinct product) AS products
FROM Activities GROUP BY sell_date;
