from flask import Flask, jsonify
# from flask_cors import CORS
import pyodbc

app = Flask(__name__)


# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


def readFunctionFromFile(nameFile):
    file_path = nameFile
    with open(file_path, "rb") as file:
        content = file.read()
    if content.startswith(b"\xef\xbb\xbf"):
        content = content[3:]
    with open(file_path, "wb") as file:
        file.write(content)
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents


def dropFunctionsInDB():
    return readFunctionFromFile("sql/drop.sql")


def createFunctionsInDB():
    return readFunctionFromFile("sql/function.sql")


def insertValuesInDB():
    return readFunctionFromFile("sql/fill.sql")



def get_db_connection():
   server = ''
   database = ''
   driver = 'ODBC Driver 17 for SQL Server'

   username = ""
   password = ""
   connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

   cnxn = pyodbc.connect(connection_string)
   cursor = cnxn.cursor()
   return cnxn, cursor

def generateDB():
    return readFunctionFromFile("sql/database.sql")


@app.route("/")
def home():
    return "Hello, world!"


# Середня ціна продуктів за брендом
@app.route("/average-product-price-by-brand")
def get_average_product_price_by_brand():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetAverageProductPriceByBrand()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік
@app.route("/brand-sales-by-part-of-year/<int:start_month>/<int:year>")
def get_brand_sales_by_part_of_year(start_month, year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetBrandSalesByPartOfYear(?, ?)", (start_month, year))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік - за місяць
@app.route("/brand-sales-by-month/<int:month>/<int:year>")
def get_brand_sales_by_month(month, year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetBrandSalesByMonth(?, ?)", (month, year))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Кількість проданих пар для бренду, за місяць, за 3 місяці, за рік - за рік
@app.route("/brand-sales-by-year/<int:year>")
def get_brand_sales_by_year(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetBrandsSalesByYear(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# FIX: return empty array
# Скільки кожна компанія доставляє взуття
@app.route("/company-shoe-deliveries")
def get_company_shoe_deliveries():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCompanyShoeDeliveries()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Витрати за місяць, за 3 місяці, за рік - за місяць
@app.route("/costs-by-month/<int:year>")
def get_costs_by_month(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCostsByMonth(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Витрати за місяць, за 3 місяці, за рік - за рік
@app.route("/costs-by-year")
def get_costs_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCostsByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Втрати на знижках - за місяць
@app.route("/discount-losses-by-month/<int:year>")
def get_discount_losses_by_month(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetDiscountLossesByMonth(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Втрати на знижках - за рік
@app.route("/discount-losses-by-year")
def get_discount_losses_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetDiscountLossesByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# FIX: returns several value with the same month
# Прибуток за місяць, за 3 місяці, за рік - за місяць
@app.route("/profit-by-month/<int:year>")
def get_profit_by_month(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetProfitByMonth(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# FIX: returns nothing
# Прибуток за місяць, за 3 місяці, за рік - за рік
@app.route("/profit-by-year")
def get_profit_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetProfitByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
        connection.close()
    return jsonify(rows)


# Прибуток за сезон
@app.route("/profit-by-season/<int:year>")
def get_profit_by_season(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetProfitBySeason(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Топ-5 активних клієнтів
@app.route("/top-5-active-customers")
def get_top_5_active_customers():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetTop5ActiveCustomers()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# Топ-5 популярних продуктів
@app.route("/top-5-popular-products")
def get_top_5_popular_products():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetTop5PopularProducts()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


# NEW______________________________________________________________________________________

@app.route("/costs-by-part-of-year/<int:year>")
def get_costs_by_part_of_year(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCostsByPartOfYear(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/discount-losses-by-part-of-year/<int:year>")
def get_discount_losses_by_part_of_year(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetDiscountLossesByPartOfYear(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/income-by-year-and-seasons/<int:year>")
def get_income_by_year_and_seasons(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetIncomeByYearAndSeasons(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/income-by-every-month/<int:year>")
def get_income_by_every_month(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetIncomeByEveryMonth(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/income-by-year")
def get_income_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetIncomeByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/job-title-and-salary")
def get_job_title_and_salary():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetJobTitleAndSalary()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/new-customers-by-month-in-year/<int:year>")
def get_new_customers_by_month_in_year(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetNewCustomersByMonthInYear(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/new-customers-by-year")
def get_new_customers_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetNewCustomersByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/new-customers-by-season/<int:year>")
def get_new_customers_by_season(year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetNewCustomersBySeason(?)", (year,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/employee-orders-by-month-in-year/<int:employee_id>/<int:year>")
def get_employee_orders_by_month_in_year(employee_id, year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetEmployeeOrdersByMonthInYear(?, ?)", (employee_id, year))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/employee-orders-by-seasons/<int:employee_id>/<int:year>")
def get_employee_orders_by_seasons(employee_id, year):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetEmployeeOrdersBySeasons(?, ?)", (employee_id, year))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/employee-orders-by-all-years/<int:employee_id>")
def get_employee_orders_by_all_years(employee_id):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetEmployeeOrdersByAllYears(?)", (employee_id,))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/pairs-by-price-range/<int:min_price>/<int:max_price>")
def get_pairs_by_price_range(min_price, max_price):
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetPairsByPriceRange(?, ?)", (min_price, max_price))
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/purchased-shoe-sizes")
def get_purchased_shoe_sizes():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetPurchasedShoeSizes()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/sales-percentage-by-material")
def get_sales_percentage_by_material():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetSalesPercentageByMaterial()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/shoe-type-percentage")
def get_shoe_type_percentage():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetShoeTypePercentage()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/shoe-type-percentage-by-brand")
def get_shoe_type_percentage_by_brand():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetShoeTypePercentageByBrand()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/shoe-type-percentage-by-company")
def get_shoe_type_percentage_by_company():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetShoeTypePercentageByCompany()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/customers-by-sex")
def get_customers_by_sex():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCustomersBySex()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/monthly-sales-by-sex")
def get_monthly_sales_by_sex():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetMonthlySalesBySex()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/supplier-pairs-percentage")
def get_supplier_pairs_percentage():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetSupplierPairsPercentage()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/shoe-type-sales-by-year")
def get_shoe_type_sales_by_year():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetShoeTypeSalesByYear()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)


@app.route("/shoe-type-sales-by-season/<int:year>")
def get_shoe_type_sales_by_season(year):
    connection, cursor = get_db_connection()
    cursor.execute(f"SELECT * FROM GetShoeTypeSalesBySeason({year})")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)

@app.route("/customers/sex/m")
def get_customers_by_sex_m():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCustomersBySexM()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)
@app.route("/customers/sex/w")
def get_customers_by_sex_w():
    connection, cursor = get_db_connection()
    cursor.execute("SELECT * FROM GetCustomersBySexW()")
    rows = cursor.fetchall()
    result = []
    column_names = [column_name[0] for column_name in cursor.description]
    for row in rows:
        result.append({column_names[i]: value for i, value in enumerate(row)})
    connection.close()
    return jsonify(result)

if __name__ == "__main__":
    connection, cursor = get_db_connection()

    # print("\n-------------------------------------------------------------------------------------------------\n")
    #
    # for statement in dropFunctionsInDB().split(';'):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()
    # print(
    #     "\n-------------------------------------------------------------------------------------------------\n"
    # )
    # #
    # for statement in generateDB().split(";"):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()

    # #
    # #
    #
    #
    # print("\n-------------------------------------------------------------------------------------------------\n")
    # for statement in insertValuesInDB().split(';'):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()
    # for statement in createFunctionsInDB().split(';'):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()
    connection.close()

    app.run(debug=True)
