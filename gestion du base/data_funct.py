import csv
import subprocess
from typing import Self
import mysql.connector
import datetime 
class srv_hard :
    def __init__(Id,Name,Enabled,State,ErrorNoConnection,HardwareName,HardwareId,Model,Address,MAC,RecorderName,RecorderUri,RecorderId,ConfiguredRecordedFPS,PercentRecordedOneWeek,UsedSpaceInGB,Date):
        Self.Id=Id
        Self.Name=Name
        Self.Enabled=Enabled
        Self.State=State
        Self.ErrorNoConnection=ErrorNoConnection
        Self.HardwareName=HardwareName
        Self.HardwareId=HardwareId
        Self.Model=Model
        Self.Address=Address
        Self.MAC=MAC
        Self.RecorderName=RecorderName
        Self.RecorderUri=RecorderUri
        Self.RecorderId=RecorderId
        Self.ConfiguredRecordedFPS=ConfiguredRecordedFPS
        Self.PercentRecordedOneWeek=PercentRecordedOneWeek
        Self.UsedSpaceInGB=UsedSpaceInGB
        Self.Date=Date
        
def connexion(host ='192.168.0.168' ,user='root', password='Qnb1234.' ,database= 'milebix') :
     host=host
     user=user
     password=password
     database=database
     cnx = mysql.connector.connect(host,user,password,database)
     return (cnx)
def ajout(conn):
    cursor=conn.cursor()
    sql="insert into zabbix_iteam (Id,Name,Enabled,State,ErrorNoConnection,HardwareName,HardwareId,Model,Address,MAC,RecorderName,RecorderUri,RecorderId,ConfiguredRecordedFPS,PercentRecordedOneWeek,UsedSpaceInGB,Date) VALUES ({Id},{Name},{Enabled},{State},{ErrorNoConnection},{HardwareName},{HardwareId},{Model},{Address},{MAC},{RecorderName},{RecorderUri},{RecorderId},{ConfiguredRecordedFPS},{PercentRecordedOneWeek},{UsedSpaceInGB},{Date})"
def Identité_hard():
    #creation d'une liste vide
    L=list()
    conn=connexion('192.168.0.168','root','Qnb1234.','milebix')
    sql='SELECT Id FROM milebix.zabbix_iteam'
    cursor=conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows :
        L.append(row)
    cursor.close()
    conn.close()
    return L
connexion('192.168.0.168','root','Qnb1234.','Milebix')  
#L=Identité_hard()
#print(L)


 
    
#with open('test.csv', 'r') as csvfile:
#    reader = csv.DictReader(csvfile)
#    x=datetime.datetime.now()
#    for row in reader:
#        data={row['Id'],row['Name'],row['Enabled'],row['State'],row['ErrorNoConnection'],row['HardwareName'],row['HardwareId'],row['Model'],row['Address'],row['MAC'],row['RecorderName'],row['RecorderUri'],row['RecorderId'],row['ConfiguredRecordedFPS'],row['PercentRecordedOneWeek'],row['UsedSpaceInGB'],x}
#        cursor.execute(sql,data)
#        print(data)

#cursor.execute(sql)
#cnx.commit()
