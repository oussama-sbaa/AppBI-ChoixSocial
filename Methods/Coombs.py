import pandas as pd
import warnings

warnings.filterwarnings("ignore")

def read_file(file_name):
    data = pd.read_csv(file_name, encoding="ISO-8859-1", header=None)
    data.index += 1
    return data

def coombs(data):
    majority = len(data.columns) / 2
    tour = 1  # Initialise le compteur de tours
    while data.shape[1] > 1:
        # Compter les votes en première place pour chaque candidat
        first_place_counts = data.iloc[0].value_counts()

        # Trouver le candidat en tête
        current_winner = first_place_counts.idxmax()
        current_winner_votes = first_place_counts.max()

        # Vérifier si ce candidat a la majorité absolue
        if current_winner_votes > majority:
            print(f"Le candidat numéro {current_winner} a gagné avec la majorité absolue.")
            break

        # Identifier le candidat avec le plus de votes en dernière place
        last_place_counts = data.apply(lambda x: x.value_counts().index[-1]).value_counts()
        eliminated = last_place_counts.idxmax()

        # Annoncer l'élimination
        print(f"Tour {tour} - Candidat éliminé: {eliminated}")

        # Éliminer le candidat des données
        data = data.applymap(lambda x: None if x == eliminated else x)
        data = data.apply(lambda x: pd.Series(x.dropna().values))

        tour += 1  # Incrémenter le compteur de tours

# Appel des fonctions
file_name = '../Profiles/profil1.csv'
data = read_file(file_name)
coombs(data)
