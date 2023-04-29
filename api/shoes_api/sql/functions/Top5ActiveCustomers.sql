--Топ 5 найактивніших клієнтів:
CREATE FUNCTION GetTop5ActiveCustomers()
RETURNS TABLE
AS
RETURN
    SELECT TOP 5
        c.FirstName,
        c.LastName,
        COUNT(o.OrderID) AS TotalOrders
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY c.FirstName, c.LastName
    ORDER BY TotalOrders DESC;
