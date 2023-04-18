--Кожен тип взуття і кількість продана за місяць, за три місяці, за рік:

-- For year
CREATE FUNCTION GetShoeTypeSalesByYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        p.Category,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY p.Category;
