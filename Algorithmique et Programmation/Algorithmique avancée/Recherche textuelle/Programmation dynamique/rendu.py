pieces = [50, 20, 10, 5, 2]

def rendu(somme_a_rendre, pieces):
    pieces_a_rendre = []
    for i in range(len(pieces)):
        while somme_a_rendre >= pieces[i]:
            pieces_a_rendre.append(pieces[i])
            somme_a_rendre -= pieces[i]
    return pieces_a_rendre

print(rendu(11, pieces))


def rendu_rec(somme, pieces, i=0):
    if somme == 0:
        return []
    if i >= len(pieces):
        return None
    if pieces[i] > somme:
        return rendu_rec(somme, pieces, i+1)
    else:
        resultat = rendu_rec(somme-pieces[i], pieces, i)
        if resultat is not None:
            return [pieces[i]] + resultat
        return None
print(rendu_rec(11, pieces))

def rendu_monnaie_rec(a_rendre, monnaies):
    if a_rendre == 0:
        return []
    resultat = [0]*(a_rendre*42)
    for i in range(len(monnaies)):
        if monnaies[i] <= a_rendre:
            if resultat[i] == 0:
                res=[monnaies[i]]+rendu_monnaie_rec(a_rendre-monnaies[i],monnaies)
                if len(res) < len(resultat):
                    resultat = res
    return resultat
print(rendu_monnaie_rec(11, pieces))