--Постачальник - кількість пар відносно загального
CREATE FUNCTION GetSupplierPairsPercentage()
RETURNS TABLE
AS
RETURN
    SELECT 
        s.SupplierID, 
        SUM(sp.Units) AS NumberOfPairs,
        (CAST(SUM(sp.Units) AS FLOAT) / CAST((SELECT SUM(Units) FROM Supplies) AS FLOAT)) * 100 AS Percentage
    FROM Supplies sp
    JOIN Suppliers s ON sp.SupplierCompanyID = s.SupplierCompanyID
    GROUP BY s.SupplierID;
