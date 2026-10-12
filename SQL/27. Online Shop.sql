SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM customers;

SELECT
  orders.id AS order_id,
  customers.name AS customer_name,
  products.name AS product_name,
  products.price AS total_price
FROM orders
INNER JOIN customers
  ON orders.customer_id = customers.id
INNER JOIN products
  ON orders.item_id = products.id;