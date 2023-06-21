import csv
import subprocess
import mysql.connector
import datetime 

cnx = mysql.connector.connect(
    host='localhost',  # Replace with the actual hostname
    user='root',  # Replace with your MySQL username
    password='Qnb1234.',  # Replace with your MySQL password
    database='milebix'  # Replace with the name of your MySQL database
)
print(cnx)
# PowerShell command
command = '$User="qnbts-video\\oussema";$PWord = ConvertTo-SecureString -String "Qnb1234." -AsPlainText -Force;$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PWord;Connect-ManagementServer -server  127.0.0.1 -Credential $Credential; Get-VmsCameraReport | Export-Csv -Path "test.csv" -NoTypeInformation'
#x.affiche(conn)
# Execute the PowerShell command
subprocess.run(['powershell.exe', '-Command', command])
cursor=cnx.cursor()
#cursor.execute('show tables')
# Read the CSV file and convert it to a dictionary
data = dict()
x=datetime.datetime.now()
datetime_string=x.strftime("%Y%m%d%H%M%S")
print (datetime_string)
with open('test.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    x=datetime.datetime.now()
    for row in reader:
        data={"Id":row['Id'],"Name":row['Name'],"Enabled":row['Enabled'],"State":row['State'],"ErrorNoConnection":row['ErrorNoConnection'],"HardwareName":row['HardwareName'],"HardwareId":row['HardwareId'],"Model":row['Model'],"Address":row['Address'],"MAC":row['MAC'],"RecorderName":row['RecorderName'],"RecorderUri":row['RecorderUri'],"RecorderId":row['RecorderId'],"ConfiguredRecordedFPS":row['ConfiguredRecordedFPS'],"PercentRecordedOneWeek":row['PercentRecordedOneWeek'],"UsedSpaceInGB":row['UsedSpaceInGB'],"Date":x}
        print(data)
