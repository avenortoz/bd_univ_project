from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


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
    server = "thesoleplate.ccxpddhrdedh.us-east-1.rds.amazonaws.com"
    database = "thesoleplate"
    driver = "ODBC Driver 17 for SQL Server"

    username = "tsp"
    password = "12345678"
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
        return jsonify(result)
    return jsonify(result)


# FIX: returns nothing
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


if __name__ == "__main__":
    connection, cursor = get_db_connection()

    # for statement in generateDB().split(';'):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()
    #
    #
    #
    #
    #
    # for statement in insertValuesInDB().split(';'):
    #     if statement.strip():
    #         try:
    #             cursor.execute(statement)
    #             connection.commit()
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             connection.rollback()
    # connection.commit()

    for statement in dropFunctionsInDB().split(";"):
        if statement.strip():
            try:
                cursor.execute(statement)
                connection.commit()
            except Exception as e:
                print("An error occurred:", e)
                connection.rollback()
    connection.commit()

    for statement in createFunctionsInDB().split(";"):
        if statement.strip():
            try:
                cursor.execute(statement)
                connection.commit()
            except Exception as e:
                print("An error occurred:", e)
                connection.rollback()
    connection.commit()
    connection.close()

    app.run(debug=True)
