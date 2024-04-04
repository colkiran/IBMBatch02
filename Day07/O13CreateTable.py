
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="studentsdb")
cursor = conn.cursor()

query = """
create table student (
studid varchar(5) PRIMARY KEY,
studname varchar(50) not null,
class varchar(25) not null, 
age int not null)
"""

cursor.execute(query)
conn.close()
