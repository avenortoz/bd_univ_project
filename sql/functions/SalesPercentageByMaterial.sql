--Відсоток продажів за категорією матеріалів:
CREATE FUNCTION GetSalesPercentageByMaterial()
RETURNS TABLE
AS
RETURN
    SELECT 
        m.Name AS MaterialName,
        SUM(od.Quantity) AS TotalSold,
        (SUM(od.Quantity) * 100.0 / (SELECT SUM(Quantity) FROM OrderDetails)) AS SalesPercentage
    FROM Materials m
    JOIN ProductMaterial pm ON m.MaterialID = pm.MaterialID
    JOIN OrderDetails od ON pm.ProductID = od.ProductID
    GROUP BY m.Name;
