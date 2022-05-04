import sqlite3
from sre_constants import BRANCH
conn = sqlite3.connect("test.db")
# print("Database connected successfully")

# conn.execute("CREATE TABLE STUDENT(ID INT PRIMARY KEY, NAME TEXT, SEMESTER TEXT, BRANCH TEXT);")
# print("Table Created")

while(True):
    n = int(input("Enter\n1. Data Entry\n2.Data Display\n3.Data Delete\n4.Exit\n"))
    if n==1:
        print("n->{n}")
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        semester = input("Enter Semester: ")
        branch = input('Enter Branch: ')
        exec = "INSERT INTO STUDENT VALUES("+id+", '"+name+"', '" +semester+"', '"+branch+"');"
        print(exec)
        conn.execute(exec)
        conn.commit()
    elif n==2:
        print("n->2")
        cur = conn.execute("SELECT * FROM STUDENT")
        print("Done")
        for row in cur:
            print(row)
            print(f"{row[0]} {row[1]}  {row[2]}  {row[3]}\n")
    else:
        break
