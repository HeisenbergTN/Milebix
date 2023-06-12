import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='127.0.0.1',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='milebix'  # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a SELECT query
query= "CREATE TABLE  test (Id varchar(20),Name varchar(20),PRIMARY KEY (ID))"
cursor.execute(query)
cursor.execute("show table ;")
query1="insert into test (Id,Name) Values(%s,%s)"
sql=("01233456","oussema")
cursor.execute(query1,sql)
#creation dela table
cnx.commit()
cursor.close()
cnx.close()
