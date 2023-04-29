--Витрати за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetCostsByMonth(@Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE MONTH(s.DateOfDelivery) = @Month AND YEAR(s.DateOfDelivery) = @Year;
