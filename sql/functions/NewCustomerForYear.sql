--Кількість нових споживачів за місяць, за сезон, за рік:

-- For year
CREATE FUNCTION GetNewCustomersByYear(@Year INT)
RETURNS INT
AS
BEGIN
    DECLARE @NewCustomers INT;

    SELECT @NewCustomers = COUNT(*)
    FROM Customers
    WHERE YEAR(CreateDate) = @Year;

    RETURN @NewCustomers;
END;