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
