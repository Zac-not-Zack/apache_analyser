# !/usr/bin/python3

def login (nom,prenom):
	#nom=input('Ton nom svp : ')
	#prenom=input('Ton prénom svp : ')
	login=prenom[0]+nom[:7]
	return login
	
def compteUtil (l):
	nom=l[0]
	prenom=l[1]
	login=prenom[0]+nom[:7]
	space=' '
	a=nom+space+prenom
	l2=[login, a]
	return l2 
	
def loginPropre (nom,prenom):
	nom=nom.translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
	prenom=prenom.translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
	login=prenom[0]+nom[:7]
	return login
	
	
def lireBase (nomFic):
	f=open(nomFic,"r")
	l4=[]
	for l in f:
		l2=l.split(";")
		nom=l2[0].translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
		prenom=l2[1].translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
		prenom=prenom[:-1]#pour enlever le caractère "\n"
		login=prenom[0]+nom[:7]
		nomprenom=nom+" "+prenom
		l3=[login,nomprenom]
		l4.append(l3)
	f.close()
	return l4
		
def lireCSV (nomFic):
	import csv
	l4=[]
	f=open(nomFic,"r")
	lignes=csv.reader(f,delimiter=';')
	for l in lignes:
		nom=l[0].translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
		prenom=l[1].translate({ord(' '):None,ord('-'):None,ord('à'):ord('a'),ord('é'):ord('e'),ord('ç'):ord('c'),ord('ù'):ord('u'),ord('à'):ord('a'),ord('è'):ord('e'),ord('ô'):ord('o')})
		login=prenom[0]+nom[:7]
		nomprenom=nom+" "+prenom
		l3=[login,nomprenom]
		l4.append(l3)
		nomFic2=nomFic[:-4]+"-resultat.csv"
		f2=open(nomFic2,"a")
		f2.write(login+";"+nom+";"+prenom+"\n")
		
def lireUnLien (nomFic) :
	#from html.parser import HTMLParser
	import re 
	#class monLecteurHTML (HTMLParser):
	f=open(nomFic,"r")
	l2=[]
	for l in f:
		l3=re.findall('href.*$',l)#dans une ligne le résultat
		a=l3[0]
		a=a[6:-2]
		l2.append(a)
	return l2
	
def lireUnHTML (nomFic) :
	from html.parser import HTMLParser
	import re
	l2=[]
	class monLecteurHTML (HTMLParser):
		def __init__(self):
			super().__init__()	
			
		def handle_starttag(self,tag,attrs):
				for name,value in attrs :
					if name == 'href' :
						print(value)
						l2=value
						l2.append(l2)
	a= monLecteurHTML()
	a.feed(nomFic)
	return a
