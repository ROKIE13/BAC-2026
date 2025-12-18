import pandas
table=pandas.read_csv("exemple_pandas.csv")
print(table)
print(table.loc[1,"prenom"])               # a séléctionné seulement le prénom du p-uplet 1#
print(table.loc[:,"prenom"])               # a séléctionné tous les prénoms de la liste, les : servant à séléctionner un domaine de valeur (colonne) ou tous les indices#
print(table.loc[1,:])                      # a sélectionné toutes les coordonnées du p-uplet 1, les : servant ici à prendre tout ce qui le concerne#
print(table.loc[[1,2],["nom","prenom"]])   # a séléctionné les nom et prénom des p uplets 1 et 2, on a fait 2 sous tables pour plusieurs sélections distinctes#

#A l execution du fichier, on a indexé les p-uplets du fichier CSV#

