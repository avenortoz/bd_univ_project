--Прибуток місяць, за 3 місяці, за рік:


-- For year
CREATE FUNCTION GetProfitByYear(@Year INT)
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
        JOIN Supplies s ON YEAR(s.DateOfDelivery) = @Year
        WHERE YEAR(o.CreateDate) = @Year
    ) AS Subquery;
