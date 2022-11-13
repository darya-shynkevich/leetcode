# Write an SQL query to find the ids of products that are both low fat and recyclable.
#
# Return the result table in any order.
#
# The query result format is in the following example.


CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats ENUM('Y', 'N'), recyclable ENUM('Y', 'N'));


INSERT INTO Products(product_id, low_fats, recyclable) VALUES
        (0, 'Y', 'N'),
        (1, 'Y', 'Y'),
        (2, 'N', 'Y'),
        (3, 'Y', 'Y'),
        (4, 'N', 'N');


SELECT product_id from Products WHERE low_fats = 'Y' AND recyclable = 'Y';
