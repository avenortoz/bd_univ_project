--Кількість куплених пар на ціновий діапазон за місяць, за рік

-- For year
CREATE FUNCTION GetPairsByPriceRangeByYear(@MinPrice MONEY, @MaxPrice MONEY, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        COUNT(*) AS NumberOfPairs
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    WHERE od.Price BETWEEN @MinPrice AND @MaxPrice AND YEAR(o.CreateDate) = @Year;
