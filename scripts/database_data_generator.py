import random
from datetime import datetime, timedelta

# Define a list of sample brand names and email domains
brand_names = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "New Balance"]
email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

# Define a function to generate a random date within the past 6 months
def random_date():
    now = datetime.now()
    delta = timedelta(days=random.randint(1, 180))
    return (now - delta).strftime("%Y-%m-%d")


# Generate 100 random rows of data for the Brands table
brands = []
for i in range(1, 101):
    name = random.choice(brand_names)
    email = f"{name.lower()}@{random.choice(email_domains)}"
    suppliers_brands = ",".join(random.sample(brand_names, random.randint(1, 4)))
    create_date = random_date()
    update_date = random_date()
    brands.append((i, name, email, suppliers_brands, create_date, update_date))

# Write the data to a SQL insert script file
with open("brands.sql", "w") as f:
    for brand in brands:
        f.write(
            f"INSERT INTO Brands (BrandID, Name, Email, SuppliersBrands, CreateDate, UpdateDate) VALUES ({brand[0]}, '{brand[1]}', '{brand[2]}', '{brand[3]}', '{brand[4]}', '{brand[5]}');\n"
        )
