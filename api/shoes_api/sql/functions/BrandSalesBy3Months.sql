--Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
CREATE FUNCTION GetBrandSalesByPartOfYear(@PartOfYear INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        b.BrandName,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Brands b ON p.BrandID = b.BrandID
    WHERE (MONTH(o.CreateDate) - 1) / 3 = (@PartOfYear - 1) AND YEAR(o.CreateDate) = @Year
    GROUP BY b.BrandName;

