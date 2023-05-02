-- Середня ціна продуктів за брендом:
CREATE FUNCTION GetAverageProductPriceByBrand()
    RETURNS TABLE AS
RETURN
SELECT b.Name       AS BrandName,
       AVG(p.Price) AS AveragePrice
FROM Brands b
         JOIN Products p ON b.BrandID = p.BrandID
GROUP BY b.Name;

-- Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
CREATE FUNCTION GetBrandSalesByPartOfYear(@PartOfYear INT, @Year INT)
    RETURNS TABLE AS
RETURN
SELECT b.Name           AS BrandName,
       SUM(od.Quantity) AS NumberOfPairsSold
FROM Orders o
         JOIN OrderDetails od ON o.OrderID = od.OrderID
         JOIN Products p ON od.ProductID = p.ProductID
         JOIN Brands b ON p.BrandID = b.BrandID
WHERE (MONTH(o.CreateDate) - 1) / 3 = (@PartOfYear - 1) AND YEAR (o.CreateDate) = @Year
GROUP BY b.Name;

-- Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetBrandSalesByMonth(@Month INT, @Year INT)
    RETURNS TABLE AS
RETURN
SELECT b.Name           AS BrandName,
       SUM(od.Quantity) AS NumberOfPairsSold
FROM Orders o
         JOIN OrderDetails od ON o.OrderID = od.OrderID
         JOIN Products p ON od.ProductID = p.ProductID
         JOIN Brands b ON p.BrandID = b.BrandID
WHERE MONTH (o.CreateDate) = @Month AND YEAR (o.CreateDate) = @Year
GROUP BY b.Name;

-- Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік:
-- For year
CREATE FUNCTION GetBrandsSalesByYear(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT b.Name           AS BrandName,
       SUM(od.Quantity) AS NumberOfPairsSold
FROM Orders o
         JOIN OrderDetails od ON o.OrderID = od.OrderID
         JOIN Products p ON od.ProductID = p.ProductID
         JOIN Brands b ON p.BrandID = b.BrandID
WHERE YEAR (o.CreateDate) = @Year
GROUP BY b.Name;

-- Скільки кожна компанія доставляє взуття:
CREATE FUNCTION GetCompanyShoeDeliveries()
    RETURNS TABLE AS
RETURN
SELECT sc.Name       AS CompanyName,
       SUM(sp.Units) AS NumberOfPairs
FROM Supplies sp
         JOIN SupplierCompany sc ON sp.SupplierCompanyID = sc.SupplierCompanyID
GROUP BY sc.Name;

-- Витрати за місяць, за 3 місяці, за рік:
CREATE FUNCTION GetCostsByPartOfYear(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT (MONTH(s.DateOfDelivery) - 1) / 3 + 1 AS PartOfYear,
       SUM(s.TotalSum)                       AS Costs
FROM Supplies s
WHERE YEAR (s.DateOfDelivery) = @Year
GROUP BY (MONTH (s.DateOfDelivery) - 1) / 3 + 1;

-- Витрати за місяць, за 3 місяці, за рік:
-- For month
CREATE FUNCTION GetCostsByMonth(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT MONTH (s.DateOfDelivery) AS Month, SUM (s.TotalSum) AS Costs
FROM Supplies s
WHERE YEAR (s.DateOfDelivery) = @Year
GROUP BY MONTH (s.DateOfDelivery);

-- Витрати за місяць, за 3 місяці, за рік:
-- For year
CREATE FUNCTION GetCostsByYear()
    RETURNS TABLE AS
RETURN
SELECT YEAR (s.DateOfDelivery) AS Year, SUM (s.TotalSum) AS Costs
FROM Supplies s
GROUP BY YEAR (s.DateOfDelivery);

-- Втрати на знижках:
CREATE FUNCTION GetDiscountLossesByMonth(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT MONTH (o.CreateDate) AS Month, SUM (o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
FROM Orders o
WHERE YEAR (o.CreateDate) = @Year
GROUP BY MONTH (o.CreateDate);

CREATE FUNCTION GetDiscountLossesByPartOfYear(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT (MONTH(o.CreateDate) - 1) / 3 + 1 AS PartOfYear, SUM(o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
FROM Orders o
WHERE YEAR (o.CreateDate) = @Year
GROUP BY (MONTH (o.CreateDate) - 1) / 3 + 1;

CREATE FUNCTION GetDiscountLossesByYear()
    RETURNS TABLE AS
RETURN
SELECT YEAR (o.CreateDate) AS Year, SUM (o.TotalPrice - o.TotalPriceWithDiscount) AS DiscountLosses
FROM Orders o
GROUP BY YEAR (o.CreateDate);

CREATE FUNCTION GetIncomeByYearAndSeasons(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT @Year AS Year,
        (SELECT SUM(TotalPrice) FROM Orders WHERE YEAR(CreateDate) = @Year AND MONTH(CreateDate) BETWEEN 1 AND 3) AS Season1Income,
        (SELECT SUM(TotalPrice) FROM Orders WHERE YEAR(CreateDate) = @Year AND MONTH(CreateDate) BETWEEN 4 AND 6) AS Season2Income,
        (SELECT SUM(TotalPrice) FROM Orders WHERE YEAR(CreateDate) = @Year AND MONTH(CreateDate) BETWEEN 7 AND 9) AS Season3Income,
        (SELECT SUM(TotalPrice) FROM Orders WHERE YEAR(CreateDate) = @Year AND MONTH(CreateDate) BETWEEN 10 AND 12) AS Season4Income;
CREATE FUNCTION GetIncomeByEveryMonth(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT MonthNumber.Month,
       ISNULL(SUM(OrdersIncome.Income), 0) AS Income
FROM (VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12)) AS MonthNumber(Month)
         LEFT JOIN (SELECT MONTH (CreateDate) AS Month, SUM (TotalPrice) AS Income
                    FROM Orders
                    WHERE YEAR (CreateDate) = @Year
                    GROUP BY MONTH (CreateDate)) AS OrdersIncome ON MonthNumber.Month = OrdersIncome.Month
GROUP BY MonthNumber.Month;

CREATE FUNCTION GetIncomeByYear()
    RETURNS TABLE AS
RETURN
SELECT YEAR (o.CreateDate) AS Year, SUM (o.TotalPrice) AS Income
FROM Orders o
GROUP BY YEAR (o.CreateDate);



-- Витрати за місяць, за 3 місяці, за рік:
-- For year
CREATE FUNCTION GetJobTitleAndSalary()
    RETURNS TABLE AS
RETURN
SELECT JobTitle, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY JobTitle;

CREATE FUNCTION GetNewCustomersByMonthInYear(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT
    MONTH (CreateDate) AS Month, COUNT (*) AS NewCustomers
FROM Customers
WHERE YEAR (CreateDate) = @Year
GROUP BY MONTH (CreateDate);



CREATE FUNCTION GetNewCustomersBySeason(@Year INT)
RETURNS TABLE AS
RETURN
SELECT
    @Year AS Year,
    CASE
        WHEN MONTH(CreateDate) BETWEEN 1 AND 3 THEN 1
        WHEN MONTH(CreateDate) BETWEEN 4 AND 6 THEN 2
        WHEN MONTH(CreateDate) BETWEEN 7 AND 9 THEN 3
        WHEN MONTH(CreateDate) BETWEEN 10 AND 12 THEN 4
    END AS Season,
    COUNT(*) AS NewCustomers
FROM
    Customers
WHERE
    YEAR(CreateDate) = @Year
GROUP BY
    YEAR(CreateDate),
    CASE
        WHEN MONTH(CreateDate) BETWEEN 1 AND 3 THEN 1
        WHEN MONTH(CreateDate) BETWEEN 4 AND 6 THEN 2
        WHEN MONTH(CreateDate) BETWEEN 7 AND 9 THEN 3
        WHEN MONTH(CreateDate) BETWEEN 10 AND 12 THEN 4
    END;


CREATE FUNCTION GetNewCustomersByYear()
    RETURNS TABLE AS
RETURN
SELECT
    YEAR (CreateDate) AS Year, COUNT (*) AS NewCustomers
FROM Customers
GROUP BY YEAR (CreateDate);

-- -------------------------------------
CREATE FUNCTION GetEmployeeOrdersByMonthInYear(@EmployeeID INT, @Year INT)
    RETURNS TABLE AS
RETURN
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName, MONTH (o.CreateDate) AS Month, SUM (o.TotalPrice) AS TotalPrice
FROM Orders o
    JOIN Employees e
ON e.EmployeeID = @EmployeeID
WHERE YEAR (o.CreateDate) = @Year
GROUP BY CONCAT(e.FirstName, ' ', e.LastName), MONTH (o.CreateDate);

CREATE FUNCTION GetEmployeeOrdersBySeasons(@EmployeeID INT, @Year INT)
    RETURNS TABLE AS
RETURN
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
       COUNT(*)                             AS OrderCount,
       CASE
           WHEN MONTH (o.CreateDate) BETWEEN 1 AND 3 THEN 'Season 1'
        WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 'Season 2'
        WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 'Season 3'
        WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 'Season 4'
END
AS Season
FROM Orders o
JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE o.EmployeeID = @EmployeeID AND YEAR(o.CreateDate) = @Year
GROUP BY e.FirstName, e.LastName,
    CASE
        WHEN MONTH(o.CreateDate) BETWEEN 1 AND 3 THEN 'Season 1'
        WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 'Season 2'
        WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 'Season 3'
        WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 'Season 4'
END;

CREATE FUNCTION GetEmployeeOrdersByAllYears(@EmployeeID INT)
    RETURNS TABLE AS
RETURN
SELECT
    YEAR (o.CreateDate) AS Year, o.OrderID, o.TotalPrice, o.TotalPriceWithDiscount
FROM Orders o
WHERE o.EmployeeID = @EmployeeID;



CREATE FUNCTION GetPairsByPriceRange(@MinPrice MONEY, @MaxPrice MONEY)
    RETURNS TABLE AS
RETURN
SELECT COUNT(*) AS NumberOfPairs
FROM Orders o
         JOIN OrderDetails od ON o.OrderID = od.OrderID
WHERE od.Price BETWEEN @MinPrice AND @MaxPrice;

CREATE FUNCTION GetProfitBySeason(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT (Income - Costs) AS Profit, Season
FROM (
    SELECT
        SUM(o.TotalPrice) AS Income,
        SUM(s.TotalSum) AS Costs,
        CASE
            WHEN MONTH(o.CreateDate) BETWEEN 1 AND 3 THEN 1
            WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 2
            WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 3
            WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 4
        END AS Season
    FROM Orders o
    JOIN Supplies s ON MONTH(s.DateOfDelivery) BETWEEN MONTH(o.CreateDate) AND (MONTH(o.CreateDate) + 2) AND YEAR(s.DateOfDelivery) = @Year
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY CASE
            WHEN MONTH(o.CreateDate) BETWEEN 1 AND 3 THEN 1
            WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 2
            WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 3
            WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 4
        END
) AS Subquery;



CREATE FUNCTION GetProfitByMonth(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT SUM(Income - Costs) AS Profit, Month
FROM (
    SELECT
        SUM(o.TotalPrice) AS Income, SUM(s.TotalSum) AS Costs, MONTH(o.CreateDate) AS Month
    FROM Orders o
    JOIN Supplies s ON MONTH(s.DateOfDelivery) = MONTH(o.CreateDate) AND YEAR(s.DateOfDelivery) = @Year
    WHERE YEAR(o.CreateDate) = @Year
    GROUP BY MONTH(o.CreateDate)
) AS Subquery
GROUP BY Month;

CREATE FUNCTION GetProfitByYear()
    RETURNS TABLE AS
RETURN
SELECT DISTINCT (Income - Costs) AS Profit, Year
FROM (
    SELECT
        SUM(o.TotalPrice) OVER (PARTITION BY YEAR(o.CreateDate)) AS Income,
        SUM(s.TotalSum) OVER (PARTITION BY YEAR(o.CreateDate)) AS Costs,
        YEAR(o.CreateDate) AS Year
    FROM Orders o
    JOIN Supplies s ON YEAR(s.DateOfDelivery) = YEAR(o.CreateDate)
) AS Subquery;

CREATE FUNCTION GetPurchasedShoeSizes()
    RETURNS TABLE AS
RETURN
SELECT p.ProductID,
       p.Name           AS ShoeName,
       ps.SizeID,
       s.Size           AS ShoeSize,
       SUM(od.Quantity) AS NumberOfPairsPurchased
FROM Orders o
         JOIN OrderDetails od ON o.OrderID = od.OrderID
         JOIN Products p ON od.ProductID = p.ProductID
         JOIN ProductSize ps ON p.ProductID = ps.ProductID
         JOIN Sizes s ON ps.SizeID = s.SizeID
GROUP BY p.ProductID, p.Name, ps.SizeID, s.Size;

CREATE FUNCTION GetSalesPercentageByMaterial()
    RETURNS TABLE AS
RETURN
SELECT m.Name                                                                AS MaterialName,
       SUM(od.Quantity)                                                      AS TotalSold,
       (SUM(od.Quantity) * 100.0 / (SELECT SUM(Quantity) FROM OrderDetails)) AS SalesPercentage
FROM Materials m
         JOIN ProductMaterial pm ON m.MaterialID = pm.MaterialID
         JOIN OrderDetails od ON pm.ProductID = od.ProductID
GROUP BY m.Name;



CREATE FUNCTION GetShoeTypePercentage()
    RETURNS TABLE AS
RETURN
SELECT p.Category,
       COUNT(*)                                                                         AS NumberOfShoes,
       (CAST(COUNT(*) AS FLOAT) / CAST((SELECT COUNT(*) FROM Products) AS FLOAT)) * 100 AS Percentage
FROM Products p
GROUP BY p.Category;



CREATE FUNCTION GetShoeTypePercentageByBrand()
    RETURNS TABLE AS
RETURN
SELECT p.Category,
       b.Name,
       COUNT(*)                                                                                                   AS NumberOfShoes,
       (CAST(COUNT(*) AS FLOAT) / CAST((SELECT COUNT(*) FROM Products WHERE BrandID = b.BrandID) AS FLOAT)) *
       100                                                                                                        AS Percentage
FROM Products p
         JOIN Brands b ON p.BrandID = b.BrandID
GROUP BY p.Category, b.Name, b.BrandID;



CREATE FUNCTION GetShoeTypePercentageByCompany()
    RETURNS TABLE AS
RETURN
SELECT p.Category,
       sc.Name,
       COUNT(*)                                                                                              AS NumberOfShoes,
       (CAST(COUNT(*) AS FLOAT) /
        CAST((SELECT COUNT(*) FROM Supplies WHERE SupplierCompanyID = sc.SupplierCompanyID) AS FLOAT)) *
       100                                                                                                   AS Percentage
FROM Products p
         JOIN Supplies s ON p.ProductID = s.ProductID
         JOIN SupplierCompany sc ON s.SupplierCompanyID = sc.SupplierCompanyID
GROUP BY p.Category, sc.Name, sc.SupplierCompanyID;



CREATE FUNCTION GetCustomersBySex()
    RETURNS TABLE AS
RETURN
SELECT Sex,
       COUNT(*) AS NumberOfCustomers
FROM Customers
GROUP BY Sex;

CREATE FUNCTION GetMonthlySalesBySex()
    RETURNS TABLE AS
RETURN
SELECT
    MONTH (o.CreateDate) AS Month, c.Sex, SUM (od.Quantity) AS NumberOfPairsSold
FROM Orders o
    JOIN OrderDetails od
ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY MONTH (o.CreateDate), c.Sex;

CREATE FUNCTION GetSupplierPairsPercentage()
    RETURNS TABLE AS
RETURN
SELECT s.Name + ' ' + s.Surname                                                                AS Supplier,
       SUM(sp.Units)                                                                           AS NumberOfPairs,
       (CAST(SUM(sp.Units) AS FLOAT) / CAST((SELECT SUM(Units) FROM Supplies) AS FLOAT)) * 100 AS Percentage
FROM Supplies sp
         JOIN Suppliers s ON sp.SupplierCompanyID = s.SupplierCompanyID
GROUP BY s.Name, s.Surname;


CREATE FUNCTION GetShoeTypeSalesByYear()
    RETURNS TABLE AS
RETURN
SELECT p.Category,
       SUM(od.Quantity) AS NumberOfPairsSold, YEAR (o.CreateDate) AS Year
FROM Orders o
    JOIN OrderDetails od
ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.Category, YEAR (o.CreateDate);

CREATE FUNCTION GetShoeTypeSalesByMonth(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT p.Category, MONTH (o.CreateDate) AS Month, SUM (od.Quantity) AS NumberOfPairsSold
FROM Orders o
    JOIN OrderDetails od
ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
WHERE YEAR (o.CreateDate) = @Year
GROUP BY p.Category, MONTH (o.CreateDate);



CREATE FUNCTION GetShoeTypeSalesBySeason(@Year INT)
    RETURNS TABLE AS
RETURN
SELECT p.Category,
       CASE
           WHEN MONTH (o.CreateDate) BETWEEN 1 AND 3 THEN 'Season 1'
        WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 'Season 2'
        WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 'Season 3'
        WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 'Season 4'
END
AS Season,
    SUM(od.Quantity) AS NumberOfPairsSold
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE YEAR(o.CreateDate) = @Year
GROUP BY p.Category, CASE
    WHEN MONTH(o.CreateDate) BETWEEN 1 AND 3 THEN 'Season 1'
    WHEN MONTH(o.CreateDate) BETWEEN 4 AND 6 THEN 'Season 2'
    WHEN MONTH(o.CreateDate) BETWEEN 7 AND 9 THEN 'Season 3'
    WHEN MONTH(o.CreateDate) BETWEEN 10 AND 12 THEN 'Season 4'
END;

CREATE FUNCTION GetTop5ActiveCustomers()
    RETURNS TABLE AS
RETURN
SELECT TOP 5
    c.FirstName + ' ' + c.LastName AS CustomerName, COUNT(o.OrderID) AS TotalOrders
FROM Customers c
         JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName
ORDER BY TotalOrders DESC;
ORDER BY TotalOrders DESC;

CREATE FUNCTION GetTop5PopularProducts()
    RETURNS TABLE AS
RETURN
SELECT TOP 5
    p.Name AS ProductName, SUM(od.Quantity) AS TotalSold
FROM Products p
         JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.Name
ORDER BY TotalSold DESC;

CREATE FUNCTION GetCustomersBySexM()
   RETURNS TABLE AS
RETURN
SELECT *
FROM StatisticsValues
WHERE Sex = 'm';

CREATE FUNCTION GetCustomersBySexW()
   RETURNS TABLE AS
RETURN
SELECT *
FROM StatisticsValues
WHERE Sex = 'w';

