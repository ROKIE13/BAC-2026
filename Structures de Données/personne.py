class Personne:
    def __init__(self, naissance, taille, poids):
        self.naissance = naissance
        self.taille = taille
        self.poids = poids
    def grandir(self, h):
        self.taille += h
luc = Personne(2005, 178, 69)
taille_initiale = luc.taille
luc.grandir(8)
nouvelle_taille = luc.taille
print("Luc p`ese " + str(luc.poids) + "kg.")
print("Luc mesure maintenant " + str(nouvelle_taille) + "cm apr`es avoir grandi" +
" de 8cm en 1 an. Avant ¸ca, il mesurait : " + str(taille_initiale) + "cm.")
print(luc)