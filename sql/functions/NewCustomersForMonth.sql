---Кількість нових споживачів за місяць, за сезон, за рік:
-- For month
CREATE FUNCTION GetNewCustomersByMonth(@Month INT, @Year INT)
RETURNS INT
AS
BEGIN
    DECLARE @NewCustomers INT;

    SELECT @NewCustomers = COUNT(*)
    FROM Customers
    WHERE MONTH(CreateDate) = @Month AND YEAR(CreateDate) = @Year;

    RETURN @NewCustomers;
END;

