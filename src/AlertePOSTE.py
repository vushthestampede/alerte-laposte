# Laurent, programme pour le service en interne, Sept 2019

def menu():
    # TODO Bravo
    consigne = """
*****************************************************************
                Bonjour.

        Voici un petit programme qui va vous permettre, 
    à partir des fichiers connexion.log et warning.txt, de : 

    1 : Créer un fichier contenant la liste des utilisateurs 
        qui se sont connectés.

    2 : Afficher la liste des utilisateurs qui se sont connectés 
        en dehors des heures autorisées.

    3 : Créer un fichier contenant la liste des utilisateurs
        suspects.

    0 : *****    Quiter    *****

Entrez UNIQUEMENT 1, 2, 3 ou 0 : """

    nom = input("""
      ****************************************************
      ***** Pré-requis vous devez avoir vos fichiers *****
      *****       connexion.log et warning.txt       *****
      *****         dans /Documents/Projet1/         *****
      ****************************************************
    
            Entrez votre nom d'utilisateur : """)

    choix = int(input(consigne))
    
    while choix != 0 :
        if choix == 1 :
            # Ouverture en lecture du fichier source
            cnx_log = open("/home/" + nom + "/Documents/Projet1/connexion.log", 'r')
            # Ouverture en écriture du fichier destination
            user_txt = open("/home/" + nom + "/Documents/Projet1/utilisateurs.txt", "w")
            # La liste de connexions que je nomme ping
            cnx_list = []

            with cnx_log as f :
            # Pour chaques lignes du fichier ouvert
                for line in f :
            # On sépare à chaque ";" et prend en compte le 2ème élément
                    cnx_list.append(line.split(";")[1])
            # On crée le fichier utilisateurs.txt avec un retour à la ligne à chaque objet
            with user_txt as f :
                    f.write("\n".join(cnx_list))

            print("""
*****************************************************************
Le fichier utilisateur.txt est dans ==> /home/""" + nom + """/Documents/Projet1/
*****************************************************************
""")
            
        elif choix == 2 :
            # Ouverture en lecture du fichier source
            cnx_log = open("/home/" + nom + "/Documents/Projet1/connexion.log", 'r')

            with cnx_log as f:
                for line in f :
            # On coupe à chaque ligne à chaque espace pour définir 2 sous-objets l'identification de connexion et l'horodatage)
                    cnx_id , timestamp = line.split(" ")               
            # On définit les connexions en-dehors des heures autorisées par une comparaison
                    if "19:00" <= str(timestamp) or str(timestamp) <= "08:00" :
            # On affiche les lignes concernées
                        print(" ")
                        print(cnx_id , timestamp)

            print("""
*****************************************************************
***** Voici la liste des utilisateurs qui se sont connectés *****
*****           en dehors des heures autorisées.            *****
*****************************************************************
""")

        elif choix == 3 :
            # Ouverture en lecture du fichier source des IP dangereuses
            warning_txt = open("/home/" + nom + "/Documents/Projet1/warning.txt", 'r')
            # Fichier source des connexions
            cnx_log = open("/home/" + nom + "/Documents/Projet1/connexion.log", 'r')
            # Ouverture en écriture du fichier destination des suspects
            suspect_txt = "/home/" + nom + "/Documents/Projet1/suspect.txt"
            # Liste des IP dangereuses
            warning_list = []
            # Liste des Suspects
            suspect_list = []

            # On définit la liste des IP dangereuses
            with warning_txt as f :
                for line in f :
                    warning_list.append(line.strip())
            #print(warning_list)   #####pour debugage

            # On définit la liste complète des connexions du fichier connexion.log
                with cnx_log as g :
                    for line in g :
            # On coupe à chaque ligne à chaque ";" pour définir 3 sous-objet IP, nickname et horodatage
                        ip , nick , timestamp = line.split(";")

                        #print(ip)   #####pour debugage
            # Si tu rencontre une IP de la warning_list, ajoute moi les nickname
                        if ip in warning_list :
                            suspect_list.append(nick)
                            #print(nick)   #####pour debugage

            # Tri par ordre décroissant du nombres de connexions
            from collections import Counter
            new_suspect_dict = Counter(suspect_list).most_common()

            # Formatage en string avec retour à la ligne
            list_txt = ""
            for i in new_suspect_dict :
                name, count = i
                list_txt += name + ":" + str(count) + "\n"
                #print(list_txt)   #####pour debugage

            # On crée le fichier suspect.txt
            with open(suspect_txt, 'w') as h :
                h.write(list_txt)

            print("""
*****************************************************************
Le fichier suspect.txt est dans ==> /home/""" + nom + """/Documents/Projet1/
*****************************************************************
""")

        else :
            print("""

   *********************************************************        
   *****    Saisie incorrect. Veuillez recommencer.    *****
   *********************************************************
""")
        
        choix = int(input("""
Entrez UNIQUEMENT 1, 2, 3 ou 0 : """))

    print("""
               *********************************
               *****    Bonne journée :)   *****
               *********************************
""")

menu()