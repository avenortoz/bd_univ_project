--Втрати на знижках:
CREATE FUNCTION GetDiscountLossesByMonth(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        MONTH(o.CreateDate) AS Month,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY MONTH(o.CreateDate);
