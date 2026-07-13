# pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

# -------------------------------
# Database Connection
# -------------------------------

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # Change your MySQL password
        database="company"
    )

    if conn.is_connected():
        print("Connected Successfully!")

except Error as e:
    print("Database Error:", e)
    exit()

cursor = conn.cursor()


# -------------------------------
# Create Employee
# -------------------------------

def add_employee():

    print("\nAdd Employee")

    name = input("Name : ")
    email = input("Email : ")
    mobile = input("Mobile : ")
    department = input("Department : ")
    salary = float(input("Salary : "))
    city = input("City : ")

    sql = """
    INSERT INTO employees
    (name,email,mobile,department,salary,city)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    values = (name,email,mobile,department,salary,city)

    cursor.execute(sql, values)
    conn.commit()

    print("Employee Added Successfully")


# -------------------------------
# View Employees
# -------------------------------

def view_employee():

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    print("\n---------------- Employee List ----------------")

    if len(rows)==0:
        print("No Records Found")
        return

    print("{:<5}{:<20}{:<25}{:<15}{:<15}{:<12}{:<15}".format(
        "ID","Name","Email","Mobile","Department","Salary","City"))

    print("-"*110)

    for row in rows:
        print("{:<5}{:<20}{:<25}{:<15}{:<15}{:<12}{:<15}".format(
            row[0],row[1],row[2],row[3],row[4],row[5],row[6]))


# -------------------------------
# Search Employee
# -------------------------------

def search_employee():

    emp_id = input("Enter Employee ID : ")

    sql = "SELECT * FROM employees WHERE id=%s"

    cursor.execute(sql,(emp_id,))

    row = cursor.fetchone()

    if row:

        print("\nEmployee Details")
        print("----------------")
        print("ID         :",row[0])
        print("Name       :",row[1])
        print("Email      :",row[2])
        print("Mobile     :",row[3])
        print("Department :",row[4])
        print("Salary     :",row[5])
        print("City       :",row[6])

    else:
        print("Employee Not Found")


# -------------------------------
# Update Employee
# -------------------------------

def update_employee():

    emp_id = input("Enter Employee ID : ")

    cursor.execute("SELECT * FROM employees WHERE id=%s",(emp_id,))
    row = cursor.fetchone()

    if row is None:
        print("Employee Not Found")
        return

    print("\nLeave Blank to Keep Old Value\n")

    name = input(f"Name ({row[1]}) : ")
    email = input(f"Email ({row[2]}) : ")
    mobile = input(f"Mobile ({row[3]}) : ")
    department = input(f"Department ({row[4]}) : ")
    salary = input(f"Salary ({row[5]}) : ")
    city = input(f"City ({row[6]}) : ")

    if name=="": name=row[1]
    if email=="": email=row[2]
    if mobile=="": mobile=row[3]
    if department=="": department=row[4]
    if salary=="": salary=row[5]
    if city=="": city=row[6]

    sql = """
    UPDATE employees
    SET
    name=%s,
    email=%s,
    mobile=%s,
    department=%s,
    salary=%s,
    city=%s
    WHERE id=%s
    """

    values = (
        name,
        email,
        mobile,
        department,
        salary,
        city,
        emp_id
    )

    cursor.execute(sql, values)
    conn.commit()

    print("Employee Updated Successfully")


# -------------------------------
# Delete Employee
# -------------------------------

def delete_employee():

    emp_id = input("Enter Employee ID : ")

    cursor.execute("SELECT * FROM employees WHERE id=%s",(emp_id,))
    row = cursor.fetchone()

    if row is None:
        print("Employee Not Found")
        return

    ch = input("Are you sure (y/n)? ")

    if ch.lower()=="y":

        cursor.execute(
            "DELETE FROM employees WHERE id=%s",
            (emp_id,)
        )

        conn.commit()

        print("Employee Deleted Successfully")


# -------------------------------
# Count Employees
# -------------------------------

def total_employee():

    cursor.execute("SELECT COUNT(*) FROM employees")

    total = cursor.fetchone()[0]

    print("\nTotal Employees :", total)


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n")
    print("="*45)
    print(" EMPLOYEE MANAGEMENT SYSTEM ")
    print("="*45)

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Total Employees")
    print("7. Exit")

    choice = input("\nEnter Choice : ")

    if choice=="1":
        add_employee()

    elif choice=="2":
        view_employee()

    elif choice=="3":
        search_employee()

    elif choice=="4":
        update_employee()

    elif choice=="5":
        delete_employee()

    elif choice=="6":
        total_employee()

    elif choice=="7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

cursor.close()
conn.close()