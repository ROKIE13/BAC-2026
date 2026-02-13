from random import randint

class GrapheListes:
    def __init__(self, oriente):
        self.listes = {}
        self.oriente = oriente
    def ajout_arete_arc(self, s1, s2):
        if s1 in self.listes.keys():
            self.listes[s1].append(s2)
        else:
            self.listes[s1] = [s2]
        if not self.oriente:
            if s2 in self.listes.keys():
                self.listes[s2].append(s1)
            else:
                self.listes[s2] = [s1]
        elif s2 not in self.sommets():
            self.listes[s2] = []
    def arete_ou_arc(self, s1, s2):
        if s1 in self.listes.keys():
            return s2 in self.listes[s1]
        return False
    def sommets(self):
        return list(self.listes.keys())
    def voisins(self, s):
        if s in self.listes.keys():
            return self.listes[s]
        return []
france = GrapheListes(False)
for region in ["IDF", "Normandie", "PdL", "NA", "ARA", "BFC"]:
    france.ajout_arete_arc("CVL", region)
for region in ["HDF", "Normandie", "GE", "BFC"]:
    france.ajout_arete_arc("IDF", region)
for region in ["BFC", "NA", "Occitanie", "PACA"]:
    france.ajout_arete_arc("ARA", region)
france.ajout_arete_arc("HDF", "GE")
france.ajout_arete_arc("Normandie", "Bretagne")
france.ajout_arete_arc("Normandie", "HDF")
france.ajout_arete_arc("Bretagne", "PdL")
france.ajout_arete_arc("NA", "PdL")
france.ajout_arete_arc("NA", "Occitanie")
france.ajout_arete_arc("GE", "BFC")
france.ajout_arete_arc("GE", "HDF")
france.ajout_arete_arc("PACA", "Corse")
france.ajout_arete_arc("PACA", "Occitanie")
for outre_mer in ["LR", "Mayotte", "Guyane", "Martinique", "Guadeloupe"]:
    france.listes[outre_mer] = []
print(france.listes["PACA"] != [])
print(france.listes["PACA"])

def parcours_profondeur_recursif(graphe, liste, sommet):
    for elt in graphe.voisins(sommet):
        if elt not in liste:
            liste.append(elt)
            parcours_profondeur_recursif(graphe, liste, elt)
    return liste

print(parcours_profondeur_recursif(france, [], "CVL"))
print

def parcours_profondeur_iteratif(graphe, liste, sommet):
    pile = [sommet]
    while pile:
        elt = pile.pop()
        if elt not in liste:
            liste.append(elt)
            for reg in graphe.voisins(elt):
                pile.append(reg)
            
    return liste

print(parcours_profondeur_iteratif(france, [], "CVL"))

def existe_chaine_chemin(g, s1, s2):
    liste = parcours_profondeur_recursif(g, [], s1)
    if s2 not in liste:
        return False
    return True

print(existe_chaine_chemin(france, "PACA", "Normandie"))
print(existe_chaine_chemin(france, "PACA", "Guyane"))

parcours = {elt : 1 for elt in france.listes.keys()}
def parcours_cycle(g, parcours_termine, s):
    if parcours_termine[s] == 2:
        return True
    elif parcours_termine[s] == 3:
        return False
    parcours_termine[s] = 2
    liste = []
    for elt in g.voisins(s):
        if parcours_cycle(g, parcours_termine, elt):
            return True
    parcours_termine[s] = 3
    return False
print(parcours_cycle(france, parcours, "PACA"))
print(parcours_cycle(france, parcours, "Occitanie"))
print(parcours_cycle(france, parcours, "Guyane"))
    
def cycle(g):
    parcours = {elt : 1 for elt in g.listes.keys()}
    for elt in parcours.keys():
        if parcours_cycle(g, parcours, elt):
            return True
    return False

print(cycle(france))
gg = GrapheListes(False)
gg.ajout_arete_arc("LL", "MM")
gg.ajout_arete_arc("MM", "PSG")
print(gg.listes)
print(cycle(gg))

def distances(g, s):
    dist = {s: (0, s)}
    file = [s]
    while file:
        elt = file.pop(0)  
        for nb in g.voisins(elt):
            if nb not in dist:          
                dist[nb] = (dist[elt][0] + 1, elt)
                file.append(nb)               
    return dist


print(distances(france, "CVL"))
def distance(g, s1, s2):
    dist = distances(g, s1)
    return dist[s2]
print(distance(france, "PACA", "HDF"))



def plus_court_chemin(g, s1, s2):
    if not(s2 in g.listes and s1 in g.listes):
        return []
    chemin = distance(g, s1, s2)
    print(chemin)
    liste = [s2]
    if chemin[1] != s1:
        liste = plus_court_chemin(g, s1, chemin[1]) + liste
    if s1 not in liste: 
        return [s1] + liste
    return liste

print(plus_court_chemin(france, "NA", "Occitanie"))