import sqlite3
connection = sqlite3.connect("company.db")
getEmployeecode = input("Enter the Employeecode to be updated: ")
getEmployeename = input("Enter the new name: ")
getDesignation = input("Enter the new Designation: ")
getSalary = input("Enter the new salary: ")
getCompanyname = input("Enter the new Companyname: ")
getMobileno = input("Enter the new Mobileno: ")
connection.execute("UPDATE EMPLOYEE SET EMPLOYEENAME='"+getEmployeename+"',\
DESIGNATION='"+getDesignation+"',SALARY="+getSalary+",COMPANYNAME='"+getCompanyname+"',MOBILENO="+getMobileno+"\
 WHERE EMPLOYEECODE="+getEmployeecode)
connection.commit()
print("updated Successfully")
result = connection.execute("SELECT * FROM EMPLOYEE")
for i in result:
    print("EMPLOYEECODE: ", i[0])
    print("EMPLOYEENAME: ", i[1])
    print("DESIGNATION: ",i[2])
    print("SALARY: ", i[3])
    print("COMPANYNAME: ", i[4])
    print("MOBILENO: ", i[5])
