from flask import Flask
import pyodbc


app = Flask(__name__)



# def get_db_connection():
   # server = 'thesoleplate.ccxpddhrdedh.us-east-1.rds.amazonaws.com'
   # database = 'thesoleplate'
   # driver = 'ODBC Driver 17 for SQL Server'
   #
   # username = "tsp"
   # password = "12345678a-"
   # connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
   #
   # cnxn = pyodbc.connect(connection_string)
   # cursor = cnxn.cursor()
   # return cnxn, cursor


def get_db_connection():
   server = 'DESKTOP-5RO5PMS'
   database = 't'
   driver = '{ODBC Driver 17 for SQL Server}'


   connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes"


   cnxn = pyodbc.connect(connection_string)


   cursor = cnxn.cursor()
   return cnxn, cursor




def generateDB():
   return readFunctionFromFile('sql/database.sql')
def createAllFunctions(cursor):
   cursor.execute(readFunctionFromFile('sql/functions/AverageProductPriceByBrand.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/BrandSalesBy3Months.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/BrandSalesByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/BrandSalesByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/CompanyShoeDeliveries.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/CostsBy3Months.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/CostsByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/CostsByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/DiscountLosses.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/IncomeBy3Months.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/IncomeByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/IncomeByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/JobTitleAndSalary.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/NewCustomerForSeason.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/NewCustomerForYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/NewCustomersForMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/OrdersByEmployeeMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/OrdersByEmployeeSeason.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/OrdersByEmployeeYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/PairsByPriceRangeByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/PairsByPriceRangeByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ProfitBy3Months.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ProfitByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ProfitByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/PurchasedShoeSizes.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/SalesPercentageByMaterial.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypePercentage.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypePercentageByBran.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypePercentageByCompany.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypeSalesBy3Months.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypeSalesByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/ShoeTypeSalesByYear.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/StatisticsByMonthBySex.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/StatisticsBySex.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/SupplierPairsPercentage.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/SuppliesByMonth.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/Top5ActiveCustomers.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/Top5PopularProducts.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/TotalPairsPurchased.sql'))
   cursor.execute(readFunctionFromFile('sql/functions/TotalProductsInStock.sql'))




def readFunctionFromFile(nameFile):
   file_path = nameFile


   with open(file_path, 'rb') as file:
       content = file.read()
   if content.startswith(b'\xef\xbb\xbf'):
       content = content[3:]
   with open(file_path, 'wb') as file:
       file.write(content)


   with open(file_path, 'r', encoding='utf-8') as file:
       file_contents = file.read()
   return file_contents




def insertValuesInDB():
   return readFunctionFromFile('sql/fill.sql')
