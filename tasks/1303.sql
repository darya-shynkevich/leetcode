# Write an SQL query to find the team size of each of the employees.
#
# Return result table in any order.

Create table If Not Exists Employee (employee_id int, team_id int);

insert into Employee (employee_id, team_id) values ('1', '8');
insert into Employee (employee_id, team_id) values ('2', '8');
insert into Employee (employee_id, team_id) values ('3', '8');
insert into Employee (employee_id, team_id) values ('4', '7');
insert into Employee (employee_id, team_id) values ('5', '9');
insert into Employee (employee_id, team_id) values ('6', '9');


SELECT employee_id, COUNT(employee_id) OVER(PARTITION BY team_id) AS team_size FROM Employee GROUP BY employee_id;
