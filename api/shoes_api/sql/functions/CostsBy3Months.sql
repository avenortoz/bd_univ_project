--Витрати за місяць, за 3 місяці, за рік:

-- For 3 months
CREATE FUNCTION GetCostsBy3Months(@StartMonth INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE MONTH(s.DateOfDelivery) BETWEEN @StartMonth AND (@StartMonth + 2) AND YEAR(s.DateOfDelivery) = @Year;
