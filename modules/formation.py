# formation.py

class Formation:
    def __init__(self, titre, duree, formateur, date):
        self.titre = titre
        self.duree = duree
        self.formateur = formateur
        self.date = date
        self.liste_participants = []

    def afficher_information(self):
        print(f"Titre : {self.titre}, Durée : {self.duree}, Formateur : {self.formateur}, Date : {self.date}")

    def ajouter_participant(self, participant):
        self.liste_participants.append(participant)

    def afficher_participants(self):
        print("Liste des participants :")
        for participant in self.liste_participants:
            print(participant)

# Exemple d'utilisation :
# formation1 = Formation("Python Avancé", "3 jours", "John Doe", "2023-11-06")
# formation1.afficher_information()
# formation1.ajouter_participant("Alice")
# formation1.ajouter_participant("Bob")
# formation1.afficher_participants()
