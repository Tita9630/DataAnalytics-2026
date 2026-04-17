-- 4a, Products
-- 4b, Categories

SELECT * FROM employees;

-- 5a, Northwind employee whose name makes it look like she’s a bird is Margaret Peacock. 

SELECT * FROM products;

-- 6a, My query returned 77 rows. To retrieve only 10 rows, I can use the dropdown that says "Limit to..."and choose Limit to 10 rows. 
-- 6b, Bonus, Instead of just saying SELECT * FROM products; I would add "LIMIT 10". The source I used is Chatgpt.

SELECT * FROM categories; 
-- 7c, The category id of seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders;
