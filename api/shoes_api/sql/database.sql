CREATE TABLE DiscountCards (
    DiscountCardID INT PRIMARY KEY,
    Discount DECIMAL(5,2),
    IssueDate DATE,
    ExpireDate DATE
);

CREATE TABLE Brands (
    BrandID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100),
    SuppliersBrands VARCHAR(200),
	CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY,
    Name VARCHAR(50),
	CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Sizes (
    SizeID INT PRIMARY KEY,
    Size VARCHAR(50),
    Dimension VARCHAR(50),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Sex VARCHAR(10),
    Birthday DATE,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PhoneNumber VARCHAR(20),
    EmailAddress VARCHAR(100),
    DiscountCardID INT REFERENCES DiscountCards(DiscountCardID),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE ProductsPriceHistory (
    ProductsPriceHistoryID INT PRIMARY KEY,
	Price Money,
	TimeCreated date,
	ProductsPricePreviousID INT REFERENCES ProductsPriceHistory(ProductsPriceHistoryID) NULL
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    BrandID INT REFERENCES Brands(BrandID),
    Sex VARCHAR(10),
    ProductSize VARCHAR(50),
    Color VARCHAR(50),
    Price MONEY,
    Description TEXT,
    ProductStaticID INT,
    ProductsPriceHistoryID INT REFERENCES ProductsPriceHistory(ProductsPriceHistoryID),
    Category VARCHAR(200),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE ProductMaterial (
    ProductID INT,
    MaterialID INT,
    Percentage DECIMAL(5,2),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
    PRIMARY KEY (ProductID, MaterialID),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE ProductSize (
    ProductID INT,
    SizeID INT,
    Units INT,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID),
    PRIMARY KEY (ProductID, SizeID),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address VARCHAR(100),
    City VARCHAR(50),
    PhoneNumber VARCHAR(20),
    JobTitle VARCHAR(50),
    Salary MONEY,
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE SupplierCompany (
    SupplierCompanyID INT PRIMARY KEY,
    Name VARCHAR(100),
    DeliveryTime VARCHAR(50),
    DeliveryPrice MONEY,
    Email VARCHAR(100),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierCompanyID INT REFERENCES SupplierCompany(SupplierCompanyID),
    Name VARCHAR(50),
    Surname VARCHAR(50),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);


CREATE TABLE SupplierCompanyBrands (
    SupplierCompanyID INT,
    BrandID INT,
    PRIMARY KEY (SupplierCompanyID, BrandID),
    FOREIGN KEY (SupplierCompanyID) REFERENCES SupplierCompany(SupplierCompanyID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID),
	  CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID),
    CustomerID INT REFERENCES Customers(CustomerID),
    TotalPrice Money,
    TotalPriceWithDiscount Money,
    DiscountCardID INT REFERENCES DiscountCards(DiscountCardID),
    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT,
    Price Money,

    CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

CREATE TABLE Supplies (
    SupplyID INT PRIMARY KEY,
    SupplierCompanyID INT FOREIGN KEY REFERENCES SupplierCompany(SupplierCompanyID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Units INT,
    DateOfDelivery DATE,
	TotalSum Money,
	CreateDate DATE DEFAULT GETDATE(),
    UpdateDate DATE DEFAULT GETDATE()
);

Create Table Calculation(
    CalculationID INT primary key,
    Costs money,
    Income money,
    Profit money,
    DATE DATE DEFAULT getDate()
);
