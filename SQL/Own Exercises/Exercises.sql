
-- EASY 1: List all products in the Electronics category, most expensive first.
SELECT name, category, price FROM products 
WHERE category = 'Electronics' 
ORDER BY price DESC;

-- EASY 2: Count how many customers live in each city.
SELECT * FROM customers;
SELECT DISTINCT city, 
COUNT(*) AS total 
FROM customers
GROUP BY city; 

-- MEDIUM 3: Show each customer’s name and total amount spent on delivered orders, 
-- highest first. (Needs joins across 4 tables, plus quantity * price.)
SELECT DISTINCT name 
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
JOIN
WHERE status = 'delivered';

-- MEDIUM 4: Productos que nunca se han pedido.


-- HARD 5: Ingresos por mes (sin pedidos 'cancelled') con total acumulado.


-- HARD 6: Producto más vendido por ingresos en cada categoría.