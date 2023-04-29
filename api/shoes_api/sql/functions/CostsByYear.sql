--Витрати за місяць, за 3 місяці, за рік:

-- For year
CREATE FUNCTION GetCostsByYear()
RETURNS TABLE
AS
RETURN
    SELECT
        YEAR(s.DateOfDelivery) AS Year,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    GROUP BY YEAR(s.DateOfDelivery);
