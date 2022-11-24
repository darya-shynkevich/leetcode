# Write an SQL query to convert each date in Days into a string formatted as "day_name, month_name day, year".
#
# Return the result table in any order.

DROP TABLE IF EXISTS Days;

Create table If Not Exists Days (day date);

insert into Days (day) values ('2022-04-12');
insert into Days (day) values ('2021-08-09');
insert into Days (day) values ('2020-06-26');


SELECT CONCAT(
    CONCAT(DAYNAME(day), ', ', MONTHNAME(day), ' ', DAY(day), ', ', YEAR(day))
) AS day FROM Days;
