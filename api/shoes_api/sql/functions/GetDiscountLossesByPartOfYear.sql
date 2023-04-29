CREATE FUNCTION GetDiscountLossesByPartOfYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        (MONTH(o.CreateDate) - 1) / 3 + 1 AS PartOfYear,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY (MONTH(o.CreateDate) - 1) / 3 + 1;
