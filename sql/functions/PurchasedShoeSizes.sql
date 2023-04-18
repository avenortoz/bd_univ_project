--На кожну пару взуття купленні розміри:
CREATE FUNCTION GetPurchasedShoeSizes()
RETURNS TABLE
AS
RETURN
    SELECT 
        p.ProductID,
        p.Name AS ShoeName,
        ps.SizeID,
        s.Size AS ShoeSize,
        SUM(od.Quantity) AS NumberOfPairsPurchased
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN ProductSize ps ON p.ProductID = ps.ProductID
    JOIN Sizes s ON ps.SizeID = s.SizeID
    GROUP BY p.ProductID, p.Name, ps.SizeID, s.Size;
