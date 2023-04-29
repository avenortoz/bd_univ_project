--Витрати за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetCostsByMonth(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        MONTH(s.DateOfDelivery) AS Month,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE YEAR(s.DateOfDelivery) = @Year
    GROUP BY MONTH(s.DateOfDelivery);