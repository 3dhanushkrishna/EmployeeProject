import sqlite3
connection = sqlite3.connect("company.db")
result = connection.execute("SELECT * FROM EMPLOYEE")
for i in result:
    print("EMPLOYEECODE: ", i[0])
    print("EMPLOYEENAME: ", i[1])
    print("DESIGNATION: ",i[2])
    print("SALARY: ", i[3])
    print("COMPANYNAME: ", i[4])
    print("MOBILENO: ", i[5])