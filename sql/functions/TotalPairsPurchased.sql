--Кількість купленого взуття:
CREATE FUNCTION GetTotalPairsPurchased()
RETURNS TABLE
AS
RETURN
    SELECT 
        SUM(od.Quantity) AS TotalPairsPurchased
    FROM OrderDetails od;
