# gestion_projet.py

class GestionProjet:
    def __init__(self, nom, responsable, date_debut, date_fin):
        self.nom = nom
        self.responsable = responsable
        self.date_debut = date_debut
        self.date_fin = date_fin

    def afficher_information(self):
        print(f"Nom du Projet : {self.nom}, Responsable : {self.responsable}, "
              f"Date de début : {self.date_debut}, Date de fin : {self.date_fin}")

# Exemple d'utilisation :
# projet1 = GestionProjet("Projet A", "Alice", "2023-11-06", "2023-11-10")
# projet1.afficher_information()
