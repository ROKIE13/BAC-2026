def afficher(arbre, marge, profondeur):
    res = marge*profondeur*" " + str(arbre.racine) + "\n"
    if arbre.gauche is not None:
        res += afficher(arbre.gauche, marge, profondeur+1)
    if arbre.droite is not None:
        res += afficher(arbre.droite, marge, profondeur+1)
    return res


def parcours_mystere(arbre):
    if arbre is not None:
        print(arbre.racine)
        parcours_mystere(arbre.gauche)
        parcours_mystere(arbre.droite)
def parcours_suffixe(arbre):
    if arbre is not None:
        parcours_suffixe(arbre.gauche)
        parcours_suffixe(arbre.droite)
        print(arbre.racine)
def parcours_infixe(arbre):
    if arbre is not None:
        parcours_infixe(arbre.gauche)
        print(arbre.racine)
        parcours_infixe(arbre.droite)


def parcours_largeur(arbre):
    file_int = [arbre]
    file_finale = []
    while len(file_int) != 0:
        val = file_int.pop(0)
        file_finale.append(val.racine)
        if val.gauche is not None:
            file_int.append(val.gauche)
        if val.droite is not None:
            file_int.append(val.droite)
    return file_finale



    

                





class ArbreBinaire:
    def __init__(self, r, g, d):
        self.racine = r
        self.gauche = g
        self.droite = d
    def __str__(self):
        return afficher(self, 2, 1)
    def est_feuille(self):
        return self.gauche is None and self.droite is None
    def taille(self):
        nbTaille = 0
        if self.est_feuille():
            return 0
        if self.gauche is not None:
            nbTaille += 1 + self.gauche.taille()
        if self.droite is not None:
            nbTaille += 1 + self.droite.taille()
        return nbTaille
    def hauteur(self):
        if self.est_feuille():
            return 0
        prof_gauche = 0
        prof_droite = 0
        if self.gauche is not None:
            prof_gauche += 1 + self.gauche.hauteur()
        if self.droite is not None:
            prof_droite += 1 + self.droite.hauteur()
        return max(prof_droite, prof_gauche)
    def est_complet(self):
        if self.est_feuille():
            return True
        if self.gauche is None and self.droite is not None:
            return False
        if self.droite is not None:
            return self.gauche.est_complet() and self.droite.est_complet()
        else:
            return self.gauche.est_complet()
    def est_abr(self):
        if self.gauche.racine > self.racine or self.droite.racine < self.racine:
            return False
        elif self.gauche is None and self.droite is None:
            return True
        return self.gauche.est_abr() and self.droite.est_abr()


def recherche_cle(arbre, k):
    if arbre == None:
        return False
    if arbre.racine == k:
        return True
    if k < arbre.racine:
        return recherche_cle(arbre.gauche, k)
    else:
        return recherche_cle(arbre.droite, k)

def inserer_cle(arbre, k):
    if arbre.est_feuille():
        if k < arbre.racine:
            arbre.gauche = ArbreBinaire(k, None, None)
        else:
            arbre.droite = ArbreBinaire(k, None, None)
    else:
        if arbre.racine > k:
            if arbre.gauche is None:
                arbre.gauche = ArbreBinaire(k, None, None)
            else:
                inserer_cle(arbre.gauche, k)
        else:
            if arbre.droite is None:
                arbre.droite = ArbreBinaire(k, None, None)
            else:
                inserer_cle(arbre.droite, k)


        
arbre = ArbreBinaire(7,ArbreBinaire(5, ArbreBinaire(3, ArbreBinaire(1, None, None),
ArbreBinaire(4, None, None)),
ArbreBinaire(6, ArbreBinaire(4, None, None),
ArbreBinaire(6, None, None))),
ArbreBinaire(9, ArbreBinaire(8, ArbreBinaire(7, None, None),
ArbreBinaire(9, None, None)),
ArbreBinaire(15, None, None))) 

print(arbre)
print(arbre.est_feuille())
print(arbre.taille())
print(arbre.hauteur())     
print(arbre.est_complet())
parcours_infixe(arbre)
print(parcours_largeur(arbre))

maths = ArbreBinaire("3",ArbreBinaire('+', ArbreBinaire('4', ArbreBinaire('*', None, None),
ArbreBinaire('5', None, None)),
ArbreBinaire('/', ArbreBinaire('2', None, None),
ArbreBinaire('-', None, None))),
ArbreBinaire('6', ArbreBinaire('+', ArbreBinaire('4', None, None),
ArbreBinaire('*', None, None)),
ArbreBinaire('9', ArbreBinaire('+', None, None), ArbreBinaire("2", None, None))))

parcours_mystere(maths) #le resultat est de 141,5
print(inserer_cle(arbre, 20))


parcours_infixe(arbre)
