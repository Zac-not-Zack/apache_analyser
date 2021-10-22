#test_line="83.149.9.216 - - [17/May/2015:10:05:03 +0000] 'GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1' 200 203023 'http://semicomplete.com/presentations/logstash-monitorama-2013/' 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'"

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, size, href, os
import json
import re
import argparse
from statistics import mean
from statistics import mode
from statistics import multimode
from collections import Counter
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
    print('La taille moyenne de fichier demandé ' + str(avgsize))
    return avgsize #Single-value
    
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
    return nbVisiteur #Single-value
    
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
    t=Counter(l_heure) 
    #print(t['01'])
    heureCreuse=mode(l_heure)
    #heureCreuse2=multimode(l_heure)
    return heureCreuse, t #Single-value
    
def AnalyseResponse (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
   
    l_rep=[]
    for data in dict1 :
        l_rep.append(data['response'])
    reponse=Counter(l_rep)
    return reponse
    
def AnalyseIPAdd (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    l_ipaddress=[]
    for data in dict1 :
        l_ipaddress.append(data['remote_ip'])
    ipAddress1=Counter(l_ipaddress).most_common(10) #Les 10 clients le plus fréquentés
    ipAddress2=Counter(l_ipaddress)
    totalSession=len(l_ipaddress)
    visiteurUnique=0
    for ipAdd in ipAddress2 : #pour calculer visiteur unique
        if ipAddress2[ipAdd] == 1 :
            visiteurUnique=visiteurUnique+1
    return ipAddress1,visiteurUnique,totalSession
    
def AnalyseTypeDoc (nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    l_typedoc=[]
    unidentifiedType=0
    for data in dict1 :
        if re.match("^.*[.].*$",data['path']) != None :
            typeDoc=data['path'].split('.')
            if "?" in typeDoc[1] :
                typeDoc1=typeDoc[1].split('?')
                l_typedoc.append(typeDoc1[0])
            else :
                l_typedoc.append(typeDoc[1])
        else :
            unidentifiedType=unidentifiedType+1
    analyseFormat=Counter(l_typedoc).most_common(10)
    return analyseFormat, unidentifiedType
    
#CLI
#nomFic=input('Nom de fichier log que vous souhaitez analyser : ')
my_parser = argparse.ArgumentParser(description="Analyser fichier log au format apache. Attention : il faut impérativement convertir le fichier log en format json (avec l'option --a) pour pouvoir l'utiliser ")

#help='Il faut impérativement convertir le fichier log en json pour pouvoir utiliser')

my_parser.add_argument('filename', type=argparse.FileType('r'),)

my_parser.add_argument('--a', action='store_true', help='changer le fichier en format JSON')#convertJSON
my_parser.add_argument('--b', action='store_true', help="analyser l'OS d'utilisateur" )#OSAnalyser
my_parser.add_argument('--c', action='store_true', help="calculer la taille moyenne de paquets demandés" )#AvgSize
my_parser.add_argument('--d', action='store_true', help="voir le trafic du jour sur le serveur" )#TraficduJour
my_parser.add_argument('--e', action='store_true', help="analyser la méthode de requête solicitée" )#AnalyseMethode
my_parser.add_argument('--f', action='store_true', help="voir l'heure creuse du serveur et le trafic en fonction d'heure" )#HeureCreuse
my_parser.add_argument('--g', action='store_true', help="analyser les réponses des requêtes" )#AnalyseResponse
my_parser.add_argument('--h', action='store_true', help="analyser les adresses IP de clients" )#AnalyseIPAdd
my_parser.add_argument('--i', action='store_true', help="analyser les 10 types de documents les plus demandés par client" )#AnalyseTypeDoc

args = my_parser.parse_args()
nom_fic=args.filename.name
nom_fic=nom_fic.split('.')
nom_fic=nom_fic[0]+'.json'
#print(nom_fic)
if args.a:
    convertJSON(args.filename.name)
#print(args.a)
#print(args.filename.name)

if args.b:
    resultat_OS=OSAnalyser(nom_fic)
    print(resultat_OS)
    
if args.c:
    resultat_avg=AvgSize(nom_fic)
    print(resultat_avg)
    
if args.d:
    resultat_trafic=TraficduJour(nom_fic)
    print(resultat_trafic)
    
if args.e:
    resultat_methode=AnalyseMethode(nom_fic)
    print(resultat_methode)
    
if args.f:
    resultat_heure_creuse=HeureCreuse(nom_fic)
    print(resultat_heure_creuse)
    
if args.g:
    resultat_reponse=AnalyseResponse(nom_fic)
    print(resultat_reponse)
    
if args.h:
    resultat_IP=AnalyseIPAdd(nom_fic)
    print(resultat_IP)
    
if args.i:
    resultat_type_doc=AnalyseTypeDoc(nom_fic)
    print(resultat_type_doc)

    