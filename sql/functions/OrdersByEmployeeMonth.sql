﻿--Статистика замовлень для конкретного співробітника, за місяць, за 3 місяці, рік:
-- For month
CREATE FUNCTION GetEmployeeOrdersByMonth(@EmployeeID INT, @Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        o.OrderID,
        o.TotalPrice,
        o.TotalPriceWithDiscount
    FROM Orders o
    WHERE o.EmployeeID = @EmployeeID AND MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year;
