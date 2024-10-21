import psycopg
from main import *
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Connexion à la base de données en utilisant les variables d'environnement
conn = psycopg.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

# Insertion des données dans la base de données
cur.execute('''
    INSERT INTO livres (couverture_url, titre, author, description, genre, annee_publication, avg_rating, nbre_rate, langue)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''', (
    data['cover_url'],
    data['title'],
    ', '.join(data['authors']),
    data['description'],
    ', '.join(data['genres']),
    data['year_of_publication'],
    data['avg_rating'],
    data['review_count'],
    data['language']
))

# Valider les changements
conn.commit()

# Fermer la connexion
conn.close()
