--Топ 5 найпопулярніших продуктів:
CREATE FUNCTION GetTop5PopularProducts()
RETURNS TABLE
AS
RETURN
    SELECT TOP 5
        p.Name AS ProductName,
        SUM(od.Quantity) AS TotalSold
    FROM Products p
    JOIN OrderDetails od ON p.ProductID = od.ProductID
    GROUP BY p.Name
    ORDER BY TotalSold DESC;
