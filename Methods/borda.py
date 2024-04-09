import pandas as pd
import numpy as np

def borda_vote(data):
    num_candidates = int(data.max().max())  # Trouver le nombre total de candidats
    borda_counts = pd.Series(0, index=np.arange(1, num_candidates + 1))

    # Attribuer des points Borda à chaque position de préférence
    for col in data.columns:
        for rank, candidate in enumerate(data[col], start=1):
            borda_counts[candidate] += num_candidates - rank

    # Afficher les scores de Borda pour chaque candidat
    print("Scores Borda par candidat :")
    print(borda_counts.sort_values(ascending=False).to_string(header=False))

    # Identifier le gagnant avec le score Borda le plus élevé
    winner = borda_counts.idxmax()
    max_points = borda_counts.max()

    print(f"\nLe gagnant est le candidat numéro {winner} avec {max_points} points Borda.")

    return winner

# Charger les données à partir du fichier CSV
data = pd.read_csv('../Profiles/socdata.csv', header=None)

# Lancer la méthode de vote de Borda
winner = borda_vote(data)
