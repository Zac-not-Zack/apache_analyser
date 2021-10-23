import json
import re
import argparse
from statistics import mean
from statistics import mode
from statistics import multimode
from collections import Counter
from datetime import date

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, packet size, referrer, system agent and browser 
#splitter :separer les textes dans une ligne afin de recuperer le temps, l'adresse ip, la requête, la code de réponse, la taille de paquet, le référent, le système d'exploitation et le navigateur
def splitter(line_to_parse):
    line = line_to_parse.split(' ')
    get = line_to_parse.split('"')
    usr_agent = get[5]
    list1 = dict(
        time = line[3]+' '+line[4],
        remote_ip = line[0],
        request = get[1],
        path = line[6],
        response = line[8],
        size = line[9],
        referrer = get[3],
        user_agent = usr_agent,
        system_agent = lire_OS(usr_agent),
        browser = lire_browser(usr_agent)
    )
    return list1

#lire_OS : pour identifier et afficher la version d'OS de la machine
def lire_OS(usr_agent):
    if "Windows" in usr_agent:
        sys_agent = "Windows"
        
    elif "Linux" in usr_agent:
        if "Android" in usr_agent:
            sys_agent = "Android"
        else:
            sys_agent = "Linux"            
    elif "Mac" in usr_agent:
        if "iPhone" in usr_agent:
            sys_agent = "iPhone OS"
        else:
            sys_agent="Mac OS"
    else:
        sys_agent = "OS unknown"
    return sys_agent

#lire_browser : pour identifier le navigateur de web
def lire_browser(usr_agent):
    if "Chrome" in usr_agent:
        browser = "Google Chrome"
    elif "Safari" in usr_agent:
        browser = "Safari"
    elif "MSIE" in usr_agent:
        browser = "MS Internet Explorer/Edge"
    elif "Firefox" in usr_agent:
        browser = "Mozilla Firefox"
    else:
        browser = "Web browser unknown or bot"
    return browser

#lire_log : fonction pour parser un document entier en utilisant splitter   
def lire_log (nom_fic):
    f = open(nom_fic, "r")
    list2 = []
    for l in f:
        list2.append(splitter(l))
    f.close()
    return list2

#convert_JSON : convert an apache log to json 
#convert_JSON : convertir un apache log à json   
def convert_JSON(nom_fic):
    list2 = []
    with open(nom_fic, "r") as f:
        nom_fic2 = nom_fic[:-4]+".json"
        for l in f:
            list2.append(splitter(l))
    with open(nom_fic2, "w") as f2:
        json.dump(list2, f2, indent=4)
    return list2
        
