import os
import subprocess

def execute_script(script_path):
    try:
        # Utilisation de subprocess pour exécuter chaque script
        result = subprocess.run(['python', script_path], check=True, text=True)
        print(f"Exécution réussie : {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_path}: {e}")

def main():
    print("Début de l'exécution de l'application")

    # Étape 1 : Scraping des films and séries
    print("Scraping des films...")
    execute_script('scrape_last_movies_series\\scrape_last_movies_series.py')

    # Étape 2 : Transformation des données
    print("Transformation des données des films et des séries...")
    execute_script('scrape_last_movies_series\\transform_data_movies.py')
    execute_script('scrape_last_movies_series\\transform_data_series.py')

    # Étape 3 : Chargement des données dans la base de données
    print("Chargement des données dans la base de données...")
    execute_script('scrape_last_movies_series\\load_data.py')

    print("Exécution de l'application terminée avec succès")

if __name__ == "__main__":
    main()
