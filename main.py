

# 1. Créer une classe Livre avec des attributs : titre, auteur, année_publication.
#     - Méthode __str__ pour afficher les informations du livre.

# 2. Créer une classe Bibliotheque qui gère une collection de livres.
#     - Attributs : dictionnaire 'livres' avec titre comme clé et objet Livre comme valeur.
#     - Méthodes :
#         - ajouter_livre(titre, auteur, année)
#         - supprimer_livre(titre)
#         - afficher_inventaire()
#         - rechercher_livre(titre ou auteur)
#         - sauvegarder_inventaire(fichier)
#         - charger_inventaire(fichier)

# 3. Créer une interface utilisateur ( invite de commande ):
#     - Boucle principale pour afficher un menu avec les choix suivants :
#         1. Ajouter un livre
#         2. Supprimer un livre
#         3. Afficher l'inventaire
#         4. Rechercher un livre
#         5. Sauvegarder l'inventaire
#         6. Charger l'inventaire
#         7. Quitter
#     - Gérer les choix de l'utilisateur et appeler les méthodes correspondantes.
#     - Utiliser try/except pour gérer les erreurs d'entrée (ex : mauvaise sélection, fichier non trouvé).

# 4. Sauvegarde/Chargement :
#     - Utiliser le module `json` pour sauvegarder et charger les données de la bibliothèque dans un fichier au format JSON.


# 5. Amélioration
#     - Charger tous les livres au lancement du programme pour permettre directement la recherche
#     - Implementer une fonction qui va permettre la modification des éléments d'un livre dans la base des fichiers
#     - permettre de charger plusieurs livres dans la bibliothèque; A l'etat actuel, a chaque chargement, notre dictionnaire qui permet de sauvegarder les livres est écrasé:


# solution du point 3


# def charger_inventaire(self, fichier):
#     if not os.path.exists(fichier):
#         raise FileNotFoundError("Le fichier n'existe pas.")
#     with open(fichier, 'r') as f:
#         donnees = json.load(f)
#         for titre, livre in donnees.items():
#             if titre not in self.livres:  # Ne pas écraser les livres existants
#                 self.livres[titre] = Livre(**livre)
#             else:
#                 print(f"Le livre '{titre}' existe déjà dans l'inventaire et n'a pas été remplacé.")
#     print(f"Inventaire chargé depuis {fichier}")
#     self.afficher_inventaire()




import json
import os

class Livre:
    def __init__(self, titre, auteur, anne_publication) -> None:
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = anne_publication
        
    def __str__(self) -> str:
        return f" votre livre {self.titre}, écrit par {self.auteur} et publié en {self.annee_publication}"
        
class Bibliotheque:
    def __init__(self) -> None:
        
        self.livres = {} # ce dictionnaire aura en clé le titre du livre et en valeur l'objet livre
    
    def ajouter_livre(self, livre: Livre) -> None:
        
        if livre.titre in self.livres:
            raise ValueError("Ce livre est déjà présent")
        else:
            
            self.livres[livre.titre] = livre
            print(f"Votre livre {livre.titre} a bien été ajouté")
            
    def supprimer_livre(self, titre: str) -> None:
        
        if titre not in self.livres:
            raise ValueError("Ce livre n'est pas présent dans l'inventaire !!")
        else:
            
            del self.livres[titre]
            
            print(f"Votre livre {titre} a bien été supprimé")
            
    def afficher_inventaire(self)-> None:
        
        if self.livres:
            for livre in self.livres.values():
                print(livre)
        else:
            raise ValueError("Cet inventaire est vide")
        
    def rechercher_livre(self, mot_cle: str) -> None:
        
        # rechercher se fait sur le titre du livre et nom de l'auteur
        
        
        # for livre in self.livres.values():
        #     if mot_cle in livre.titre or mot_cle in livre.auteur:
        #         resultats.append(livre)
                
        resultats = [livre  for livre in self.livres if mot_cle.lower() in livre.titre.lower() or mot_cle.lower() in livre.auteur.lower()]
        
        for livre in resultats:
            print(livre)
    
    def sauvegarder_inventaire(self, fichier: str) -> None:
        
        with open(fichier, 'a') as f:
            
            for titre, livre in self.livres.items():
                
                json.dump({
                    titre: livre.__dict__
                }, f)
            
            print("l'inventaire a été sauvegardé")
            
    def chager_inventaire(self, fichier: str) -> None:
        
        if os.path.exists(fichier):
    
            with open(fichier, "r") as f:
                
                donnees = json.load(f)
                
                for titre, livre in donnees.items():
                    
                    livre_obj = Livre(titre=livre["titre"], auteur=livre["auteur"], anne_publication=livre["annee_publication"])
                    
                    print(livre_obj)
                    
                    self.livres[titre] = livre_obj     
                    
            self.afficher_inventaire()
        else:
            raise FileNotFoundError("Fichier non trouvé")
      

def menu():
    
    bibliotheque = Bibliotheque()
    
    while True:
        
        print("======= Menu ========")
        print("1. Ajouter un livre ")
        print("2. Supprimer un livre")
        print("3. rechercher un livre")
        print("4. Afficher un inventaire ")
        print("5. Sauvegarder un inventaire")
        print("6. Charger un inventaire")
        
        print("7. Quitter le programme ")
        
        choix = input("Veuillez faire un choix dans ce menu : ")
        
        if choix == "1":
            print("Ok, vous voulez ajouter un livre ")
            print(" ====== =======")
            titre = input("le titre du livre ? : ")
            auteur = input("Auteur du livre ? : ")
            annee_publication = input("Année de publication du livre ? : ")
            
            livre = Livre(titre=titre, auteur=auteur, anne_publication=annee_publication)
            
            try:
                bibliotheque.ajouter_livre(livre=livre)
            except ValueError as e:
                print(e)
            
        elif choix == "2":
            print("Ok, vous voulez supprimer un livre ")
            
            titre = input("le titre du livre ? : ")
            
            try:
                bibliotheque.supprimer_livre(titre=titre)
            except ValueError as e:
                print(e)
            
        elif choix == "3":
            
            print("Ok, vous voulez rechercher un livre ")
            
            mot_cle = input("Entrer un mot clé")
            
            bibliotheque.rechercher_livre(mot_cle=mot_cle)
            
        elif choix == "4":
            
            print("ok, vous voulez afficher l'inventaire de livre ")
            
            bibliotheque.afficher_inventaire()
            
        elif choix == "5":
            
            print("ok, vous voulez sauvegarder un inventaire")
            
            fichier = input("le nom du fichier ? : ")
            
            bibliotheque.sauvegarder_inventaire(fichier=fichier)
            
        elif choix == "6":
            
            print("ok, vous voulez charger un inventaire")
            
            fichier = input("le nom du fichier ? : ")
            
            try:
                bibliotheque.chager_inventaire(fichier=fichier)
            except FileNotFoundError as e:
                print(e)
                
        elif choix == "7":
            print("ok, vous voulez quitter le programme ")
            break
        
        else:
            
            print("Veuillez entrer un choix valide")
    


if __name__ == "__main__":
    
    menu()
    
