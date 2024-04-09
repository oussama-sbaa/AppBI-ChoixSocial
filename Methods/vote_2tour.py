import pandas as pd

# Charger les données à partir du fichier CSV
data = pd.read_csv('../Profiles/socdata.csv', header=None)

# Initialiser un dictionnaire pour compter les votes du premier tour
votes_count_first_round = {}

# Parcourir chaque colonne de données (chaque électeur)
for col in data:
    # Prendre le premier choix de l'électeur
    first_choice = data[col].iloc[0]
    # Compter le vote
    votes_count_first_round[first_choice] = votes_count_first_round.get(first_choice, 0) + 1

# Convertir en série pour faciliter l'analyse
votes_series_first_round = pd.Series(votes_count_first_round)

# Afficher le nombre de votes pour chaque candidat
print("Votes au premier tour par candidat :")
print(votes_series_first_round.sort_values(ascending=False).to_string())

# Vérifier la majorité absolue
total_votes = len(data.columns)
majority = total_votes / 2
winner_first_round = votes_series_first_round.idxmax()
votes_winner_first_round = votes_series_first_round.max()

if votes_winner_first_round > majority:
    print(f"\nLe gagnant est le candidat numéro {winner_first_round} avec {votes_winner_first_round} votes.")
else:
    # Identifier les deux candidats pour le second tour
    candidates_second_round = votes_series_first_round.nlargest(2).index

    # Initialiser un dictionnaire pour les votes du second tour
    votes_count_second_round = {candidate: 0 for candidate in candidates_second_round}

    # Parcourir les votes pour le second tour
    for col in data:
        # Trouver le vote de l'électeur pour le candidat le plus élevé restant
        for vote in data[col]:
            if vote in candidates_second_round:
                votes_count_second_round[vote] += 1
                break

    # Convertir en série pour faciliter l'analyse
    votes_series_second_round = pd.Series(votes_count_second_round)

    # Afficher le résultat du second tour
    print("Votes au second tour par candidat :")
    print(votes_series_second_round.sort_values(ascending=False).to_string())

    # Déterminer le gagnant du second tour
    winner_second_round = votes_series_second_round.idxmax()
    print(
        f"\nLe gagnant après le deuxième tour est le candidat numéro {winner_second_round} avec {votes_series_second_round.max()} votes.")
