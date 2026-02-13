class GrapheListes:
    def __init__(self, oriente):
        self.liste = {}
        self.oriente = oriente
    def recherche_changer(self, sommet1, sommet2, val = 0):
        for elt in self.liste[sommet1]:
            if sommet2 == elt[0]:
                if val != 0:
                    elt[1] = val
                    return
                else:
                    return True
        return False
    def ajout_arete_arc(self, sommet1, sommet2, val = 1):
        if sommet1 not in self.liste:
            self.liste[sommet1] = [[sommet2, val]]
        else:
            if not self.recherche_changer(sommet1, sommet2):
                self.liste[sommet1].append([sommet2, val])
            else:
                self.recherche_changer(sommet1, sommet2, val)
        if not self.oriente:
            if sommet2 not in self.liste:
                self.liste[sommet2] = [[sommet1, val]]
            else:
                if not self.recherche_changer(sommet2, sommet1):
                    self.liste[sommet2].append([sommet1, val])
                else:
                    self.recherche_changer(sommet2, sommet1, val)
        else:
            if sommet2 not in self.liste:
                self.liste[sommet2] = []
        print(self.liste)
    def arete_ou_arc(self, sommet1, sommet2):
        return self.recherche_changer(sommet1, sommet2) and self.recherche_changer(sommet2, sommet1)
    def sommets(self):
        liste_sommets = []
        for elt in self.liste.keys():
            liste_sommets.append(elt)
        return liste_sommets
    def voisins(self, sommet):
        return self.liste[sommet]
Gp = GrapheListes(False)
Gp.ajout_arete_arc('A', 'B')
print(Gp.arete_ou_arc('A', 'B'))
print(Gp.sommets())
print(Gp.voisins('A'))
Gp.ajout_arete_arc('A', 'C', 12)
Gp.ajout_arete_arc('C', 'A' ,13)
print(Gp.arete_ou_arc('A', 'C'))
print(Gp.sommets())
print(Gp.voisins('A'))