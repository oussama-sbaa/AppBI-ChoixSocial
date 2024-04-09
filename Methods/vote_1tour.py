import pandas as pd

# Charger les données à partir du fichier CSV
data = pd.read_csv('../Profiles/socdata.csv', header=None)

# Initialiser un dictionnaire pour compter les votes
votes_count = {}

# Parcourir chaque colonne de données (chaque électeur)
for col in data:
    # Prendre le premier choix de l'électeur
    first_choice = data[col].iloc[0]
    # Compter le vote
    if first_choice in votes_count:
        votes_count[first_choice] += 1
    else:
        votes_count[first_choice] = 1

# Convertir le dictionnaire en une série pour faciliter l'affichage et l'analyse
votes_series = pd.Series(votes_count)

# Afficher le nombre de votes pour chaque candidat
print("Votes au premier tour par candidat :")
print(votes_series.sort_values(ascending=False).to_string())

# Identifier le gagnant du premier tour
winner = votes_series.idxmax()
winner_votes = votes_series.max()

# Afficher le gagnant
print(f"\nLe gagnant est le candidat numéro {winner} avec {winner_votes} votes.")
