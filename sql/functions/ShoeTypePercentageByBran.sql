--Таблиця типу взуття і відсоток на бренд:
CREATE FUNCTION GetShoeTypePercentageByBrand()
RETURNS TABLE
AS
RETURN
    SELECT 
        p.Category, 
        b.BrandID, 
        COUNT(*) AS NumberOfShoes,
        (CAST(COUNT(*) AS FLOAT) / CAST((SELECT COUNT(*) FROM Products WHERE BrandID = b.BrandID) AS FLOAT)) * 100 AS Percentage
    FROM Products p
    JOIN Brands b ON p.BrandID = b.BrandID
    GROUP BY p.Category, b.BrandID;
