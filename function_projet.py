#test_line="83.149.9.216 - - [17/May/2015:10:05:03 +0000] 'GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1' 200 203023 'http://semicomplete.com/presentations/logstash-monitorama-2013/' 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'"

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, size, href, os

    
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
        
    list1=dict(
    time=line[3]+' '+line[4],
    remote_ip=line[0],
    request=get[1],
    path=line[6],
    response=line[8],
    size=line[9],
    referrer=get[3],
    user_agent=usr_agent,
    system_agent=lireOS(usr_agent)
    )

    return list1

def cleaner(list1):
    list1[0]=list1[1:]
    list1[2]=list1[3].split('/')
    #list1[6]=

#print(splitter(test_line))

#lireLog : fonction pour parser un document entier en utilisant splitter   
def lireLog (nomFic) :
    f=open(nomFic,"r")
    list2=[]
    for l in f:
        list2.append(splitter(l))
    return list2
    
def convertJSON(nomFic) :
    import json
    f=open(nomFic,"r")
    list2=[]
    nomFic2=nomFic[:-4]+".json"
    for l in f:
        list2.append(splitter(l))
    f2=open(nomFic2,"a")
    json.dump(list2,f2,indent = 4)
        
        
    
    


    