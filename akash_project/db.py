import mysql.connector  
def get_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root",
        password="",      # change if needed
        database="student_db"
    )
#pip install mysql-connector-python