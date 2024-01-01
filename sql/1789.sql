# Employees can belong to multiple departments. When the employee joins other departments,
# they need to decide which department is their primary department.
# 'N'ote that when an employee belongs to only one department, their primary column is 'N'.
#
# Write an SQL query to report all the employees with their primary department.
# For employees who belong to one department, report their only department.
#
# Return the result table in any order.
#
# The query result format is in the following example.

DROP TABLE IF EXISTS Employee;

Create table If Not Exists Employee (employee_id int, department_id int, primary_flag ENUM('Y','N'));

Truncate table Employee;
insert into Employee (employee_id, department_id, primary_flag) values (1, 1, 'N');
insert into Employee (employee_id, department_id, primary_flag) values (2, 1, 'Y');
insert into Employee (employee_id, department_id, primary_flag) values (2, 2, 'N');
insert into Employee (employee_id, department_id, primary_flag) values (3, 3, 'N');
insert into Employee (employee_id, department_id, primary_flag) values (4, 2, 'N');
insert into Employee (employee_id, department_id, primary_flag) values (4, 3, 'Y');
insert into Employee (employee_id, department_id, primary_flag) values (4, 4, 'N');


SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' OR employee_id in (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(employee_id) = 1
)
GROUP BY employee_id
