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
