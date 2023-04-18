--Кількість нових споживачів за місяць, за сезон, за рік:
-- For season
CREATE FUNCTION GetNewCustomersBySeason(@Season INT, @Year INT)
RETURNS INT
AS
BEGIN
    DECLARE @NewCustomers INT;
    DECLARE @StartMonth INT;
    DECLARE @EndMonth INT;

    IF @Season = 1
    BEGIN
        SET @StartMonth = 1;
        SET @EndMonth = 3;
    END;
    ELSE IF @Season = 2
    BEGIN
        SET @StartMonth = 4;
        SET @EndMonth = 6;
    END;
    ELSE IF @Season = 3
    BEGIN
        SET @StartMonth = 7;
        SET @EndMonth = 9;
    END;
    ELSE IF @Season = 4
    BEGIN
        SET @StartMonth = 10;
        SET @EndMonth = 12;
    END;
    ELSE
        RETURN NULL;

    SELECT @NewCustomers = COUNT(*)
    FROM Customers
    WHERE MONTH(CreateDate) BETWEEN @StartMonth AND @EndMonth AND YEAR(CreateDate) = @Year;

    RETURN @NewCustomers;
END;
