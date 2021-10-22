import json
import re
import argparse
from statistics import mean
from statistics import mode
from statistics import multimode
from collections import Counter
from datetime import date

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, packet size, referrer, system agent and browser 
def splitter(line_to_parse):
    line=line_to_parse.split(' ')
    get=line_to_parse.split("'")
    usr_agent=get[5]
    list1=dict(
        time=line[3]+' '+line[4],
        remote_ip=line[0],
        request=get[1],
        path=line[6],
        response=line[8],
        size=line[9],
        referrer=get[3],
        user_agent=usr_agent,
        system_agent=lire_OS(usr_agent),
        browser=lire_browser(usr_agent)
    )
    return list1

#lireOS : pour identifier et afficher la version d'OS de la machine
def lire_OS(usr_agent) :
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
#lireOS : pour identifier le navigateur de web
def lire_browser(usr_agent) :
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




#lire_log : fonction pour parser un document entier en utilisant splitter   
def lire_log (nom_fic) :
    f=open(nom_fic,"r")
    list2=[]
    for l in f:
        list2.append(splitter(l))
    return list2

#convert an apache log to json   
def convert_JSON(nom_fic) :
    list2=[]
    with open(nom_fic,"r") as f :
        nom_fic2=nom_fic[:-4]+".json"
        for l in f:
            list2.append(splitter(l))
    with open(nom_fic2,"w") as f2 :
        json.dump(list2,f2,indent = 4)
    return list2
        
#count number of users who uses x OS        
def count_OS(nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    result={}
    for data in dict1:
        if data['system_agent'] not in result:
            result[data['system_agent']]=1
        else:
            result[data['system_agent']]=result[data['system_agent']]+1
    return result
            
#give the average size of packet in byte for the total session   
def average_size (nom_fic_JSON) :  
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    l_size=[]
    for data in dict1 :
        if data['size'] != '-' :
            size_float=float(data['size'])
            l_size.append(size_float)
    avgsize=mean(l_size)   
    return avgsize

#calculate the number of visitor for x day    
def trafic_du_jour (nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    today=date.today()
    d=today.strftime("%d/%B/%Y")
    nb_visiteur=0
    for data in dict1 :
        date1=data['time'].split(':')
        if date1[0]==d :
            nb_visiteur=nb_visiteur+1
    return nb_visiteur
    
#HEAD,GET,POST,PUT,OTHERS
#find peak hours, types of files?if same website?response
# def count_method(nom_fic_JSON) :
#     with open(nom_fic_JSON,"r") as f :
#         dict1=json.load(f)
    
#     for data in dict1 :
#         if "GET" in data['request'] :
        
#         elif "POST" in data['request'] :
        
#         elif "HEAD" in data['request'] :
        
#         elif "PUT" in data['request'] :
        
#         else :
        
            
#     return result

#find peak hours  
def heure_creuse (nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
   
    l_heure=[]
    for data in dict1 :
        heure=data['time'].split(':')
        l_heure.append(heure[1])
    heureCreuse=mode(l_heure)
    #heureCreuse2=multimode(l_heure)
    return heureCreuse #,heureCreuse2

#count response code (eg. "200" : 100)   
def count_response (nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    l_rep=[]
    for data in dict1 :
        l_rep.append(data['response'])
    result=Counter(l_rep)
    return result

#find 10 ip address that visited the server the most and users that visit only once   
def analyse_IP_addr (nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    l_ipaddress=[]
    for data in dict1 :
        l_ipaddress.append(data['remote_ip'])
    ip_addr1=Counter(l_ipaddress).most_common(10) #Les 10 clients le plus fréquentés
    ip_addr2=Counter(l_ipaddress)
    total_session=len(l_ipaddress)
    visiteur_unique=0
    for ip_addr in ip_addr2 : #pour calculer visiteur unique
        if ip_addr2[ip_addr] == 1 :
            visiteur_unique=visiteur_unique+1
    result=dict(ip_addr1) #change to dictionary
    result["Unique Visitor"]=visiteur_unique
    return result

#give the frequency of type of document (eg. "png" : 100)  
def analyse_doc_type (nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    l_typedoc=[]
    unidentified_type=0
    for data in dict1 :
        if re.match("^.*[.].*$",data['path']) != None :
            type_doc=data['path'].split('.')
            if "?" in type_doc[1] :
                type_doc1=type_doc[1].split('?')
                l_typedoc.append(type_doc1[0])
            else :
                l_typedoc.append(type_doc[1])
        else :
            unidentified_type=unidentified_type+1
    analyse_format=Counter(l_typedoc).most_common(10)
    result=dict(analyse_format)
    result["Unidentified Type"]=unidentified_type
    return result

#count browser
def count_browser(nom_fic_JSON) :
    with open(nom_fic_JSON,"r") as f :
        dict1=json.load(f)
    result={}
    for data in dict1:
        if data['browser'] not in result:
            result[data['browser']]=1
        else:
            result[data['browser']]=result[data['browser']]+1
    return result
    
#statistics in percentage
def stat_percentage(nom_fic_JSON, count_function):
    dict1=count_function(nom_fic_JSON)
    total=0
    for data in dict1:
        total=total+dict1[data]
    for data in dict1:
        dict1[data]=str(round(dict1[data]/total,2))+'%'
    return dict1   

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
