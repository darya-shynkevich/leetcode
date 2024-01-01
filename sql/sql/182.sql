# Write an SQL query to report all the duplicate emails.
#
# Return the result table in any order.
#
# The query result format is in the following example.

DROP table If Exists Person;

Create table If Not Exists Person (id int, email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'a@b.com');
insert into Person (id, email) values ('2', 'c@d.com');
insert into Person (id, email) values ('3', 'a@b.com');

SELECT email AS Email
FROM (
    SELECT email, COUNT(email) as email_count
    FROM Person
    GROUP BY email
     ) as Statistic
WHERE Statistic.email_count > 1;
