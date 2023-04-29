--Кількість куплених пар на ціновий діапазон за місяць, за рік
-- For month
CREATE FUNCTION GetPairsByPriceRangeByMonth(@MinPrice MONEY, @MaxPrice MONEY, @Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        COUNT(*) AS NumberOfPairs
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    WHERE od.Price BETWEEN @MinPrice AND @MaxPrice AND MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year;
