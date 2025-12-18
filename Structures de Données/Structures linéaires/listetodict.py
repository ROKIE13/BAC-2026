def list_to_dico(liste):
    dico = {}
    for i in range(0, len(liste), 2):
        dico[liste[i]] = liste[i + 1]
    return dico
print(list_to_dico(['A', 1, 'B', 2, 'C', 3]))