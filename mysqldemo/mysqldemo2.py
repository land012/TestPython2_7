__author__ = 'xudazhou'

import MySQLdb

conn = MySQLdb.connect("localhost", "root", "123456", "test", 3306)

cursor1 = conn.cursor()
cursor1.execute("select * from student where id<3")
students = cursor1.fetchall()

print("cursor1.arraysize=%d" % cursor1.arraysize)
print("cursor1.rowcount=%d" % cursor1.rowcount)

cursor2 = conn.cursor()

for s in students:
    cursor2.execute("select id, name, teacher_id from course where teacher_id=" + str(s[0]))
    courses = cursor2.fetchall()
    for c in courses:
        print("c is " + str(c))

cursor1.close()
cursor2.close()
conn.close()
