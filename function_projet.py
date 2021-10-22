#test_line="83.149.9.216 - - [17/May/2015:10:05:03 +0000] 'GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1' 200 203023 'http://semicomplete.com/presentations/logstash-monitorama-2013/' 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'"

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, size, href, os
import json
from statistics import mean
from statistics import mode
from statistics import multimode
from datetime import date
    
def splitter(linetoparse):
    line=linetoparse.split(' ')
    get=linetoparse.split('"')
    usr_agent=get[5]
    
    #lireOS : pour identifier et afficher la version d'OS de la machine
    def lireOS(usr_agent) :
        if "Windows" in usr_agent :
            sys_agent="Windows"
        
        elif "Linux" in usr_agent :
            if "Android" in usr_agent :
                sys_agent="Android"
            else :
                sys_agent="Linux"
            
        elif "Mac" in usr_agent :
            if "iPhone" in usr_agent :
                sys_agent="iPhone OS"
            else :
                sys_agent="Mac OS"
        else:
            sys_agent="OS unknown"
        return sys_agent

    def lireBrowser(usr_agent) :
        if "Chrome" in usr_agent:
            browser="Google Chrome"
        elif "Safari" in usr_agent:
            browser="Safari"
        elif "MSIE" in usr_agent:
            browser="MS Internet Explorer/Edge"
        elif "Firefox" in usr_agent:
            browser="Mozilla Firefox"
        else:
            browser="Web browser unknown or bot"
        return browser
            

    list1=dict(
    time=line[3]+' '+line[4],
    remote_ip=line[0],
    request=get[1],
    path=line[6],
    response=line[8],
    size=line[9],
    referrer=get[3],
    user_agent=usr_agent,
    system_agent=lireOS(usr_agent),
    browser=lireBrowser(usr_agent)
    )
    return list1





#lireLog : fonction pour parser un document entier en utilisant splitter   
def lireLog (nomFic) :
    f=open(nomFic,"r")
    list2=[]
    for l in f:
        list2.append(splitter(l))
    return list2
    
def convertJSON(nomFic) :
    list2=[]
    with open(nomFic,"r") as f :
        nomFic2=nomFic[:-4]+".json"
        for l in f:
            list2.append(splitter(l))
    with open(nomFic2,"w") as f2 :
        json.dump(list2,f2,indent = 4)
    return list2
        
        
def OSAnalyser(nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    compteurOS=[0,0,0,0,0,0]
    for data in dict1 :
        #print(data['system_agent'])
        if data['system_agent'] == 'Windows' :
            compteurOS[0]=compteurOS[0]+1
        elif data['system_agent'] == 'Linux' :
            compteurOS[1]=compteurOS[1]+1
        elif data['system_agent'] == 'Android' :
            compteurOS[2]=compteurOS[2]+1
        elif data['system_agent'] == 'iPhone OS' :
            compteurOS[3]=compteurOS[3]+1
        elif data['system_agent'] == 'Mac OS' :
            compteurOS[4]=compteurOS[4]+1
        elif data['system_agent'] == 'OS unknown' :
            compteurOS[5]=compteurOS[5]+1
            
    return compteurOS
    
def AvgSize (nomFicJSON) :  
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    l_size=[]
    for data in dict1 :
        if data['size'] != '-' :
            size_float=float(data['size'])
            l_size.append(size_float)
    avgsize=mean(l_size)   
    return avgsize
    
def TraficduJour (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    today=date.today()
    d=today.strftime("%d/%B/%Y")
    nbVisiteur=0
    for data in dict1 :
        date1=data['time'].split(':')
        if date1[0]==d :
            nbVisiteur=nbVisiteur+1
    return nbVisiteur
    
#HEAD,GET,POST,PUT,OTHERS
#find peak hours, types of files?if same website?response
def AnalyseMethode (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    compteurMethode=[0,0,0,0,0]
    for data in dict1 :
        if "GET" in data['request'] :
            compteurMethode[0]=compteurMethode[0]+1
        elif "POST" in data['request'] :
            compteurMethode[1]=compteurMethode[1]+1
        elif "HEAD" in data['request'] :
            compteurMethode[2]=compteurMethode[2]+1
        elif "PUT" in data['request'] :
            compteurMethode[3]=compteurMethode[3]+1
        else :
            compteurMethode[4]=compteurMethode[4]+1
            
    return compteurMethode
  
def HeureCreuse (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
   
    l_heure=[]
    for data in dict1 :
        heure=data['time'].split(':')
        l_heure.append(heure[1])
    heureCreuse=mode(l_heure)
    #heureCreuse2=multimode(l_heure)
    return heureCreuse #,heureCreuse2
    
