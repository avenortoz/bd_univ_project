import datetime
import random
from util.mygenerators import (
    IntegerNumberGenerator,
    AutoIncermentGenerator,
    ChoiceGenerator,
    ChoiceGeneratorInteger,
    DateGenerator,
    EmailGenerator,
    FirstnameGenerator,
    FloatNumberGenerator,
    LastnameGenerator,
    PhoneGenerator,
    StaticNumberGenerator,
    insert_into_table,
)


class PercentageGenerator(FloatNumberGenerator):
    def __init__(self):
        super().__init__(start=0.0, end=100.0, precision=2)


class ProductStaticIDGenerator(AutoIncermentGenerator):
    def __init__(self):
        super().__init__(n=1000)


class SuppliesTotalSumGenerator(FloatNumberGenerator):
    def __init__(self):
        super().__init__(start=100.0, end=10000.0, precision=2)


# Start date and end date for DateGenerator
start_date = datetime.datetime(year=2010, month=1, day=1)
end_date = datetime.datetime(year=2023, month=1, day=1)

tables = [
    ("DiscountCards", 100),
    ("Brands", 100),
    ("Materials", 7),
    ("Sizes", 56),
    ("Customers", 100),
    ("ProductsPriceHistory", 100),
    ("Products", 500),
    ("ProductMaterial", 100),
    ("ProductSize", 100),
    ("Employees", 100),
    ("SupplierCompany", 100),
    ("Suppliers", 100),
    ("SupplierCompanyBrands", 100),
    ("Orders", 500),
    ("OrderDetails", 500),
    ("Supplies", 100),
    ("Calculation", 100),
]


def generate_data(table_name):
    generators = []
    if table_name == "DiscountCards":
        generators = [
            AutoIncermentGenerator(),
            ChoiceGeneratorInteger([0.01, 0.03, 0.05]),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Brands":
        generators = [
            AutoIncermentGenerator(),
            ChoiceGenerator(
                ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "New Balance"]
            ),
            EmailGenerator(),
            LastnameGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Materials":
        generators = [
            AutoIncermentGenerator(),
            ChoiceGenerator(
                [
                    "Canvas",
                    "Leather",
                    "Mesh",
                    "Rubber",
                    "Rubber sole",
                    "Synthetic sole",
                    "Textile",
                ]
            ),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Sizes":
        dimensions = ["US", "EU", "UKR"]
        sizes = {
            "US": [
                4,
                4.5,
                5,
                5.5,
                6,
                6.5,
                7,
                7.5,
                8,
                8.5,
                9,
                9.5,
                10,
                10.5,
                11,
                11.5,
                12,
                12.5,
                13,
            ],
            "EU": [
                35,
                35.5,
                36,
                37,
                37.5,
                38,
                38.5,
                39,
                40,
                40.5,
                41,
                42,
                42.5,
                43,
                44,
                44.5,
                45,
                46,
                47,
            ],
            "UKR": [
                33,
                33.5,
                34,
                35,
                35.5,
                36,
                36.5,
                37,
                38,
                38.5,
                39,
                40,
                40.5,
                41,
                42,
                42.5,
                43,
                44,
                44.5,
            ],
        }
        generators = [
            AutoIncermentGenerator(),
            (str(key) for key in dimensions for _ in range(len(sizes[key]))),
            (str(i) for i in sum(sizes.values(), [])),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Customers":
        generators = [
            AutoIncermentGenerator(),
            ChoiceGenerator(["male", "female"]),
            DateGenerator(start_date, end_date),
            FirstnameGenerator(),
            LastnameGenerator(),
            PhoneGenerator(),
            EmailGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # DiscountCardID
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "ProductsPriceHistory":
        generators = [
            AutoIncermentGenerator(),
            FloatNumberGenerator(start=25.0, end=1000.0, precision=2),
            DateGenerator(start_date, end_date),
            IntegerNumberGenerator(start=1, end=10),  # ProductsPricePreviousID
        ]
    elif table_name == "Products":
        generators = [
            AutoIncermentGenerator(),
            FirstnameGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # BrandID
            ChoiceGenerator(["male", "female"]),
            FirstnameGenerator(),  # TODO: What does it mean(see table Products ProductSize)
            ChoiceGenerator(
                [
                    "red", "orange", "yellow",
                    "green", "blue", "purple",
                    "pink", "brown", "gray",
                    "black", "white", "beige",
                    "other"
                ]
            ),
            FloatNumberGenerator(start=25.0, end=1000.0, precision=1),
            FirstnameGenerator(),
            ProductStaticIDGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # ProductsPriceHistoryID
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "ProductMaterial":
        generators = [
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=100),  # MaterialID
            PercentageGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "ProductSize":
        generators = [
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=100),  # SizeID
            IntegerNumberGenerator(start=5, end=50),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Employees":
        generators = [
            AutoIncermentGenerator(),
            FirstnameGenerator(),
            LastnameGenerator(),
            FirstnameGenerator(),
            FirstnameGenerator(),
            PhoneGenerator(),
            FirstnameGenerator(),
            FloatNumberGenerator(start=1000.0, end=10000.0, precision=1),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "SupplierCompany":
        generators = [
            AutoIncermentGenerator(),
            FirstnameGenerator(),
            LastnameGenerator(),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=1),
            EmailGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Suppliers":
        generators = [
            AutoIncermentGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # SupplierCompanyID
            FirstnameGenerator(),
            LastnameGenerator(),
            PhoneGenerator(),
            EmailGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "SupplierCompanyBrands":
        generators = [
            IntegerNumberGenerator(start=1, end=100),  # SupplierCompanyID
            IntegerNumberGenerator(start=1, end=100),  # BrandID
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Orders":
        generators = [
            AutoIncermentGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # EmployeeID
            IntegerNumberGenerator(start=1, end=100),  # CustomerID
            FloatNumberGenerator(start=1.0, end=10000.0, precision=1),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=1),
            IntegerNumberGenerator(start=1, end=100),  # DiscountCardID
        ]
    elif table_name == "OrderDetails":
        generators = [
            AutoIncermentGenerator(),
            IntegerNumberGenerator(start=1, end=500),  # OrderID
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=100),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=1),
        ]
    elif table_name == "Supplies":
        generators = [
            AutoIncermentGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # SupplierCompanyID
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=100),
            DateGenerator(start_date, end_date),
            SuppliesTotalSumGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "Calculation":
        generators = [
            AutoIncermentGenerator(),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=2),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=2),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=2),
            DateGenerator(start_date, end_date),
        ]
    return generators


if __name__ == "__main__":
    with open("fill.sql", "wt+") as fd:
        for tablename, count in tables:
            print(
                insert_into_table(
                    name=tablename, generators=generate_data(tablename), n=count
                ),
                file=fd,
            )
