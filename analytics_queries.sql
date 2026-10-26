-- SQLite-compatible e-commerce analytics queries
-- 1. Revenue by month for completed orders
SELECT substr(o.OrderDate,1,7) AS OrderMonth, ROUND(SUM(oi.LineSalesINR),2) AS RevenueINR
FROM Orders o JOIN OrderItems oi ON o.OrderID=oi.OrderID
WHERE o.OrderStatus='Completed'
GROUP BY substr(o.OrderDate,1,7) ORDER BY OrderMonth;

-- 2. Top 10 products by completed-order revenue
SELECT p.ProductName, p.Category, SUM(oi.Quantity) AS UnitsSold,
       ROUND(SUM(oi.LineSalesINR),2) AS RevenueINR
FROM Products p JOIN OrderItems oi ON p.ProductID=oi.ProductID
JOIN Orders o ON o.OrderID=oi.OrderID
WHERE o.OrderStatus='Completed'
GROUP BY p.ProductID, p.ProductName, p.Category
ORDER BY RevenueINR DESC LIMIT 10;

-- 3. Revenue by category
SELECT p.Category, ROUND(SUM(oi.LineSalesINR),2) AS RevenueINR
FROM Products p JOIN OrderItems oi ON p.ProductID=oi.ProductID
JOIN Orders o ON o.OrderID=oi.OrderID
WHERE o.OrderStatus='Completed'
GROUP BY p.Category ORDER BY RevenueINR DESC;

-- 4. Customer order frequency
SELECT c.CustomerID, c.CustomerName, COUNT(DISTINCT o.OrderID) AS CompletedOrders,
       ROUND(SUM(oi.LineSalesINR),2) AS RevenueINR
FROM Customers c JOIN Orders o ON c.CustomerID=o.CustomerID
JOIN OrderItems oi ON o.OrderID=oi.OrderID
WHERE o.OrderStatus='Completed'
GROUP BY c.CustomerID, c.CustomerName
ORDER BY CompletedOrders DESC, RevenueINR DESC;

-- 5. Order status distribution
SELECT OrderStatus, COUNT(*) AS OrderCount FROM Orders GROUP BY OrderStatus;

-- 6. Profit by category on completed orders
SELECT p.Category, ROUND(SUM(oi.LineProfitINR),2) AS ProfitINR
FROM Products p JOIN OrderItems oi ON p.ProductID=oi.ProductID
JOIN Orders o ON o.OrderID=oi.OrderID
WHERE o.OrderStatus='Completed'
GROUP BY p.Category ORDER BY ProfitINR DESC;
