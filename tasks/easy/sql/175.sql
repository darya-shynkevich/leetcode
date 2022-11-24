# Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
# If the address of a personId is not present in the Address table, report null instead.
#
# Return the result table in any order.

DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Address;

Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255));
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255));

insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');

insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');


SELECT firstName, lastName, city, state from Person Left JOIN Address A on Person.personId = A.personId;
