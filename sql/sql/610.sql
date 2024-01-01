# Write an SQL query to report for every three line segments whether they can form a triangle.
#
# Return the result table in any order.

DROP TABLE IF EXISTS Triangle;

Create table If Not Exists Triangle (x int, y int, z int);

Truncate table Triangle;
insert into Triangle (x, y, z) values (13, 15, 30);
insert into Triangle (x, y, z) values (10, 20, 15);


SELECT x, y, z, IF(x + y > z AND y + z > x AND x + z > y, 'Yes', 'No')  AS triangle
FROM Triangle;
