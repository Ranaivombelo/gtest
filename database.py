# database.py

import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error fetching data: {e}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Exemple d'utilisation :

# Création d'une instance de la base de données
db = Database(host="localhost", user="root", password="password", database="milamina_db")

# Exemple d'exécution d'une requête
query = "INSERT INTO formations (titre, duree, formateur, date) VALUES ('Python Avancé', '3 jours', 'John Doe', '2023-11-06')"
db.execute_query(query)

# Exemple de récupération de données
select_query = "SELECT * FROM formations"
result = db.fetch_data(select_query)
for row in result:
    print(row)

# Fermeture de la connexion
db.close_connection()
