# Write an SQL query to report the IDs of the low-quality problems.
# A LeetCode problem is low-quality if the like percentage of the problem
# (number of likes divided by the total number of votes) is strictly less than 60%.
#
# Return the result table ordered by problem_id in ascending order.
#
# The query result format is in the following example.

DROP table If Exists Problems;

Create table If Not Exists Problems (problem_id int, likes int, dislikes int);
TRUNCATE Problems;
insert into Problems (problem_id, likes, dislikes) values ('6', '1290', '425');
insert into Problems (problem_id, likes, dislikes) values ('11', '2677', '8659');
insert into Problems (problem_id, likes, dislikes) values ('1', '4446', '2760');
insert into Problems (problem_id, likes, dislikes) values ('7', '8569', '6086');
insert into Problems (problem_id, likes, dislikes) values ('13', '2050', '4164');
insert into Problems (problem_id, likes, dislikes) values ('10', '9002', '7446');


SELECT problem_id
FROM Problems
WHERE likes / (likes + dislikes) < 0.6
ORDER BY problem_id;
