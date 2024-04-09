import pandas as pd

def alternative_vote(data):
    while len(data.columns) > 0:
        first_pref_counts = data.iloc[0].value_counts().sort_index()
        first_pref_counts.index = first_pref_counts.index.astype(int)
        first_pref_counts = first_pref_counts.astype(int)

        print("Répartition des votes actuelle :")
        print(first_pref_counts.to_string(header=False))  # Converti en chaîne sans en-tête
        print()

        total_votes = first_pref_counts.sum()
        majority = total_votes // 2 + 1
        if (first_pref_counts >= majority).any():
            winner = first_pref_counts.idxmax()
            print(f"Le gagnant est le candidat numéro {winner} avec {first_pref_counts[winner]} votes.\n")
            break

        candidate_to_eliminate = first_pref_counts.idxmin()
        data = data.apply(lambda col: col[col != candidate_to_eliminate]).apply(lambda col: col.dropna().reset_index(drop=True))
        print(f"Candidat numéro {candidate_to_eliminate} éliminé.\n")

        if len(data.iloc[0].unique()) == 2:
            print("Dernier décompte entre les deux finalistes :")
            first_pref_counts = data.iloc[0].value_counts()
            first_pref_counts.index = first_pref_counts.index.astype(int)
            first_pref_counts = first_pref_counts.astype(int)
            print(first_pref_counts.to_string(header=False))  # Converti en chaîne sans en-tête
            winner = first_pref_counts.idxmax()
            print(f"Le gagnant final est le candidat numéro {winner} avec {first_pref_counts[winner]} votes.\n")
            break

    return winner

data = pd.read_csv('../Profiles/socdata.csv', header=None)
winner = alternative_vote(data)
