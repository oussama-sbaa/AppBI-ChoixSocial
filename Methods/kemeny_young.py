import pandas as pd
import itertools

def kemeny_young(votes):
    # Déterminer l'ensemble des alternatives
    alternatives = set(itertools.chain(*votes))

    # Calculer la matrice de préférence
    preference_matrix = {}
    for alt1 in alternatives:
        preference_matrix[alt1] = {}
        for alt2 in alternatives:
            preference_matrix[alt1][alt2] = 0
    for vote in votes:
        for i, alt1 in enumerate(vote):
            for alt2 in vote[i+1:]:
                preference_matrix[alt1][alt2] += 1

    # Calculer le classement Kemeny-Young
    min_score = float("inf")
    min_ranking = None
    for ranking in itertools.permutations(alternatives):
        score = sum(preference_matrix[ranking[i]][ranking[j]] for i in range(len(ranking)) for j in range(i+1, len(ranking)))
        if score < min_score:
            min_score = score
            min_ranking = ranking
    results = list(min_ranking)
    return results


def read_votes(file_name):
    data = pd.read_csv(file_name, header=None)
    votes = data.values.tolist()
    return votes

# Lecture des votes depuis le fichier CSV
file_name = '../Profiles/socdata.csv'
votes = read_votes(file_name)

# Appel à la fonction pour calculer le classement Kemeny-Young
ranking = kemeny_young(votes)

# Création d'un DataFrame Pandas pour afficher le classement par ordre
df_ranking = pd.DataFrame({'Candidat': ranking})

# Affichage du classement
print("Classement Kemeny-Young (par ordre) : ")
print(df_ranking)

# Affichage du candidat gagnant
print("\nLe gagnant est le candidat", ranking[0])
