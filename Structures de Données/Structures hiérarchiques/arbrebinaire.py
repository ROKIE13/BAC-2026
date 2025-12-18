def afficher (arbre, profondeur):
    chaine = " " * profondeur + str(arbre.racine) + "\n"
    if arbre.gauche is not None:
       chaine += afficher(arbre.gauche, profondeur + 2)
    if arbre.droite is not None:
       chaine += afficher(arbre.droite, profondeur + 2)
    return chaine 



class ArbreBinaire:
    def __init__(self, racine, gauche, droite):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite
    def __str__(self):
        return afficher(self, 0)


arbre1 = ArbreBinaire(10, ArbreBinaire(7, ArbreBinaire(5, None, None), ArbreBinaire(9, ArbreBinaire(8, None, None), ArbreBinaire(10, None, None))), ArbreBinaire(15, None, ArbreBinaire(18, ArbreBinaire(17, None, None), None)))
arbre2 = ArbreBinaire(7, ArbreBinaire(3, ArbreBinaire(9, ArbreBinaire(10, None, None), ArbreBinaire(13, None, None)), ArbreBinaire(2, ArbreBinaire(15, None, None), ArbreBinaire(17, None, None))), ArbreBinaire(8, ArbreBinaire(1, ArbreBinaire(12, None, None), ArbreBinaire(14, None, None)), ArbreBinaire(5, None, None)))
arbre3 = ArbreBinaire('A', ArbreBinaire('B', ArbreBinaire('E', None, None), ArbreBinaire('F', None, None)), ArbreBinaire('C', ArbreBinaire('G', None, None), ArbreBinaire('H', None, None)))
print(arbre1)
print(arbre2)
print(arbre3)