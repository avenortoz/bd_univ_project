CREATE FUNCTION GetDiscountLossesByYear()
RETURNS TABLE
AS
RETURN
    SELECT
        YEAR(o.CreateDate) AS Year,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    GROUP BY YEAR(o.CreateDate);
