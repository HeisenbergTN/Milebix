import requests
import sys
import json
def get_url():
    url=str(input("donner l'adress du serveur"))
    url='http://'+url+'/zabbix/api_jsonrpc.php'
    return(url)
def get_address():
    addr=str(input("donner l'adress du host"))
    return(addr)
addr="192.168.0.168"
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
def interface_detecter(key,url):
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
                y= j["interfaceid"]
                return(y) 
def get_name(key,url):
    headers={
             "Content-Type": "application/json-rpc"


            }
    data2={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
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
                x= i["host"]
                return(x) 
key=zabbix_connect(url)
name=get_name(key,url)
Id=Id_detecter(key,url)
it=interface_detecter(key,url)
def add_items(key,Id,var,url,name):
    
    ch=(r'system.run[python C:\Users\oussema\Desktop\Milebix\zabbix_tests\ConfigurededRecordedFPS.py')
    ch5=(r'system.run[python C:\Users\oussema\Desktop\Milebix\zabbix_tests\UsedSpaceinGB.py')
    ch5=ch5+' '+var["Id"]+"]"
    ch=ch+' '+var["Id"]+"]"
    ch2=(r'system.run[python C:\Users\oussema\Desktop\Milebix\zabbix_tests\ErrorConnexion.py')
    ch2=ch2+' '+var["Id"]+"]"

    headers={
             "Content-Type": "application/json-rpc"


            }
    data2= {"jsonrpc":"2.0","method":"item.create","params":{"name":var["Name"]+':fps',"hostid":Id,'key_':ch,"type":0,"value_type":3,"Units":"FPS","interfaceid":it,"delay":30},"auth":key,"id":1}
    response = requests.post(url, headers=headers, json=data2)
    data5= {"jsonrpc":"2.0","method":"item.create","params":{"name":var["Name"]+':space in GB',"hostid":Id,'key_':ch5,"type":0,"value_type":0,"Units":"GB","interfaceid":it,"delay":30},"auth":key,"id":1} 
    response = requests.post(url, headers=headers, json=data5)
    ch3="last(/"+name+"/"+ch+")<12"
    ch4='last(/'+name+'/'+ch2+')<>"False"'
    ch6="last(/"+name+"/"+ch5+")<20"
    dexc1= var["Name"]+":"+"nombre de FPS bas " 
    dexc2= var["Name"]+":"+"pourcentage en GB supperieur a 20 % " 
    data6={
         "jsonrpc": "2.0",
         "method": "trigger.create",
         "params": {
         "description": dexc2,
         "expression": ch6,  
         "priority": 3,
         "status": 0,
         "type": 0,
         "status": 0
                   },
         "auth":key,
         "id": 1
          }
    data={
         "jsonrpc": "2.0",
         "method": "trigger.create",
         "params": {
         "description": dexc1,
         "expression": ch3,  
         "priority": 3,
         "status": 0,
         "type": 0,
         "status": 0
                   },
         "auth":key,
         "id": 1
          }
    data4={"jsonrpc": "2.0",
         "method": "trigger.create",
         "params": {
         "description": "Error connexion",
         "expression": ch4,  
         "priority": 3,
         "status": 0,
         "type": 0,
         "status": 0
                   },
         "auth":key,
         "id": 1}
          

    response = requests.post(url, headers=headers, json=data)
    data3= {"jsonrpc":"2.0","method":"item.create","params":{"name":var["Name"]+':errorconnexion ',"hostid":Id,'key_':ch2,"type":0,"value_type":4,"interfaceid":it,"delay":30},"auth":key,"id":1}
    response = requests.post(url, headers=headers, json=data3)
    response = requests.post(url, headers=headers, json=data4)
    response = requests.post(url, headers=headers, json=data6)
    
