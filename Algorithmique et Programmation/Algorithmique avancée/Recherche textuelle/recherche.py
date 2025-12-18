def recherche_naive(text:str, motif:str) -> list:
    liste = []
    compteur = 0
    for i in range(len(text) - len(motif) + 1):
        j = 0
        while j != len(motif) and text[i+j] == motif[j]: #vérifier la condition d'arret avant de faire la vérification.
            j += 1
            compteur += 1
        compteur += 1
        if j == len(motif):
            liste.append(i)
            
        
    return liste, compteur

print(recherche_naive("CAGCGAGCGGCTGAGCAGCTGCTAGTCGGCTGATGCGGCTG", "CGGCTG"))
print(len("CAGCGAGCGGCTGAGCAGCTGCTAGTCGGCTGATGCGGCTG"))

def recherche_boyer_moore_horspool(text:str, motif:str) -> list:
    horspool = {'A' : len(motif), 'C' : len(motif), 'G' : len(motif), 'T' : len(motif)}

    for i in range(len(motif)-1):
        horspool[motif[i]] = len(motif) - i - 1
    print(horspool)
    compteur = 0
    nbCorres = []
    j = 0
    while j <= len(text) - len(motif) + 1:
        k = len(motif) -1
        while k > -1 and text[j+k] == motif[k]:
            k -= 1
            compteur +=1
        compteur += 1
        if k != -1:
            j += horspool[text[j + k]]
        else:
            nbCorres.append(j)
            j+=horspool[motif[0]]
    return nbCorres, compteur
def recherche_boyer_moore_amelioree(texte, motif):
    m = len(motif)
    horspool = []
    for i in range(m):
        horspool.append({'A': i+1, 'T': i+1, 'C': i+1, 'G': i+1})
        for j in range(i):
            horspool[i][motif[j]] = i-j
    print(horspool)
    res = []
    nb_tests = 0
    decalage = 0
    while decalage < len(texte)-m+1:
        j = m-1
        nb_tests += 1
        while j >= 0 and texte[decalage+j]==motif[j]:
            nb_tests += 1
            j -= 1
        if j < 0:
            res.append(decalage)
            decalage += horspool[-1][texte[decalage+m-1]]
        else:
            decalage += max(horspool[-1][texte[decalage+m-1]], horspool[j][texte[decalage+j]]) #aligner le max entre la derniere valeur comparee et la valeur suivante
    return res, nb_tests
print(recherche_boyer_moore_amelioree("CAGCGAGCGGCTGAGCAGCTGCTAGTCGGCTGATGCGGCTG", "CGGCTG"))
            


print(recherche_boyer_moore_horspool("CAGCGAGCGGCTGAGCAGCTGCTAGTCGGCTGATGCGGCTG", "CGGCTG"))
