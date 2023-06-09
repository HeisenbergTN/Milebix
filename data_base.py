import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='localhost',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='',  # Replace with your MySQL password
    database='MileBix'  # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a SELECT query
query = "SELECT * FROM table1"
cursor.execute(query)

# Fetch all rows returned by the query
rows = cursor.fetchall()

# Process the rows
for row in rows:
    # Access individual columns using row[column_index]
    
    column1_value = row[0]
    column2_value = row[1]
    print(str(column1_value)+" | "+str(column2_value))
    # ...

# Close the cursor and the connection
cursor.close()
cnx.close()