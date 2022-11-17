# Write an SQL query to report the shortest distance between any two points from the Point table.

Create Table If Not Exists Point (x int not null);

insert into Point (x) values ('-1');
insert into Point (x) values ('0');
insert into Point (x) values ('2');


SELECT Min(p1.x - p2.x) AS shortest FROM Point AS p1 CROSS JOIN Point as p2 WHERE p1.x > p2.x;
