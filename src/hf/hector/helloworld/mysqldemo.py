__author__ = 'xudazhou'

import MySQLdb

conn = MySQLdb.connect("localhost", "root", "123456", "test", 3306)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)

cursor.close()
conn.close()
