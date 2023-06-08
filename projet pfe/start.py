import subprocess
import json
# Se connecter au serveur de gestion avec des informations d'identification spécifiées
connect_command =  '$User="qnbts-video\oussema";$PWord = ConvertTo-SecureString -String "Qnb1234." -AsPlainText -Force;$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PWord;Connect-ManagementServer -server  192.168.0.168 -Credential $Credential;Get-VmsCameraReport |ConvertTo-Json'
connect_result = subprocess.run(["powershell","-c", connect_command],capture_output=True, text=True)
if(connect_result.stderr):
    #print(connect_result.stdout)
    print(connect_result.stdout)
else:
    print("connecté")
    print(connect_result.stdout)
    result=json(connect_result)
var2 = json.loads(result)
