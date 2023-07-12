import csv
import subprocess
import mysql.connector
import datetime 

def item_id(cnx) :
    L=list()
    sql="select Id from zabbix_iteam"
    cursor=cnx.cursor()
    cursor.execute(sql)
    rows =cursor.fetchall()
    for row in rows :
        L.append(row[0])
    cursor.close()
    cnx.close()
    return(L)
cnx=mysql.connector.connect('127.0.0.1','root','Qnb1234.','milebix')
ch=item_id(cnx)
print(ch)
#def milestone_test() :
#    L=item_id()
#   cnx=conexion()
#    print(cnx)
# PowerShell 
 #   command = '$User="qnbts-video\\oussema";$PWord = ConvertTo-SecureString -String "Qnb1234." -AsPlainText -Force;$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PWord;Connect-ManagementServer -server  127.0.0.1 -Credential $Credential; Get-VmsCameraReport | Export-Csv -Path "test.csv" -NoTypeInformation'
  #  subprocess.run(['powershell.exe', '-Command', command])
   # data = {}
    #x=datetime.datetime.now()
    #datetime_string=x.strftime("%Y%m%d%H%M%S")
    #print (datetime_string)
    #with open('test.csv', 'r') as csvfile:
        #reader = csv.DictReader(csvfile)
        #x=datetime.datetime.now()
        #for row in reader:
            #data={"Id":row['Id'],"Name":row['Name'],"Enabled":row['Enabled'],"State":row['State'],"ErrorNoConnection":row['ErrorNoConnection'],"HardwareName":row['HardwareName'],"HardwareId":row['HardwareId'],"Model":row['Model'],"Address":row['Address'],"MAC":row['MAC'],"RecorderName":row['RecorderName'],"RecorderUri":row['RecorderUri'],"RecorderId":row['RecorderId'],"ConfiguredRecordedFPS":row['ConfiguredRecordedFPS'],"PercentRecordedOneWeek":row['PercentRecordedOneWeek'],"UsedSpaceInGB":row['UsedSpaceInGB'],"Date":x}
            #if (data[0] in L) :
                #sql = "update zabbix_iteam SET Name ='"+ data['Id']+"',Enabled ='"+ data["Name"]+"',State ='"+ data["State"] + "',ErrorNoConnection ='"+ data["ErrorNoConnection"]+"',HardwareName="+data["HardwareName"]+"',HardwareId='"+data["HardwareId"]+"',Model='"+data["Model"]+"',Address='"+data["Address"]+"',MAC='"+data["MAC"]+"',RecorderName='"+data["RecorderName"]+"',RecorderUri='"+data["RecorderUri"]+"',RecorderId='"+data["RecorderId"]+"',ConfiguredRecordedFPS='"+data["ConfiguredRecordedFPS"]+"',UsedSpaceInGB='"+data["UsedSpaceInGB"]+"',Date='"+data["Date"]+"'" + "where Id ='"+data["Id"]+"'"
                #conn=connexion()
                #cursor=conn.cursor()
                #cursor.execute(sql)
            #else :
                #sql="insert into zabbix_iteam (Id,Name,Enabled,State,ErrorNoConnection,HardwareName,HardwareId,Model,Address,MAC,RecorderName,RecorderUri,RecorderId,ConfiguredRecordedFPS,PercentRecordedOneWeek,UsedSpaceInGB,Date) Values('"+ data['Id']+"','"+ data["Name"]+"','"+ data["State"] + "','"+ data["ErrorNoConnection"]+"','"+data["HardwareName"]+"','"+data["HardwareId"]+"','"+data["Model"]+"','"+data["Address"]+"','"+data["MAC"]+"','"+data["RecorderName"]+"','"+data["RecorderUri"]+"','"+data["RecorderId"]+"','"+data["ConfiguredRecordedFPS"]+"','"+data["UsedSpaceInGB"]+"','"+data["Date"]+"')"
                #conn=connexion()
                #cursor=conn.cursor()
                #cursor.execute(sql)
#milestone_test()