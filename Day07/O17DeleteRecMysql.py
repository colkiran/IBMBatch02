
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="studentsdb")

cursor = conn.cursor()

query = "delete from student where studid = 'ST025'"

cursor.execute(query)

conn.commit()

conn.close()
