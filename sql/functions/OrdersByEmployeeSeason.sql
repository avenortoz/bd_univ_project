--Статистика замовлень для конкретного співробітника, за місяць, за 3 місяці, рік:
-- For 3 months
CREATE FUNCTION GetEmployeeOrdersBy3Months(@EmployeeID INT, @StartMonth INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        o.OrderID,
        o.TotalPrice,
        o.TotalPriceWithDiscount
    FROM Orders o
    WHERE o.EmployeeID = @EmployeeID AND MONTH(o.CreateDate) BETWEEN @StartMonth AND (@StartMonth + 2) AND YEAR(o.CreateDate) = @Year;
