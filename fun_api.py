import requests
import sys
import json
addr='192.168.0.168'
url="http://192.168.0.212/zabbix/api_jsonrpc.php"
def zabbix_connect(url):
    headers={
             "Content-Type": "application/json-rpc"


            }
    data1= {"jsonrpc":"2.0","method":"user.login","params":{"username":"Admin","password":"zabbix"},"id":1}
    responce=requests.post(url,headers=headers,json=data1)
    var = json.loads(responce.text)
    key=var['result']
    return(key)
def Id_detecter(key,url):
    headers={
             "Content-Type": "application/json-rpc"


            }
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
    var2 = json.loads(responce.text)
    aaa=var2['result']
    for i in aaa :
        for j in i["interfaces"] :
            if (j["ip"]==addr):
                x= i["hostid"]
                return(x) 
key=zabbix_connect(url)
Id=Id_detecter(key,url)
def add_items(key,Id,var,url):
    ch=(r'system.run[python C:\Users\oussema\Desktop\Milebix\zabbix_tests\ConfigurededRecordedFPS.py')
    ch=ch+' '+var["Id"]+"]"
    ch2=(r'system.run[python C:\Users\oussema\Desktop\Milebix\zabbix_tests\ErrorConnexion.py')
    ch2=ch2+' '+var["Id"]+"]"
    headers={
             "Content-Type": "application/json-rpc"


            }
    data2= {"jsonrpc":"2.0","method":"item.create","params":{"name":var["Name"]+'/fps',"hostid":Id,'key_':ch,"type":0,"value_type":3,"Unit":"FPS","interfaceid":"17","delay":30},"auth":key,"id":1}
    response = requests.post(url, headers=headers, json=data2)
    data3= {"jsonrpc":"2.0","method":"item.create","params":{"name":var["Name"]+'/errorconnexion ',"hostid":Id,'key_':ch2,"type":0,"value_type":4,"interfaceid":"17","delay":30},"auth":key,"id":1}
    response = requests.post(url, headers=headers, json=data3)

