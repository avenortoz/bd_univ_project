--Дохід за місяць, за 3 місяці, за рік:

-- For 3 months
CREATE FUNCTION GetIncomeBy3Months(@StartMonth INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(o.TotalPrice) AS Income
    FROM Orders o
    WHERE MONTH(o.CreateDate) BETWEEN @StartMonth AND (@StartMonth + 2) AND YEAR(o.CreateDate) = @Year;
