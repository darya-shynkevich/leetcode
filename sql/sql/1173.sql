# If the customer's preferred delivery date is the same as the order date, then the order is called immediate;
# otherwise, it is called scheduled.
#
# Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.
#
# The query result format is in the following example.

DROP table If Exists Delivery;

Create table If Not Exists Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date);
Truncate table Delivery;
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('1', '1', '2019-08-01', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('2', '5', '2019-08-02', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('3', '1', '2019-08-11', '2019-08-11');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('4', '3', '2019-08-24', '2019-08-26');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('5', '4', '2019-08-21', '2019-08-22');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date) values ('6', '2', '2019-08-11', '2019-08-13');


SELECT ROUND(100 * (A.immediate_orders / B.total_deliveries), 2) AS immediate_percentage
FROM (
    SELECT COUNT(*) AS immediate_orders
    FROM Delivery
    WHERE order_date = customer_pref_delivery_date
) AS A,
(
    SELECT COUNT(*) AS total_deliveries FROM Delivery
) AS B;
