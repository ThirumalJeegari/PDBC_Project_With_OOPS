import mysql.connector

db_con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Thirumal@2004",
    database = "BankingProject"
)


cursor =db_con.cursor()

print("DB Connected Successfully")

