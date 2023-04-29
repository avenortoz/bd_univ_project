--Середня ціна продуктів за брендом:
CREATE FUNCTION GetAverageProductPriceByBrand()
RETURNS TABLE
AS
RETURN
    SELECT
        b.Name AS BrandName,
        AVG(p.Price) AS AveragePrice
    FROM Brands b
    JOIN Products p ON b.BrandID = p.BrandID
    GROUP BY b.Name;

--Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
CREATE FUNCTION GetBrandSalesByPartOfYear(@PartOfYear INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        b.Name AS BrandName,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Brands b ON p.BrandID = b.BrandID
    WHERE (MONTH(o.CreateDate) - 1) / 3 = (@PartOfYear - 1) AND YEAR(o.CreateDate) = @Year
    GROUP BY b.Name;

--Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetBrandSalesByMonth(@Month INT, @Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        b.Name AS BrandName,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Brands b ON p.BrandID = b.BrandID
    WHERE MONTH(o.CreateDate) = @Month AND YEAR(o.CreateDate) = @Year
    GROUP BY b.Name;

--Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
-- For year
CREATE FUNCTION GetBrandsSalesByYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        b.Name AS BrandName,
        SUM(od.Quantity) AS NumberOfPairsSold
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Brands b ON p.BrandID = b.BrandID
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY b.Name;

--Скільки кожна компанія доставляє взуття:
CREATE FUNCTION GetCompanyShoeDeliveries()
RETURNS TABLE
AS
RETURN
    SELECT
        sc.Name AS CompanyName,
        SUM(sp.Units) AS NumberOfPairs
    FROM Supplies sp
    JOIN SupplierCompany sc ON sp.SupplierCompanyID = sc.SupplierCompanyID
    GROUP BY sc.Name;

--Витрати за місяць, за 3 місяці, за рік:
CREATE FUNCTION GetCostsByPartOfYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        (MONTH(s.DateOfDelivery) - 1) / 3 + 1 AS PartOfYear,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE YEAR(s.DateOfDelivery) = @Year
    GROUP BY (MONTH(s.DateOfDelivery) - 1) / 3
--Витрати за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetCostsByMonth(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        MONTH(s.DateOfDelivery) AS Month,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    WHERE YEAR(s.DateOfDelivery) = @Year
    GROUP BY MONTH(s.DateOfDelivery);

--Витрати за місяць, за 3 місяці, за рік:
-- For year
CREATE FUNCTION GetCostsByYear()
RETURNS TABLE
AS
RETURN
    SELECT
        YEAR(s.DateOfDelivery) AS Year,
        SUM(s.TotalSum) AS Costs
    FROM Supplies s
    GROUP BY YEAR(s.DateOfDelivery);

--Втрати на знижках:
CREATE FUNCTION GetDiscountLossesByMonth(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        MONTH(o.CreateDate) AS Month,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY MONTH(o.CreateDate);

CREATE FUNCTION GetDiscountLossesByPartOfYear(@Year INT)
RETURNS TABLE
AS
RETURN
    SELECT
        (MONTH(o.CreateDate) - 1) / 3 + 1 AS PartOfYear,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY (MONTH(o.CreateDate) - 1) / 3 + 1;

CREATE FUNCTION GetDiscountLossesByYear()
RETURNS TABLE
AS
RETURN
    SELECT
        YEAR(o.CreateDate) AS Year,
        SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
    FROM Orders o
    GROUP BY YEAR(o.CreateDate);
