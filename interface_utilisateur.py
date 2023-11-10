# interface_utilisateur.py

class InterfaceUtilisateur:
    def __init__(self):
        pass

    def afficher_menu_principal(self):
        print("Menu Principal:")
        print("1. Afficher les formations")
        print("2. Afficher les projets en cours")
        print("3. Planifier une formation")
        print("4. Générer un rapport")
        print("5. Quitter")

    def get_choix_utilisateur(self):
        choix = input("Veuillez entrer votre choix : ")
        return choix

    def afficher_message(self, message):
        print(message)

# Exemple d'utilisation :

# interface = InterfaceUtilisateur()
# interface.afficher_menu_principal()
# choix = interface.get_choix_utilisateur()
# if choix == "1":
#     # Afficher les formations
#     pass
# elif choix == "2":
#     # Afficher les projets en cours
#     pass
# elif choix == "3":
#     # Planifier une formation
#     pass
# elif choix == "4":
#     # Générer un rapport
#     pass
# elif choix == "5":
#     # Quitter
#     pass
# else:
#     interface.afficher_message("Choix invalide, veuillez réessayer.")
