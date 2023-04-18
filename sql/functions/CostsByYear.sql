--Витрати за місяць, за 3 місяці, за рік:

-- For year
CREATE FUNCTION GetCostsByYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE YEAR(s.DateOfDelivery) = @Year;
