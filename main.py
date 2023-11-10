# main.py

from formation import Formation
from services_informatiques import ServiceInformatique
from bureau_etudes import BureauEtudes
from gestion_projet import GestionProjet
from gestion_ressources import GestionRessources
from planification_formations import PlanificationFormations
from reporting import Reporting

# Exemple d'utilisation des classes

# Création d'une formation
formation1 = Formation("Python Avancé", "3 jours", "John Doe", "2023-11-06")
formation1.ajouter_participant("Alice")
formation1.ajouter_participant("Bob")

# Création d'un service informatique
service1 = ServiceInformatique("Maintenance Systèmes", "Jane Smith", 10)
service1.ajouter_projet("Mise à jour du serveur")
service1.ajouter_projet("Migration vers le cloud")

# Création d'un projet du bureau d'études
projet1 = BureauEtudes("Conception d'une nouvelle application", "Bob Johnson", "2023-11-06", "2023-11-10")

# Gestion de projet
projet2 = GestionProjet("Projet A", "Alice", "2023-11-06", "2023-11-10")

# Gestion des ressources
ressource1 = GestionRessources("Serveurs", 50)

# Planification des formations
formation2 = PlanificationFormations("Python Avancé", "2023-11-06", "Salle de formation A")

# Reporting
rapport1 = Reporting("Rapport Mensuel", "Financier")
rapport1.generer_rapport()

# Affichage des informations
formation1.afficher_information()
service1.afficher_information()
projet1.afficher_information()
projet2.afficher_information()
ressource1.afficher_information()
formation2.afficher_information()
