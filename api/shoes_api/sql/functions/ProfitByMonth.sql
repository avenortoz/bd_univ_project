--Прибуток місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetProfitByMonth(@Month INT, @Year INT)
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
        JOIN Supplies s ON MONTH(s.DateOfDelivery) = @Month AND YEAR(s.DateOfDelivery) = @Year
        WHERE MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year
    ) AS Subquery;

