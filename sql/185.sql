DROP TABLE IF EXISTS Employee;

Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));

Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');

Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

# A company's executives are interested in seeing who earns the most money in each of the company's departments.
# A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
#
# Write a solution to find the employees who are high earners in each of the departments.
#
# Return the result table in any order.

SELECT
    dept.name AS 'Department',
    emp1.name AS 'Employee',
    emp1.salary
FROM Employee emp1
JOIN Department dept ON emp1.departmentId = dept.id
WHERE 3 > (
    SELECT COUNT(DISTINCT emp2.salary)
    FROM Employee emp2
    WHERE emp2.salary > emp1.salary AND emp1.departmentId = emp2.departmentId
);
