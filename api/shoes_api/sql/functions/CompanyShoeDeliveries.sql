--Скільки кожна компанія доставляє взуття:
CREATE FUNCTION GetCompanyShoeDeliveries()
RETURNS TABLE
AS
RETURN
    SELECT 
        sc.SupplierCompanyID, 
        SUM(sp.Units) AS NumberOfPairs
    FROM Supplies sp
    JOIN SupplierCompany sc ON sp.SupplierCompanyID = sc.SupplierCompanyID
    GROUP BY sc.SupplierCompanyID;
