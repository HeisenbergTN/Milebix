import csv
import subprocess
import mysql.connector
import datetime 

cnx = mysql.connector.connect(
    host='127.0.0.1',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='milebix'  # Replace with the name of your MySQL database
)
print(cnx)
# PowerShell command
command = '$User="qnbts-video\\oussema";$PWord = ConvertTo-SecureString -String "Qnb1234." -AsPlainText -Force;$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PWord;Connect-ManagementServer -server  192.168.0.168 -Credential $Credential; Get-VmsCameraReport | Export-Csv -Path "test.csv" '
#x.affiche(conn)
# Execute the PowerShell command
#subprocess.run(['powershell.exe', '-Command', command])
cursor=cnx.cursor()
cursor.execute('show tables')
# Read the CSV file and convert it to a dictionary
data = {}
sql="insert into zabbix_iteam (Id,Name,Enabled,State,ErrorNoConnection,HardwareName,Model,Address,MAC,RecorderName,RecorderUri,RecorderId,ConfiguredRecordedFPS,PercentRecordedOneWeek,UsedSpaceInGB,Date)"+"VALUES (%s,%s,%b,%b,%b,%s,%s,%s,%s,%s,%s,%s,%i,%f,%f,%s)"
data2={"kkkk","kkekek",True,False,True,"jjjjj","llll","kekeke","kekekek","ekekmerkke","elellkke","ekelkjr","kzjrjkj",1,1.1,1.2,"20:20:2022"}
#with open('test.csv', 'r') as csvfile:
#    reader = csv.DictReader(csvfile)
#    x=datetime.datetime.now()
#    for row in reader:
#        data={row['Id'],row['Name'],row['Enabled'],row['State'],row['ErrorNoConnection'],row['HardwareName'],row['HardwareId'],row['Model'],row['Address'],row['MAC'],row['RecorderName'],row['RecorderUri'],row['RecorderId'],row['ConfiguredRecordedFPS'],row['PercentRecordedOneWeek'],row['UsedSpaceInGB'],x}
#        cursor.execute(sql,data)
#        print(data)
cursor.execute(sql,data2)
