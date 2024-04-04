
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="studentsdb")

cursor = conn.cursor()

query = "update student set studname = 'Micheal Jordan' where studid='ST001'"

cursor.execute(query)
conn.commit()

conn.close()
