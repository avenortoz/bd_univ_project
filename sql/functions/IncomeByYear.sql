--Дохід за місяць, за 3 місяці, за рік:

-- For year
CREATE FUNCTION GetIncomeByYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(o.TotalPrice) AS Income
    FROM Orders o
    WHERE YEAR(o.CreateDate) = @Year;
