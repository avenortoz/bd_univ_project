--Витрати за місяць, за 3 місяці, за рік:

CREATE FUNCTION GetCostsByPartOfYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        (MONTH(s.DateOfDelivery) - 1) / 3 + 1 AS PartOfYear,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE YEAR(s.DateOfDelivery) = @Year
    GROUP BY (MONTH(s.DateOfDelivery) - 1) / 3;