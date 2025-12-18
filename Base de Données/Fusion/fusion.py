import pandas
client = pandas.read_csv("Fusion/Client.csv")
commande = pandas.read_csv("Fusion/Commande.csv")
client_commande = pandas.merge(client, commande, right_on = "Client", left_on = "ID")
print(client_commande)

#4a : elle n'affiche rien car rien ne les lie au general#
#4b : right_on correspond au domaine"Client" dans le 2e argument, celui de droite (commande) et left_on au domaine"ID" du 1er argument celui de gauche(client). Du coup, on a réussi à les lier à un point commun pour fusionner