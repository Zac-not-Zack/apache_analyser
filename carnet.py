# !/usr/bin/python3
from login import loginPropre
carnet={}
lnom=[]
lprenom=[]
llogin=[]
i=0
while i <= 5 :
	nom=input('Saisissez un nom svp : ')
	prenom=input('Saisissez un prénom svp : ')
	login=loginPropre(nom,prenom)
	lnom.append(nom)
	lprenom.append(prenom)
	llogin.append(login)
	carnet[login]=[lnom[i],lprenom[i]]
	i=i+1

for j in carnet.items():
	print(j)
	

	
cherche=input('Saissisez un login pour lancer la recherche : ')
#print(cherche)
#cle=carnet.keys()
#print(cle)

if cherche in carnet.keys() :
	print(carnet[cherche])

else :
	print('login inconnu')

#for key in carnet.keys():
#	if key == cherche :
#		print(carnet[key])
#	else :
#		print('login inconnu')
		
		
#if cherche in dict_keys ==True : tnya mr!!!
#	print('yes')


