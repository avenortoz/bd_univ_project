---Статистика по покупцях Customers чоловіки - жінки
CREATE FUNCTION GetCustomersBySex()
RETURNS TABLE
AS
RETURN
    SELECT 
        Sex, 
        COUNT(*) AS NumberOfCustomers 
    FROM Customers 
    GROUP BY Sex;
