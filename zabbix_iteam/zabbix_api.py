import requests
import sys
import json
filename = r"C:\Users\admin\Desktop\Milebix\zabbix_iteam"
addr= "192.168.0.225"
url="http://192.168.0.212/zabbix/api_jsonrpc.php"
headers={
         "Content-Type": "application/json-rpc"


        }
data1= {"jsonrpc":"2.0","method":"user.login","params":{"username":"Admin","password":"zabbix"},"id":1}
responce=requests.post(url,headers=headers,json=data1)
print(responce.text)
var = json.loads(responce.text)
key=var['result']
print(key)
data2={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host",
            "hostadrr"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "auth":key,
    "id": 2
}
responce=requests.post(url,headers=headers,json=data2)
print(responce.text)
var2 = json.loads(responce.text)
aaa=var2['result']
for i in aaa :
    for j in i["interfaces"] :
        if (j["ip"]==addr):
           x= i["hostid"]
           print(x)
lines=list()
with open(filename, "r") as file:
    

    for line in file :
        lines.append(line)
    for line in lines :

        x=line.split(' ')
        nom=x[0]
        print(nom)
        ch="system.run[python3 /home/zabbix/zabbix_iteam/test.py"
        ch=ch+' '+nom+"]"
       # responce=requests.post(url,headers=headers,json=data1)
       # var = json.loads(responce.text)
       # key=var['result']

        data2= {"jsonrpc":"2.0","method":"item.create","params":{"name":nom,"hostid":"10084",'key_':ch,"type":0,"value_type":4,"interfaceid":"1","delay":30},"auth":key,"id":3}
        response = requests.post(url, headers=headers, json=data2)
        print(response.text)
