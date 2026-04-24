/* 1,Create a single query to list the product id, product name, unit price and category name of all products. 
Order by category name and within that, by product name.*/

SELECT ProductID, ProductName, UnitPrice, CategoryName FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY CategoryName, ProductName;

/* 2,Create a single query to list the product id, product name, unit price and supplier name of all products
that cost more than $75. Order by product name. */

SELECT ProductID, ProductName, UnitPrice, CompanyName FROM products
JOIN suppliers
ON products.SupplierID =suppliers.SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

/* 3,Create a single query to list the product id, product name, unit price, category name, and supplier 
name of every product. Order by product name.*/

SELECT ProductID, ProductName, UnitPrice, CategoryName, CompanyName FROM products
JOIN categories 
ON products.CategoryID = categories.CategoryID
JOIN suppliers 
ON products.SupplierID = suppliers.SupplierID
ORDER BY ProductName;

/* 4,Create a single query to list the order id, ship name, ship address, and shipping company name of every 
order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of 
the shipper, then the name of who it shipped to.*/

SELECT OrderID, ShipName, ShipAddress, CompanyName AS 'Shipper' FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = 'Germany'
ORDER BY Shipper, ShipName;

/* 5,Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a 
count of how many orders were shipped for that ship name.*/

SELECT ShipName, ShipAddress, CompanyName AS 'Shipper', count(*) AS Orders FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = 'Germany'
GROUP BY ShipName, ShipAddress, CompanyName
ORDER BY Shipper, ShipName;

/* 6,Create a single query to list the order id, order date, ship name, ship address of all orders that
included Sasquatch Ale.
∗ Hint: You will need to join on three tables to accomplish this. (One of these tables has 
a sneaky space in the name, so you will need to surround it with backticks, like this: `table name`)*/

SELECT orders.OrderID, OrderDate, ShipName, ShipAddress FROM orders
JOIN `order details`
ON orders.OrderID = `order details`.OrderID
JOIN products
ON `order details`.ProductID = products.ProductID
WHERE ProductName = 'Sasquatch Ale';

