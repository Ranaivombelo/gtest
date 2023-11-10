# planification_formations.py

class PlanificationFormations:
    def __init__(self, titre_formation, date, lieu):
        self.titre_formation = titre_formation
        self.date = date
        self.lieu = lieu

    def afficher_information(self):
        print(f"Formation : {self.titre_formation}, Date : {self.date}, Lieu : {self.lieu}")

# Exemple d'utilisation :
# formation1 = PlanificationFormations("Python Avancé", "2023-11-06", "Salle de formation A")
# formation1.afficher_information()
