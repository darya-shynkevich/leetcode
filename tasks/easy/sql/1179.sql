# Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.
#
# Return the result table in any order.
#
# The query result format is in the following example.

DROP TABLE IF EXISTS Department;

Create table If Not Exists Department (id int, revenue int, month varchar(5));

Truncate table Department;
insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');


SELECT
  id,
  SUM(IF (month = 'Jan', revenue, null)) AS Jan_Revenue,
  SUM(IF (month = 'Feb', revenue, null)) AS Feb_Revenue,
  SUM(IF (month = 'Mar', revenue, null)) AS Mar_Revenue,
  SUM(IF (month = 'Apr', revenue, null)) AS Apr_Revenue,
  SUM(IF (month = 'May', revenue, null)) AS May_Revenue,
  SUM(IF (month = 'Jun', revenue, null)) AS Jun_Revenue,
  SUM(IF (month = 'Jul', revenue, null)) AS Jul_Revenue,
  SUM(IF (month = 'Aug', revenue, null)) AS Aug_Revenue,
  SUM(IF (month = 'Sep', revenue, null)) AS Sep_Revenue,
  SUM(IF (month = 'Oct', revenue, null)) AS Oct_Revenue,
  SUM(IF (month = 'Nov', revenue, null)) AS Nov_Revenue,
  SUM(IF (month = 'Dec', revenue, null)) AS Dec_Revenue
FROM
  Department
GROUP BY
  id;
