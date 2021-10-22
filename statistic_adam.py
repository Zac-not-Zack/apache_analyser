import json

#count ip adress

def statIP(nomFicJSON) :
    statIP={}
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    for data in dict1:
        if data['remote_ip'] not in statIP:
            statIP[data['remote_ip']]=1
            
        else:
            statIP[data['remote_ip']]=statIP[data['remote_ip']]+1
    
    return statIP

#count browser
def statBrowser(line) :
    statBrowser={}
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    for data in dict1:
        if data['browser'] not in statBrowser:
            statIP[data['browser']]=1
            
        else:
            statIP[data['browser']]=statIP[data['browser']]+1   
    return statBrowser