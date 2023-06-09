import csv
import subprocess
import database_mysql as x
import datetime 
# connexion a la base 
conn=x.connexion('127.0.0.1','mysql','root','')
print(conn)
# PowerShell command
command = '$User="qnbts-video\\oussema";$PWord = ConvertTo-SecureString -String "Qnb1234." -AsPlainText -Force;$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PWord;Connect-ManagementServer -server  192.168.0.168 -Credential $Credential; Get-VmsCameraReport | Export-Csv -Path "dossier1/test.csv" '
x.affiche(conn)
# Execute the PowerShell command
subprocess.run(['powershell.exe', '-Command', command])

# Read the CSV file and convert it to a dictionary
data = {}
with open(r'C:\Users\admin\Desktop\pfe\projet pfe\dossier1\test.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    x=datetime.datetime.now()
    for row in reader:
        data[row['Id']] ={
            'Id': row['Id'],
            'Name': row['Name'],
            'Enabled': row['Enabled'],
            'State':row['State'],
            'ErrorNoConnection':row['ErrorNoConnection'],
            'HardwareName':row['HardwareName'],
            'HardwareId': row['HardwareId'],
            'Model': row['Model'],
            'Address':row['Address'], 
            'MAC':row['MAC'],
            'RecorderName':row['RecorderName'],
            'RecorderUri':row['RecorderUri'],
            'RecorderId':row['RecorderId'],
            'ConfiguredRecordedFPS ':row['ConfiguredRecordedFPS'],
            'PercentRecordedOneWeek':row['PercentRecordedOneWeek'],
            'UsedSpaceInGB':row['UsedSpaceInGB'],
            'date':x}
# Print the dictionary
print(data)
