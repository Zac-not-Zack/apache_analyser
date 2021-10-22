import json

#count ip adress

def statIP(nomFicJSON) :
    ipAddr=[]
    cntr=[]
    i=0
    j=0 
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    for data in dict1:
        if data['remote_ip'] not in ipAddr:
            ipAddr.append(data['remote_ip'])
            cntr[i]=j+1
            i=i+1
        else:
            
    
    return statIP

#count browser
def statBrowser(line) :
    return statBrowser