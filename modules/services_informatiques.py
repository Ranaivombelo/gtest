# services_informatiques.py

class ServiceInformatique:
    def __init__(self, nom, responsable, effectif):
        self.nom = nom
        self.responsable = responsable
        self.effectif = effectif
        self.liste_projets = []

    def afficher_information(self):
        print(f"Nom : {self.nom}, Responsable : {self.responsable}, Effectif : {self.effectif}")

    def ajouter_projet(self, projet):
        self.liste_projets.append(projet)

    def afficher_projets(self):
        print("Liste des projets en cours :")
        for projet in self.liste_projets:
            print(projet)

# Exemple d'utilisation :
# service1 = ServiceInformatique("Maintenance Systèmes", "Jane Smith", 10)
# service1.afficher_information()
# service1.ajouter_projet("Mise à jour du serveur")
# service1.ajouter_projet("Migration vers le cloud")
# service1.afficher_projets()
