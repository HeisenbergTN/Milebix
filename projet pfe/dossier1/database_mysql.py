import mysql.connector
def connexion(host='127.0.0.1',database='projet_test',username='root',password=''):
    conn = mysql.connector.connect(host=host, database=database, user=username,password=password)
    return (conn)
def affiche(conn) :
    cursor=conn.cursor()
    x=cursor.execute("SHOW TABLES")
    print(x)
