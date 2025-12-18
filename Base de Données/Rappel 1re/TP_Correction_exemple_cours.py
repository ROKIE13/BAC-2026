import csv
fichier = open("exemple_cours.csv")

table = list(csv.DictReader(fichier))
table = [dict(n_uplet) for n_uplet in table]

print(table) # Pour répondre à la question 1
print(table[1]["prenom"]) # 2a
print(table[2]["date_naissance"]) # 2b
print(table[-1]) # 3a
print([e["nom"] for e in table]) # 3b
print([(e["nom"], e["date_naissance"]) for e in table[:2]]) # 3c
print([{"nom": e["nom"], "date_naissance": e["date_naissance"]} for e in table[:2]]) # 3c encore mieux
