-- Demo SQL; orders table is loaded with build_db.py from synthetic_orders.csv
SELECT substr(order_date,1,7) month, COUNT(*) orders,
 ROUND(SUM(quantity*unit_price_sar*(1-discount_rate)),2) revenue_sar
FROM orders WHERE order_status='Completed' GROUP BY month ORDER BY month;

SELECT category, COUNT(*) orders,
 ROUND(SUM(quantity*unit_price_sar*(1-discount_rate)),2) revenue_sar
FROM orders WHERE order_status='Completed' GROUP BY category ORDER BY revenue_sar DESC;

SELECT customer_id,COUNT(*) completed_orders,
 ROUND(SUM(quantity*unit_price_sar*(1-discount_rate)),2) customer_revenue_sar
FROM orders WHERE order_status='Completed' GROUP BY customer_id ORDER BY customer_revenue_sar DESC;

SELECT region,ROUND(SUM(quantity*unit_price_sar*(1-discount_rate)),2) revenue_sar
FROM orders WHERE order_status='Completed' GROUP BY region ORDER BY revenue_sar DESC;
