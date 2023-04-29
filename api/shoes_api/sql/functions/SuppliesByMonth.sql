--Кількість постачань за місяць (supplies id за місяць):
CREATE FUNCTION GetSuppliesByMonth(@Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT 
        SupplyID
    FROM Supplies
    WHERE MONTH(DateOfDelivery) = @Month AND YEAR(DateOfDelivery) = @Year;
