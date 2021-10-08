# !/usr/bin/python3
import random
nbATrouver= random.randint(1,100)
print(nbATrouver)
i=0
j=0
l=[]
while i <= 9 :
	nbDonne=int(input('Nombre choisi = '))
	l.append(nbDonne)
	while j < i :
		if l[i]==l[j] :
		 i=i-1
		j=j+1
		
	if nbATrouver > nbDonne :
		print('Trop petit')
	
	elif nbATrouver == nbDonne :
		print("c'est juste bravo!")
		i=9
		
	else :
		print('Trop grand')
		
	i=i+1
	
