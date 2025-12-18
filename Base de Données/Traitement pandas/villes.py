import pandas
infos_villes = pandas.read_csv("Traitement pandas/villes_virgule.csv") #Traitement pandas/ : on a ouvert un dossier dans ce dossier bASE DE DONNÉES POUR TROUVER ET EXECUTER LE FICHIER)
print(infos_villes)
print(infos_villes.loc[infos_villes["alt_min"]>1500,["nom","alt_min"]])
print(infos_villes.loc[infos_villes["dens"]<50,["nom","alt_min","dens"]])
print(infos_villes.loc[(infos_villes["dens"]>50 )&(infos_villes["alt_min"]>1500), ["nom"]])
print(infos_villes.loc[:,"alt_min"].mean())
print(infos_villes.loc[:,"nb_hab_2012"].mean())
print(infos_villes.loc[infos_villes["alt_min"]>1500,["nb_hab_2012"]].mean())
print(infos_villes.sort_values(by=["dens"], ascending=False))



#2a : il y a 36700 lignes (rows)#
#2b : elle a sélectionnée dans un premier temps les villes ou l'altitiude minimale est supérieure à 1500 mètres avant qu'elle choisisse leurs noms#
#2c : Mont-Louis#
#2d : l'opération mean() fait la moyenne d'un domaine de valuers, ici l'altitude minimale#
#2e : 1751 hab environ#
#2f : oui#
#3a : Levalois perret#
