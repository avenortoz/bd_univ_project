--Загальна кількість товарів на складі:
CREATE FUNCTION GetTotalProductsInStock()
RETURNS TABLE
AS
RETURN
    SELECT 
        p.Name AS ProductName,
        (s.Units - COALESCE(SUM(od.Quantity), 0)) AS Stock
    FROM Products p
    JOIN Supplies s ON p.ProductID = s.ProductID
    LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
    GROUP BY p.Name, s.Units;
