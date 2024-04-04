
import pymysql
from prettytable import prettytable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="studentsdb")

cursor = conn.cursor()
query = "select * from student"

cursor.execute(query)

pltTbl = from_db_cursor(cursor)

pltTbl.align['studname'] = "l"
pltTbl.align['class'] = "r"

print(pltTbl)

conn.close()
