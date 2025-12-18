def compteur(phrase, lettre):
    if len(phrase) == 0:
        return 0
    compt = 0
    if phrase[-1] == lettre:
        compt +=1
    return compt + compteur(phrase[:-1], lettre)

print(compteur("Bonjour tout le monde", 'u'))

