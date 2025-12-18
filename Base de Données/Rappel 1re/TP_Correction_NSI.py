from datetime import datetime
import csv

fichier = open("NSI.csv")

nsi = list(csv.DictReader(fichier, delimiter=';'))
nsi = [dict(n_uplet) for n_uplet in nsi]

def mise_en_coherence_nsi(n_uplet):
    n_uplet["Naissance"] = datetime.strptime(n_uplet["Naissance"], "%d/%m/%Y").date()
    return n_uplet
nsi = [mise_en_coherence_nsi(p_uplet) for p_uplet in nsi]

print(nsi)

# Exercice 3.2
print()
print([n_uplet["Nom"] for n_uplet in nsi if n_uplet["Nom"]<"C"])
print()
print([n_uplet["Nom"] for n_uplet in nsi if n_uplet["Naissance"].month<5 or n_uplet["Naissance"].month==5 and n_uplet["Naissance"].day<14])
print()
print([n_uplet["Nom"] for n_uplet in nsi if n_uplet["Sexe"]=="M" and n_uplet["Classe"]=="1G2" and n_uplet["LV2"]=="ESPAGNOL"])
print()

# Exercice 3.3
def nom(n_uplet):
    return n_uplet["Nom"]
print([n_uplet["Nom"] for n_uplet in sorted(nsi, key=nom, reverse=True)])
print()

# Exercice 3.4
print()
## Question 1
fichier = open("Client.csv")
clients = list(csv.DictReader(fichier))
clients = [dict(n_uplet) for n_uplet in clients]
fichier = open("Commande.csv")
commandes = list(csv.DictReader(fichier))
commandes = [dict(n_uplet) for n_uplet in commandes]

def mise_en_coherence_client(n_uplet):
    n_uplet["ID"] = int(n_uplet["ID"])
    return n_uplet
clients = [mise_en_coherence_client(p_uplet) for p_uplet in clients]
def mise_en_coherence_commande(n_uplet):
    n_uplet["ID"] = int(n_uplet["ID"])
    n_uplet["Date"] = datetime.strptime(n_uplet["Date"], "%d/%m/%Y").date()
    n_uplet["Client"] = int(n_uplet["Client"])
    return n_uplet
commandes = [mise_en_coherence_commande(p_uplet) for p_uplet in commandes]
print(clients)
print(commandes)

## Question 2
def fusion(n_uplet_1, n_uplet_2):
    n_uplet = n_uplet_1.copy()
    for cle, valeur in n_uplet_2.items():
        n_uplet[cle] = valeur
    return n_uplet
print()
clients_commandes = []
for n_uplet_1 in clients:
    for n_uplet_2 in commandes:
        if n_uplet_1["ID"] == n_uplet_2["Client"]:
            clients_commandes.append(fusion(n_uplet_1, n_uplet_2))
print(clients_commandes)

## Question 3
for n_uplet in clients_commandes:
    n_uplet["ID_Client"] = n_uplet.pop("Client")
    n_uplet["ID_Commande"] = n_uplet.pop("ID")
print()
print(clients_commandes)
