# There is a country with three schools, where each student is enrolled in exactly one school.
# The country is joining a competition and wants to select one student from each school to represent the country such that:
#
# member_A is selected from SchoolA,
# member_B is selected from SchoolB,
# member_C is selected from SchoolC, and
# The selected students' names and IDs are pairwise distinct
# (i.e. no two students share the same name, and no two students share the same ID).
# Write an SQL query to find all the possible triplets representing the country under the given constraints.
#
# Return the result table in any order.

DROP TABLE IF EXISTS SchoolA;
DROP TABLE IF EXISTS SchoolB;
DROP TABLE IF EXISTS SchoolC;

Create table If Not Exists SchoolA (student_id int, student_name varchar(20));
Create table If Not Exists SchoolB (student_id int, student_name varchar(20));
Create table If Not Exists SchoolC (student_id int, student_name varchar(20));

insert into SchoolA (student_id, student_name) values ('1', 'Alice');
insert into SchoolA (student_id, student_name) values ('2', 'Bob');

insert into SchoolB (student_id, student_name) values ('3', 'Tom');

insert into SchoolC (student_id, student_name) values ('3', 'Tom');
insert into SchoolC (student_id, student_name) values ('2', 'Jerry');
insert into SchoolC (student_id, student_name) values ('10', 'Alice');


SELECT
    A.student_name AS member_A,
    B.student_name AS member_B,
    C.student_name AS member_C
FROM SchoolA AS A JOIN SchoolB AS B ON
        A.student_name != B.student_name
        AND A.student_id != B.student_id
    JOIN SchoolC AS C ON
        A.student_name != C.student_name
        AND C.student_name != B.student_name
        AND C.student_id != A.student_id
        AND C.student_id != B.student_id
