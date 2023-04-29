--Статистика проданих пар по статі по місяцях (місяць, стать, кількість пар):
CREATE FUNCTION GetMonthlySalesBySex()
RETURNS TABLE
AS
RETURN
    SELECT 
        MONTH(o.CreateDate) AS Month, 
        c.Sex, 
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Customers c ON o.CustomerID = c.CustomerID
    GROUP BY MONTH(o.CreateDate), c.Sex;
