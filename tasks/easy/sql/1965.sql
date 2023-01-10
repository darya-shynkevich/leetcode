# Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:
#
# The employee's name is missing, or
# The employee's salary is missing.
# Return the result table ordered by employee_id in ascending order.
#
# The query result format is in the following example.

DROP table If Exists Employees;
DROP table If Exists Salaries;

Create table If Not Exists Employees (employee_id int, name varchar(30));
Create table If Not Exists Salaries (employee_id int, salary int);

Truncate table Employees;
insert into Employees (employee_id, name) values ('2', 'Crew');
insert into Employees (employee_id, name) values ('4', 'Haven');
insert into Employees (employee_id, name) values ('5', 'Kristian');

Truncate table Salaries;
insert into Salaries (employee_id, salary) values ('5', '76071');
insert into Salaries (employee_id, salary) values ('1', '22517');
insert into Salaries (employee_id, salary) values ('4', '63539');
