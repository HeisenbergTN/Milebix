import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='192.168.0.168',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='Milebix'  # Replace with the name of your MySQL database
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute a SELECT query
query= "CREATE TABLE  zabbix_iteam (Id varchar(20),Name varchar(20),Enabled  BOOL ,State    BOOL,ErrorNoConnection  BOOL,HardwareName varchar(25),HardwareId   varchar(25), Model varchar(25),Address varchar(25), MAC varchar(15),RecorderName varchar(25),RecorderUri  varchar(25),RecorderId   varchar(25),ConfiguredRecordedFPS int,PercentRecordedOneWeek  float,UsedSpaceInGB float,Date date , PRIMARY KEY (ID))"
cursor.execute(query)
#creation dela table
cursor.close()
cnx.close()
