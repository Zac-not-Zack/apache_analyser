import json

#count browser
def count_browser(nomFicJSON) :
    with open(nomFicJSON,"r") as f :
        dict1=json.load(f)
    result={}
    for data in dict1:
        if data['browser'] not in result:
            result[data['browser']]=1
        else:
            result[data['browser']]=result[data['browser']]+1
    return result
    