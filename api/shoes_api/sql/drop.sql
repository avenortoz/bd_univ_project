DROP TABLE IF EXISTS Calculation;
DROP TABLE IF EXISTS Supplies;
DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS SupplierCompanyBrands;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS SupplierCompany;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS ProductSize;
DROP TABLE IF EXISTS ProductMaterial;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS ProductsPriceHistory;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Brands;
DROP TABLE IF EXISTS DiscountCards;

DROP FUNCTION GetCustomersBySexW;
DROP FUNCTION GetCustomersBySexM;
DROP FUNCTION GetAverageProductPriceByBrand;
DROP FUNCTION GetBrandSalesByPartOfYear;
DROP FUNCTION GetBrandSalesByMonth;
DROP FUNCTION GetBrandsSalesByYear;
DROP FUNCTION GetEmployeeOrdersByMonthInYear;
DROP FUNCTION GetCompanyShoeDeliveries;
DROP FUNCTION GetCostsByPartOfYear;
DROP FUNCTION GetCostsByMonth;
DROP FUNCTION GetCostsByYear;
DROP FUNCTION GetDiscountLossesByMonth;
DROP FUNCTION GetDiscountLossesByPartOfYear;
DROP FUNCTION GetDiscountLossesByYear;
DROP FUNCTION GetIncomeByYearAndSeasons;
DROP FUNCTION GetIncomeByEveryMonth;
DROP FUNCTION GetIncomeByYear;
DROP FUNCTION GetJobTitleAndSalary;
DROP FUNCTION GetNewCustomersByMonthInYear;
DROP FUNCTION GetNewCustomersBySeason;
DROP FUNCTION GetNewCustomersByYear;
DROP FUNCTION GetEmployeeOrdersByMonth;
DROP FUNCTION GetEmployeeOrdersBySeasons;
DROP FUNCTION GetEmployeeOrdersByAllYears;
DROP FUNCTION GetPairsByPriceRange;
DROP FUNCTION GetProfitBySeason;
DROP FUNCTION GetProfitByMonth;
DROP FUNCTION GetProfitByYear;
DROP FUNCTION GetPurchasedShoeSizes;
DROP FUNCTION GetSalesPercentageByMaterial;
DROP FUNCTION GetShoeTypePercentage;
DROP FUNCTION GetShoeTypePercentageByBrand;
DROP FUNCTION GetShoeTypePercentageByCompany;
DROP FUNCTION GetCustomersBySex;
DROP FUNCTION GetMonthlySalesBySex;
DROP FUNCTION GetSupplierPairsPercentage;
DROP FUNCTION GetShoeTypeSalesByYear;
DROP FUNCTION GetShoeTypeSalesByMonth;
DROP FUNCTION GetShoeTypeSalesBySeason;
DROP FUNCTION GetTop5ActiveCustomers;
DROP FUNCTION GetTop5PopularProducts;
