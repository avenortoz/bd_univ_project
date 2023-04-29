--Таблиця тип взуття і відсоток від загальної кількості:
CREATE FUNCTION GetShoeTypePercentage()
RETURNS TABLE
AS
RETURN
    SELECT 
        p.Category, 
        COUNT(*) AS NumberOfShoes,
        (CAST(COUNT(*) AS FLOAT) / CAST((SELECT COUNT(*) FROM Products) AS FLOAT)) * 100 AS Percentage
    FROM Products p
    GROUP BY p.Category;
