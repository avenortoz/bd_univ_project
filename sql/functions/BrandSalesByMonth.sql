--Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetBrandSalesByMonth(@BrandID INT, @Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        b.BrandID,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Brands b ON p.BrandID = b.BrandID
    WHERE b.BrandID = @BrandID AND MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year
    GROUP BY b.BrandID;

