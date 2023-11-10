# gestion_ressources.py

class GestionRessources:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def afficher_information(self):
        print(f"Ressource : {self.nom}, Quantité : {self.quantite}")

# Exemple d'utilisation :
# ressource1 = GestionRessources("Serveurs", 50)
# ressource1.afficher_information()
