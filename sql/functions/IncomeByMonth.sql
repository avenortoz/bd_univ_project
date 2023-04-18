--Дохід за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetIncomeByMonth(@Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(o.TotalPrice) AS Income
    FROM Orders o
    WHERE MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year;

