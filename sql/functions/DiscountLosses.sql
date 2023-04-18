--Втрати на знижках:
CREATE FUNCTION GetDiscountLosses()
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o;