#count_OS : compter le nombre d'utilisateur qui utilise tel système d'exploitation pour acceder le serveur // afiche le nombre, le pourcentage et un diagramme circulaire      
def count_OS(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    result = {}
    for data in dict1:
        if data['system_agent'] not in result:
            result[data['system_agent']] = 1
        else:
            result[data['system_agent']] = result[data['system_agent']]+1
    string="\nLe nombre d'utilisateur qui utilise tel système d'exploitation pour acceder le serveur :\n\n"
    for os in result:
        string=string+"\t"+os+" : "+str(result[os])+'\n'
    string = string+stat_percentage(result)
    return string
            
#average_size : donne la taille moyenne des paquets pour un enregistrement apache  
def average_size (nom_fic_JSON):  
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    l_size = []
    for data in dict1 :
        if data['size'] != '-':
            size_float = float(data['size'])
            l_size.append(size_float)
    avgsize = mean(l_size)
    string = "\nLa taille moyenne est égale à : "+str(round(avgsize, 4)) 
    return string

#trafic_du_jour : calculer le nombre total de visiteur à jour actuel  
def trafic_du_jour (nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    today = date.today()
    today = today.strftime("%d/%B/%Y")
    nb_visiteur=0
    for data in dict1 :
        date1 = data['time'].split(':')
        date1[0] = date1[0][1:]
        if date1[0] == today :
            nb_visiteur = nb_visiteur+1
    string = "\nLe nombre total de visiteur aujourd'hui : "+str(nb_visiteur)
    return string
    
#count_method : compter le nombre de méthode utilisée par le monde pour acceder le serveur // afiche le nombre, le pourcentage et un diagramme circulaire
def count_method(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    result = {
        "GET" : 0,
        "POST" : 0,
        "HEAD" : 0,
        "PUT" : 0,
        "Others" : 0
    }
    for data in dict1:
        if "GET" in data['request']:
            result["GET"] = result["GET"]+1
        elif "POST" in data['request']:
            result["POST"] = result["POST"]+1
        elif "HEAD" in data['request']:
            result["HEAD"] = result["HEAD"]+1
        elif "PUT" in data['request']:
            result["PUT"] = result["PUT"]+1
        else :
            result["Others"]=result["Others"]+1  
    string = "\nLe nombre de méthode utilisée pour acceder le serveur :\n\n"
    for method in result:
        string = string+"\t"+method+" : "+str(result[method])+'\n'
    string = string+stat_percentage(result)
    return string

#heure_creuse : find peak hours  
#heure_creuse : trouver l'heure creuse
def heure_creuse(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
   
    l_heure = []
    for data in dict1:
        heure = data['time'].split(':')
        l_heure.append(heure[1])
    heure_creuse = mode(l_heure)
    string="\nL'heure quand il y'avait beacoup de session : "+str(heure_creuse)+'00h'
    return string 

#count_response : compter le nombre de code de réponse  // affiche le nombre (eg. "200" : 100), le pourcentage, et un diagramme circulaire   
def count_response(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    l_rep = []
    for data in dict1:
        l_rep.append(data['response'])
    result = Counter(l_rep)
    string = "\nLe nombre de code de réponse :\n\n"
    for response in result:
        string = string+'\t'+response+' : '+str(result[response])+'\n'
    string = string+stat_percentage(result)
    return string
    

#analyse_IP_addr : find 10 ip address that visited the server the most and users that visit only once   
#analyse_IP_addr : trouver 10 adresse ip qui visite le serveur le plus avec la fréquence et le nombre de visiteur unique
def analyse_IP_addr(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    l_ipaddress = []
    for data in dict1:
        l_ipaddress.append(data['remote_ip'])
    ip_addr1 = Counter(l_ipaddress).most_common(10) #Les 10 clients le plus fréquentés
    ip_addr2 = Counter(l_ipaddress)
    total_session = len(l_ipaddress)
    visiteur_unique = 0
    for ip_addr in ip_addr2 : #pour calculer visiteur unique
        if ip_addr2[ip_addr] == 1:
            visiteur_unique = visiteur_unique+1
    result = dict(ip_addr1) #change to dictionary
    string = "\n10 adresse IP qui visitent le serveur le plus sont :\n\n"
    placement = 1 #compteur pour placement
    for ip in result:
        string = string+'\t'+str(placement)+'. '+ip+' : '+str(result[ip])+'\n'
        placement = placement+1
    string = string+'\nLe nombre de visiteur unique : '+str(visiteur_unique)
    return string

#analyse_doc_type : trouver 10 type des documents le plus demandés avec la fréquence et le nombre de session qui le type est non identifiable
def analyse_doc_type(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    l_typedoc = []
    unidentified_type = 0
    for data in dict1:
        if re.match("^.*[.].*$",data['path']) != None:
            type_doc = data['path'].split('.')
            if "?" in type_doc[1] :
                type_doc1 = type_doc[1].split('?')
                l_typedoc.append(type_doc1[0])
            else:
                l_typedoc.append(type_doc[1])
        else:
            unidentified_type = unidentified_type+1
    analyse_format = Counter(l_typedoc).most_common(10)
    result = dict(analyse_format) #change to dictionary
    string='\n10 type des documents le plus demandé  :\n\n'
    placement = 1
    for doc in result:
        string = string+'\t'+str(placement)+'. '+doc+' : '+str(result[doc])+'\n'
        placement = placement+1
    string = string+'\nLe nombre de session dont le type de document est non identifiable  : '+str(unidentified_type)
    return string

#count_browser : compter le navigateur utilsé pour acceder le serveur // affiche le nombre, pourcentage et diagramme circulaire
def count_browser(nom_fic_JSON):
    with open(nom_fic_JSON, "r") as f:
        dict1 = json.load(f)
    result = {}
    for data in dict1:
        if data['browser'] not in result:
            result[data['browser']] = 1
        else:
            result[data['browser']] = result[data['browser']]+1
    string = '\nLe nombre de navigateur utilisé pour acceder le serveur :\n\n'
    for browser in result:
        string = string+"\t"+browser+" : "+str(result[browser])+"\n"
    string = string+stat_percentage(result)
    return string
    
#statistics in percentage
def stat_percentage(dict1):
    total = 0
    string = ""
    for data in dict1:
        total = total+dict1[data]
    for data in dict1:
        dict1[data] = str((round((dict1[data]/total)*100,2)))+"%"
    string = string+'\nLes donnée en pourcentage :\n\n'
    for data in dict1:
        string = string+"\t"+data+" : "+dict1[data]+"\n"
    return string   