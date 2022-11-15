# Write an SQL query to find the IDs of the invalid tweets.
# The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
#
# Return the result table in any order.


Create table If Not Exists Tweets(tweet_id int, content varchar(50));

insert into Tweets (tweet_id, content) values ('1', 'Vote for Biden');
insert into Tweets (tweet_id, content) values ('2', 'Let us make America great again!');

SELECT tweet_id FROM Tweets WHERE LENGTH(content) >= 15;
