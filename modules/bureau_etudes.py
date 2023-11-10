# bureau_etudes.py

class BureauEtudes:
    def __init__(self, projet, responsable, date_debut, date_fin):
        self.projet = projet
        self.responsable = responsable
        self.date_debut = date_debut
        self.date_fin = date_fin

    def afficher_information(self):
        print(f"Projet : {self.projet}, Responsable : {self.responsable}, "
              f"Date de début : {self.date_debut}, Date de fin : {self.date_fin}")

# Exemple d'utilisation :
# projet1 = BureauEtudes("Conception d'une nouvelle application", "Bob Johnson", "2023-11-06", "2023-11-10")
# projet1.afficher_information()
