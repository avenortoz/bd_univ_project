--Прибуток місяць, за 3 місяці, за рік:

-- For 3 months
CREATE FUNCTION GetProfitBy3Months(@StartMonth INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        (Income - Costs) AS Profit
    FROM (
        SELECT 
            SUM(o.TotalPrice) AS Income,
            SUM(s.TotalSum) AS Costs
        FROM Orders o
        JOIN Supplies s ON MONTH(s.DateOfDelivery) BETWEEN @StartMonth AND (@StartMonth + 2) AND YEAR(s.DateOfDelivery) = @Year
        WHERE MONTH(o.CreateDate) BETWEEN @StartMonth AND (@StartMonth + 2) AND YEAR(o.CreateDate) = @Year
    ) AS Subquery;
