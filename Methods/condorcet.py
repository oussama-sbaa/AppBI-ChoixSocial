import pandas as pd
import warnings


warnings.filterwarnings("ignore")

def condorcet(file_name):
    def get_occurrence_classement(data_set, columns):
        nbr_occur_class = []
        print("Nombre de classements distincts disponibles : ", data_set.T.drop_duplicates().T.shape[1])
        data_unique = data_set.T.drop_duplicates().T
        data_unique = data_unique.T

        for feature in data_set.T.groupby(columns).groups.values():
            data_unique.loc[feature[0], "number"] = feature.shape[0]
            nbr_occur_class.append(feature.shape[0])
        # Trie les classements selon leurs occurrences dans l'ordre décroissant
        data_unique = data_unique.sort_values(by=["number"], ascending=False)

        return data_unique

    def copland(condorcet, columns):
        classement = pd.DataFrame(columns=["candidat", "points"], data={"candidat": columns})

        for i in range(1, len(columns) + 1):
            mask = condorcet[i] < condorcet.loc[i, :]
            classement.loc[i - 1, "points"] = mask[mask == True].shape[0] - (mask[mask == False].shape[0] - 1)

        classement.sort_values(by=["points"], ascending=False, inplace=True, ignore_index=True)
        print(classement, "\n")

    def min_max(condorcet, columns):
        classement = pd.DataFrame(data={"candidat": columns, "points": condorcet.max(axis=0).values})
        classement.sort_values(by=["points"], ascending=True, inplace=True, ignore_index=True)

        print("Le classement avec la méthode min_max : ")
        print(classement, "\n")

    data = pd.read_csv(file_name, encoding="ISO-8859-1", header=None)
    data.index += 1
    columns = list(data.index)
    data_unique = get_occurrence_classement(data, columns)

    condorcet = pd.DataFrame(columns=columns)
    for i in range(1, len(columns) + 1):
        for j in range(i + 1, len(columns) + 1):
            for_first = data_unique.loc[
                data_unique[i] < data_unique[j], "number"].agg('sum')
            for_second = data.shape[1] - for_first

            condorcet.loc[i, j] = for_first
            condorcet.loc[j, i] = for_second

    print("Le tableau de Condorcet : ")
    condorcet.fillna(0, inplace=True)
    print(condorcet, "\n")

    gagnant = False

    for i in range(1, len(columns) + 1):
        mask = condorcet[i] < condorcet.loc[i, :]
        if mask[mask == True].shape[0] == len(columns) - 1:
            print("Le gagnant avec la méthode de Condorcet est le candidat numéro :", i, "\n")

            gagnant = True
    if not gagnant:
        print("Il n'y a aucun candidat gagnant avec la méthode de Condorcet.\n")
        min_max(condorcet, columns)
        copland(condorcet, columns)

condorcet('../Profiles/socdata.csv')
