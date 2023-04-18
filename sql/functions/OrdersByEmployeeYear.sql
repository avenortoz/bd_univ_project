--Статистика замовлень для конкретного співробітника, за місяць, за 3 місяці, рік:

-- For year
CREATE FUNCTION GetEmployeeOrdersByYear(@EmployeeID INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        o.OrderID,
        o.TotalPrice,
        o.TotalPriceWithDiscount
    FROM Orders o
    WHERE o.EmployeeID = @EmployeeID AND YEAR(o.CreateDate) = @Year;

