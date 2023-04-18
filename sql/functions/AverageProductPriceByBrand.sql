--Середня ціна продуктів за брендом:
CREATE FUNCTION GetAverageProductPriceByBrand()
RETURNS TABLE
AS
RETURN
    SELECT 
        b.Name AS BrandName,
        AVG(p.Price) AS AveragePrice
    FROM Brands b
    JOIN Products p ON b.BrandID = p.BrandID
    GROUP BY b.Name;
