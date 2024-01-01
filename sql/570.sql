DROP TABLE Employee;
Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
Truncate table Employee;
insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', null);
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
insert into Employee (id, name, department, managerId) values ('107', 'Test 1', 'A', '103');
insert into Employee (id, name, department, managerId) values ('108', 'Test 2', 'B', '104');
insert into Employee (id, name, department, managerId) values ('109', 'Test 3', 'B', '104');
insert into Employee (id, name, department, managerId) values ('110', 'Test 4', 'B', '104');
insert into Employee (id, name, department, managerId) values ('111', 'Test 5', 'B', '104');
insert into Employee (id, name, department, managerId) values ('112', 'Test 6', 'B', '104');
insert into Employee (id, name, department, managerId) values ('113', 'Test 7', 'B', '104');
insert into Employee (id, name, department, managerId) values ('114', 'Test 8', 'B', '104');

SELECT name
FROM Employee
WHERE id in (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
)



