USE northwind;

/* 1,Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to 
find the name of the product that has that price.*/ 

SELECT min(UnitPrice) FROM products;

SELECT ProductName FROM products
ORDER BY UnitPrice
LIMIT 1;

/* 2,Write a query to find the average price of all items that Northwind sells. (Bonus: Once you have written 
a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average 
price to the nearest cent.)*/

SELECT avg(UnitPrice) FROM products;

SELECT round(avg(UnitPrice), 2) AS AveragePrice FROM products; -- Bonus 

/* 3,Write a query to find the price of the most expensive item that Northwind sells. Then write a second
query to find the name of the product with that price, plus the name of the supplier for that product.*/


SELECT ProductName, CompanyName FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE UnitPrice = (
     SELECT max(UnitPrice) FROM products);
     
-- 4,Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).

SELECT round(sum(Salary), 2) AS TotalPayroll FROM employees;

/* 5,Write a query to identify the highest salary and the lowest salary amounts which any employee makes.
(Just the amounts, not the specific employees!)*/

SELECT max(Salary), min(Salary) FROM employees;

/* 6,Write a query to find the name and supplier ID of each supplier and the number of items they supply.
Hint: Join is your friend here.*/

SELECT suppliers.SupplierID, CompanyName, count(products.ProductID) AS 'Total Items'
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, CompanyName;

/* 7,Write a query to find the list of all category names and the average price for items in each category.*/

SELECT CategoryName, round(avg(UnitPrice), 2) AS AvgPrice FROM categories
JOIN products
ON categories.CategoryID = products.CategoryID
GROUP BY categories.CategoryID;

/* 8,Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of 
each supplier and the number of items they supply.*/

SELECT CompanyName, count(products.ProductID) AS Items FROM suppliers
JOIN products
ON products.SupplierID =suppliers.SupplierID
GROUP BY suppliers.SupplierID, CompanyName
HAVING count(products.ProductID) >= 5;

/* 9,Write a query to list products currently in inventory by the product id, product name, and inventory 
value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending
order by value. If two or more have the same value, order by product name. If a product is not in stock,
leave it off the list.*/

SELECT ProductID, ProductName, UnitPrice, UnitsInStock, UnitPrice * UnitsInStock AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;








