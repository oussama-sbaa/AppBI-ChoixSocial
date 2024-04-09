import pandas as pd

# Chemin vers le fichier .soc
file_soc = 'Other_Profiles/00014-00000001.soc'
# Chemin de sortie pour le fichier .csv
file_csv = 'Profiles/socdata.csv'

# Lire le fichier .soc ligne par ligne, en supprimant la première colonne et en divisant les autres
data_lines = []
with open(file_soc, 'r', encoding='ISO-8859-1') as file:
    for line in file:
        # Supprime le numéro de la première colonne et le ':' puis divise les éléments restants
        parts = line.strip().split(': ')[1].split(',')
        data_lines.append(parts)

# Convertir en DataFrame et transposer
df = pd.DataFrame(data_lines).transpose()

# Enregistrer le DataFrame transposé en fichier .csv sans en-tête et sans index
df.to_csv(file_csv, header=False, index=False)
