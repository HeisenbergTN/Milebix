import pyodbc
server = '127.0.0.1'
database='MileBix'
username='admin'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username)
print(cnxn)                      
