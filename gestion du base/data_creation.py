import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='127.0.0.1',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database=''  # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a SELECT query
query="CREATE database IF NOT EXISTS Milebix"
cursor.execute(query)
#creation dela base
cursor.close()
cnx.close()
