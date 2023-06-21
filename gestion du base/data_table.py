import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='127.0.0.1',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='Milebix'  # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a SELECT query
query= "CREATE TABLE  zabbix_iteam (Id varchar(100),Name varchar(30),Enabled  varchar(50),State    varchar(50),ErrorNoConnection varchar(50),HardwareName varchar(50),HardwareId   varchar(100), Model varchar(50),Address varchar(50), MAC varchar(15),RecorderName varchar(50),RecorderUri  varchar(50),RecorderId   varchar(100),ConfiguredRecordedFPS int,PercentRecordedOneWeek  varchar(50),UsedSpaceInGB varchar(10),Date datetime , PRIMARY KEY (ID))"
cursor.execute(query)
#creation dela table
cursor.close()
cnx.close()
