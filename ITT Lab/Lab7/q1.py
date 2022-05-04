import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
#conn.execute("CREATE TABLE STUDENT (ID INT PRIMARY KEY NOT NULL, NAME STRING, MARKS INT);")
# conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(1,'Sam',10)")
# conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(2,'Tom',20)")
# conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(3,'Ram',50)")
# conn.commit()
cursor = conn.execute("SELECT ID, NAME, MARKS FROM STUDENT")
for row in cursor:
    print(f"ID-{row[0]}\n Name-{row[1]}\n Marks-{row[2]}")