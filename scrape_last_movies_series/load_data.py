import mysql.connector
import pandas as pd

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="movies_series"
)

cursor = conn.cursor()

# Lire les données transformées à partir du fichier CSV
transformed_movies_data = "scrape_last_movies_series\\transformed_movies.csv"
transformed_df = pd.read_csv(transformed_movies_data)

# Supprimer les lignes contenant des valeurs NaN
transformed_df.dropna(inplace=True)

# Insertion de chaque film dans la table en évitant les doublons
for index, movie in transformed_df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO movies_table (movie_name, categories, movie_rate, description, country, release_date, duration, movie_link)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        movie['movie_name'],
        movie['categories'],
        movie['movie_rate'],
        movie['description'],
        movie['country'],
        movie['release_date'],
        movie['duration'],
        movie['movie_link']
    ))

# Lire les données transformées à partir du fichier CSV
transformed_series_data = "scrape_last_movies_series\\transformed_series.csv"
transformed_df_series = pd.read_csv(transformed_series_data)

# Supprimer les lignes contenant des valeurs NaN
transformed_df_series.dropna(inplace=True)

# Insertion de chaque série dans la table en évitant les doublons
for index, serie in transformed_df_series.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO series_table (serie_name, season_episode, categories, serie_rate, description, country, duration, movie_link)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        serie['serie_name'],
        serie['season_episode'],
        serie['categories'],
        serie['serie_rate'],
        serie['description'],
        serie['country'],
        serie['duration'],
        serie['serie_link']
    ))

# Valider les modifications
conn.commit()

# Fermer la connexion
cursor.close()
conn.close()

print("Données ajoutées avec succès à la table des séries.")
print("Données ajoutées avec succès à la table des movies.")

