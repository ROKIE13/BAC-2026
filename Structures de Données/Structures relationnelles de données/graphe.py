G = {'A' : [('B', 1), ('C', 1), ('E', 1)], 'B' : [('A', 1), ('E', 1)], 'C' : [('A', 1), ('D', 1)], 'D' : [('C', 1)], 'E' : ['A', 'B']}

Gr = [[0, 9, 0, 15, 0, 0, 0, 0, 8]
, [9, 0, 13, 0, 0, 0, 38, 0, 6]
, [0, 13, 0, 14, 0, 21, 17, 0, 28]
, [15, 0, 14, 0, 10, 17, 0, 0, 5]
, [0, 0, 0, 10, 0, 19, 0, 0, 0]
, [0, 0, 21, 17, 19, 0, 5, 17, 0]
, [0, 38, 17, 0, 0, 5, 0, 16, 0]
, [0, 0, 0, 0, 0, 17, 16, 0, 0]
, [8, 6, 28, 5, 0, 0, 0, 0, 0]]

Gp = {'A' : [('B', 9), ('D', 15), ('I', 8)], 'B' : [('A', 9), ('C', 13), ('G', 38), ('I', 6)]}

class GrapheMatrice:
    def __init__(self, nb_sommets, oriente):
        self.matrice = []
        self.oriente = oriente
        for i in range(nb_sommets):
            liste_sommet = [0] * nb_sommets
            self.matrice.append(liste_sommet)
    def ajout_arete_arc(self, sommet1, sommet2, val = 1):
        self.matrice[sommet1][sommet2] = val
        if not self.oriente:
            self.matrice[sommet2][sommet1] = val
        print(self.matrice)
    def arete_ou_arc(self, sommet1, sommet2):
        return self.matrice[sommet1][sommet2] == self.matrice[sommet2][sommet1]
    def voisins(self, sommet):
        liste_voisins = []
        for i in range(len(self.matrice[sommet])):
            if self.matrice[sommet][i] != 0:
                liste_voisins.append(i)
        return liste_voisins

Gr = GrapheMatrice(9, False)
Gr.ajout_arete_arc(3, 1, 13)
print(Gr.arete_ou_arc(5, 2))
print(Gr.voisins(1))

class GrapheListes:
    def __init__(self, oriente):
        self.liste = {}
        self.oriente = oriente
    def ajout_arete_arc(self, sommet1, sommet2, val = 1):
        if sommet1 not in self.liste:
            self.liste[sommet1] = [(sommet2, val)]
        else:
            self.liste[sommet1].append((sommet2, val))
        if not self.oriente:
            if sommet2 not in self.liste:
                self.liste[sommet2] = [(sommet1, val)]
            else:
                self.liste[sommet2].append((sommet1, val))
        print(self.liste)
    def arete_ou_arc(self, sommet1, sommet2):
        print(self.liste[sommet1][0][0], self.liste[sommet2][0][0], sommet2, sommet1)
        return sommet2 == self.liste[sommet1][0][0] and sommet1 == self.liste[sommet1][0][0]
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

