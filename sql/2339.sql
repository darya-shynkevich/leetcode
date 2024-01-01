# Write an SQL query that reports all the possible matches of the league.
# Note that every two teams play two matches with each other,
# with one team being the home_team once and the other time being the away_team.
#
# Return the result table in any order.

DROP TABLE IF EXISTS Teams;

Create table If Not Exists Teams (team_name varchar(50));

insert into Teams (team_name) values ('Leetcode FC');
insert into Teams (team_name) values ('Ahly SC');
insert into Teams (team_name) values ('Real Madrid');


SELECT Teams.team_name AS home_team, T.team_name AS away_team
FROM Teams CROSS JOIN Teams T on Teams.team_name != T.team_name;
