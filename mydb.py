import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost", user="bufu1", passwd="bufu1myproject"
)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE srm_database")

print("All Done!")
