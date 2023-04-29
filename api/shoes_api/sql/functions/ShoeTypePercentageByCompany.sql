--Таблиця типу взуття і відсоток на компанію
CREATE FUNCTION GetShoeTypePercentageByCompany()
RETURNS TABLE
AS
RETURN
    SELECT 
        p.Category, 
        sc.SupplierCompanyID, 
        COUNT(*) AS NumberOfShoes,
        (CAST(COUNT(*) AS FLOAT) / CAST((SELECT COUNT(*) FROM Supplies WHERE SupplierCompanyID = sc.SupplierCompanyID) AS FLOAT)) * 100 AS Percentage
    FROM Products p
    JOIN Supplies s ON p.ProductID = s.ProductID
    JOIN SupplierCompany sc ON s.SupplierCompanyID = sc.SupplierCompanyID
    GROUP BY p.Category, sc.SupplierCompanyID;