@app.route("/avgppb")
def GetAverageProductPriceByBrand():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetAverageProductPriceByBrand ()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/bsb3/<int:brand_id>/<int:start_month>/<int:year>")
def GetBrandSalesBy3Months(brand_id, start_month, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetBrandSalesBy3Months (?,?,?)", (brand_id, start_month, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/bsb/<int:brand_id>/<int:start_month>/<int:year>")
def GetBrandSalesByMonth(brand_id, start_month, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetBrandSalesByMonth (?,?,?)", (brand_id, start_month, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/bsby/<int:brand_id>/<int:year>")
def GetBrandSalesByYear(brand_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetBrandSalesByYear(?,?)", (brand_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/sdby/")
def GetCompanyShoeDeliveries():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetCompanyShoeDeliveries()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/cb3/<int:month_id>/<int:year>")
def GetCostsBy3Months(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetCostsBy3Months(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/cbm/<int:month_id>/<int:year>")
def GetCostsByMonth(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetCostsByMonth(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/cby/<int:year>")
def GetCostsByYear( year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetCostsByYear(?)", ( year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/dl")
def GetDiscountLosses():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetDiscountLosses()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/ib3m/<int:month_id>/<int:year>")
def GetIncomeBy3Months(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetIncomeBy3Months(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/ibm/<int:month_id>/<int:year>")
def GetIncomeByMonth(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetIncomeByMonth(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/iby/<int:year>")
def GetIncomeByYear( year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetIncomeByYear(?)", ( year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/jts")
def GetJobTitleAndSalary():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetJobTitleAndSalary()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/ncs/<int:brand_id>/<int:year>")
def GetNewCustomersBySeason(brand_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetNewCustomersBySeason(?,?)", (brand_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/ncy/<int:year>")
def GetNewCustomersByYear(brand_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetNewCustomersByYear(?)", (year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/ncm/<int:brand_id>/<int:year>")
def GetNewCustomersByMonth(brand_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetNewCustomersByMonth(?,?)", (brand_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/eobm/<int:employee_id>/<int:month_id>/<int:year>")
def GetEmployeeOrdersByMonth(employee_id,month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetEmployeeOrdersByMonth(?,?,?)", (employee_id,month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/eob3m/<int:employee_id>/<int:month_id>/<int:year>")
def GetEmployeeOrdersBy3Months(employee_id,month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetEmployeeOrdersBy3Months(?,?,?)", (employee_id,month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/eob3m/<int:employee_id>/<int:year>")
def GetEmployeeOrdersByYear(employee_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetEmployeeOrdersByYear(?,?)", (employee_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




# --------------------------------------------------------------------------------------------------------------------------




@app.route("/pbrm/<int:min_price>/<int:max_price>/<int:month>/<int:year>")
def GetPairsByPriceRangeByMonth(min_price,max_price,month, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetPairsByPriceRangeByMonth(?,?,?,?)", (min_price,max_price,month, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/pbry/<int:min_price>/<int:max_price>/<int:year>")
def GetPairsByPriceRangeByYear(min_price,max_price, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetPairsByPriceRangeByYear(?,?,?)", (min_price,max_price, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/pb3m/<int:month_id>/<int:year>")
def GetProfitBy3Months(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetProfitBy3Months(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/pbm/<int:month_id>/<int:year>")
def GetProfitByMonth(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetProfitByMonth(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/pby/<int:year>")
def GetProfitByYear( year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetProfitByYear(?)", (year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/pss")
def GetPurchasedShoeSizes():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetPurchasedShoeSizes()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/spbm")
def GetSalesPercentageByMaterial():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetSalesPercentageByMaterial()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/stp")
def GetShoeTypePercentage():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypePercentage()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/stpbb")
def GetShoeTypePercentageByBrand():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypePercentageByBrand()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/stpbc")
def GetShoeTypePercentageByCompany():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypePercentageByCompany()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/stsb3m/<int:month_id>/<int:year>")
def GetShoeTypeSalesBy3Months(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypeSalesBy3Months(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result






@app.route("/stsbm/<int:month_id>/<int:year>")
def GetShoeTypeSalesByMonth(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypeSalesByMonth(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/stsbm/<int:year>")
def GetShoeTypeSalesByYear( year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetShoeTypeSalesByYear(?)", ( year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/msbs")
def GetMonthlySalesBySex():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetMonthlySalesBySex()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result










@app.route("/cbs")
def GetCustomersBySex():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetCustomersBySex()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/spp")
def GetSupplierPairsPercentage():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetSupplierPairsPercentage()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result






@app.route("/sbm/<int:month_id>/<int:year>")
def GetSuppliesByMonth(month_id, year):
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetSuppliesByMonth(?,?)", (month_id, year))
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/t5ac")
def GetTop5ActiveCustomers():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetTop5ActiveCustomers()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result


@app.route("/t5ap")
def GetTop5PopularProducts():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetTop5PopularProducts()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




@app.route("/tpis")
def GetTotalProductsInStock():
   connection, cursor = get_db_connection()
   cursor.execute("SELECT * FROM GetTotalProductsInStock()")
   rows = cursor.fetchall()
   result = "РЕЗУЛЬТАТ: \n"
   for row in rows:
       result += ', '.join(map(str, row)) + '\n'
   connection.close()
   return result




if __name__ == '__main__':
   connection, cursor = get_db_connection()

   for statement in generateDB().split(';'):
       if statement.strip():
           try:
               cursor.execute(statement)
               connection.commit()
           except Exception as e:
               print("An error occurred:", e)
               connection.rollback()
   connection.commit()





   for statement in insertValuesInDB().split(';'):
       if statement.strip():
           try:
               cursor.execute(statement)
               connection.commit()
           except Exception as e:
               print("An error occurred:", e)
               connection.rollback()
   connection.commit()
   # createAllFunctions(cursor)
   # connection.commit()
   connection.close()


   app.run(debug=True)

