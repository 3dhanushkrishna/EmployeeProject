import sqlite3
connection = sqlite3.connect("company.db")
connection.execute('''CREATE TABLE EMPLOYEE(
                      EMPLOYEECODE INTEGER PRIMARY KEY AUTOINCREMENT,
                      EMPLOYEENAME TEXT,
                      DESIGNATION TEXT,
                      SALARY INTEGER,
                      COMPANYNAME TEXT,
                      MOBILENO INTEGER
);''')

print("table created successfully")
getEmployeeName = input("Enter the name: ")
getDesignation = input("Enter the designation: ")
getSalary = input("Enter the salary: ")
getCompanyName = input("Enter the companyname: ")
getMobileNo = input("Enter the mobileno: ")
connection.execute("INSERT INTO EMPLOYEE(EMPLOYEENAME,DESIGNATION,SALARY,COMPANYNAME,MOBILENO)\
                   VALUES('"+getEmployeeName+"','"+getDesignation+"',"+getSalary+",'"+getCompanyName+"',"+getMobileNo+")")
connection.commit()
connection.close()
print("inserted successfully")