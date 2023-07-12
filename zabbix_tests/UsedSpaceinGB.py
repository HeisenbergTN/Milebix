import mysql.connector
import sys 
cnx = mysql.connector.connect(
    host='127.0.0.1',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='Milebix'  # Replace with the name of your MySQL database
)
def convertir (ch):
    ch2=''
    for i in ch:
        if (i == ","):
            ch2=ch2+"."
        else :
            ch2=ch2+i
    ch2=float(ch2)
    return (ch2)
sql2="select UsedSpaceInGB from zabbix_iteam where Id='"+ sys.argv[1]+"'"
cursor= cnx.cursor()
cursor.execute(sql2)
rows=cursor.fetchall()
for row in rows :
    x=convertir(row[0])
    print(x)
cursor.close()
cnx.close()