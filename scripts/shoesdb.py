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
BrandGenerator
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
    ("Brands", 50),
    ("Materials", 50),
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
    ("Orders", 1000),
    ("OrderDetails", 500),
    ("Supplies", 200),
    ("Calculation", 500),
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
            BrandGenerator(
                ["Nike", "Adidas", "Puma", "Reebok", "New Balance", "Vans", "Converse", "Under Armour", "Skechers",
                 "ASICS", "Fila", "Salomon", "Timberland", "Lacoste", "Brooks", "Merrell", "DC Shoes", "Birkenstock",
                 "UGG", "Crocs", "Clarks", "Dr. Martens", "Havaianas", "Burberry", "Gucci", "Prada", "Louis Vuitton",
                 "Fendi", "Versace", "Balenciaga", "Chanel", "Hermes", "Givenchy", "Valentino", "Dior", "Yeezy",
                 "Supreme", "Off-White", "Balmain", "Tom Ford", "Alexander McQueen", "Saint Laurent", "Bottega Veneta",
                 "Miu Miu", "Jimmy Choo", "Stella McCartney", "Christian Louboutin", "Ralph Lauren", "Calvin Klein",
                 "Michael Kors", "Hugo Boss", "Guess"]
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
                ["Leather", "Suede", "Canvas", "Mesh", "Knit", "Synthetic", "Nubuck", "Patent Leather", "Rubber",
                 "Cork", "Denim", "Linen", "Wool", "Velvet", "Faux Fur", "Shearling", "Neoprene", "EVA Foam", "Latex",
                 "PVC", "Microfiber", "Silk", "Satin", "Gore-Tex", "Kevlar", "Nylon", "Polyester", "Acrylic",
                 "Polyurethane", "Spandex", "Mesh Nylon", "Knit Mesh", "Cotton", "Bamboo", "Hemp", "Jute", "Lycra",
                 "Rayon", "Elastane", "Ramie", "Sisal", "Felt", "Foam Rubber", "Fleece", "Chenille", "Jacquard",
                 "Tweed", "Flannel", "Corduroy", "Twill"]

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
            ("'"+str(key)+"'" for key in dimensions for _ in range(len(sizes[key]))),
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
            ChoiceGenerator(
                ["Classic", "Sneaker", "Runner", "Sporty", "Casual", "Vintage", "High-top", "Low-top", "Slip-on",
                 "Loafer", "Oxford", "Boot", "Chelsea", "Ankle", "Moccasin", "Wedge", "Platform", "Sandals",
                 "Flip Flops", "Espadrilles"]
            ),
            IntegerNumberGenerator(start=1, end=50),  # BrandID
            ChoiceGenerator(["male", "female"]),
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
            ChoiceGenerator(
                ["Comfortable", "Stylish", "Versatile", "Durable", "Fashionable", "Elegant", "Sleek", "Sporty",
                 "Classic", "Trendy", "Cozy", "Chic", "Modern", "Sophisticated", "Casual", "Premium", "Vintage",
                 "Contemporary", "Unique", "Refined", "Timeless", "Functional", "Luxurious", "Innovative",
                 "Flexible", "Breathable", "Lightweight", "Cushioned", "Supportive", "Waterproof", "Glamorous",
                 "Bold", "Exquisite", "Handcrafted", "High-quality", "Distinctive", "Adaptable", "Practical",
                 "Gentle", "Vibrant", "Statement-making", "Eco-friendly", "Traction", "Padded", "Polished",
                 "Weather-resistant", "Versatile", "Performance-driven", "Sustainable", "Sleek"]),
            ProductStaticIDGenerator(),
            IntegerNumberGenerator(start=1, end=100),  # ProductsPriceHistoryID
            ChoiceGenerator(["Athletic", "Casual", "Formal", "Sneakers", "Boots", "Sandals", "Slippers", "Loafers",
                             "Flats",
                             "Pumps", "Espadrilles", "Oxfords", "Mules", "Wedges", "Platforms", "Heels",
                             "Running Shoes",
                             "Training Shoes", "Hiking Shoes", "Dress Shoes", "Moccasins", "Slingbacks", "Clogs",
                             "Booties",
                             "Brogues", "Derby", "Monkstraps", "Chelsea Boots", "Chukka Boots", "Ankle Boots",
                             "Lace-up Boots",
                             "Peep Toe", "Mary Janes", "Gladiator Sandals", "Flip Flops", "Slides", "Wingtip",
                             "Tassel Loafers",
                             "Driving Shoes", "Boat Shoes", "Saddle Shoes", "Rain Boots", "Winter Boots", "Chelseas",
                             "Cowboy Boots", "Penny Loafers", "High Tops", "Low Tops", "Spectator Shoes", "Ski Boots"]),

            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
          ]
    elif table_name == "ProductMaterial":
        generators = [
            IntegerNumberGenerator(start=1, end=200),  # ProductID
            IntegerNumberGenerator(start=1, end=50),  # MaterialID
            PercentageGenerator(),
            DateGenerator(start_date, end_date),
            DateGenerator(start_date, end_date),
        ]
    elif table_name == "ProductSize":
        generators = [
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=56),  # SizeID
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
            IntegerNumberGenerator(start=1, end=50),  # BrandID
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
            IntegerNumberGenerator(start=1, end=100)  # DiscountCardID
        ,
        DateGenerator(start_date, end_date),
        DateGenerator(start_date, end_date),

        ]
    elif table_name == "OrderDetails":
        generators = [
            AutoIncermentGenerator(),
            IntegerNumberGenerator(start=1, end=500),  # OrderID
            IntegerNumberGenerator(start=1, end=500),  # ProductID
            IntegerNumberGenerator(start=1, end=100),
            FloatNumberGenerator(start=1.0, end=10000.0, precision=1),
        DateGenerator(start_date, end_date),
        DateGenerator(start_date, end_date)
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
            FloatNumberGenerator(start=1.0, end=1.0, precision=2),
            FloatNumberGenerator(start=1.0, end=3000.0, precision=2),
            FloatNumberGenerator(start=1.0, end=5000.0, precision=2),
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
