import mysql.connector


conn = mysql.connector.connect(
         user='root',
         password='2672',
         host='localhost',
         database='test')

cur = conn.cursor()

query = ("SELECT * FROM takelook")


