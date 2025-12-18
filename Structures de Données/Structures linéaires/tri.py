from time import perf_counter
from random import randint
def tri_selection(tab):
    for i in range(len(tab)-1):
        i_min = i
        for j in range(i+1, len(tab)):
            if tab[j]<tab[i_min]:
                i_min=j
        tab[i],tab[i_min]=tab[i_min],tab[i]
    return tab
def tri_insertion(tab):
    for i in range(1, len(tab)):
        val = tab[i]
        j = i-1
        while j>=0 and tab[j]>val:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = val
    return tab
def initialiser_tableau(n):
    tab = []
    for i in range(n):
        tab.append(randint(1,n))
    return tab


for i in range(7):
    taille = 10**(i+1)
    tab_selection = initialiser_tableau(taille)
    tab_insertion = initialiser_tableau(taille)
    tab_sorted = initialiser_tableau(taille)
    if i<4:
        debut_selection = perf_counter()
        tab_selection = tri_selection(tab_selection)
        fin_selection = perf_counter()
        print("Tri sélection taille " + str(taille) + " : " + str(fin_selection-debut_selection))
        debut_insertion = perf_counter()
        tab_insertion = tri_insertion(tab_insertion)
        fin_insertion = perf_counter()
        print("Tri insertion taille " + str(taille) + " : " + str(fin_insertion-debut_insertion))
    debut_sorted = perf_counter()
    tab_sorted_trie = sorted(tab_sorted)
    fin_sorted = perf_counter()
    print("Tri Python sorted taille " + str(taille) + " : " + str(fin_sorted-debut_sorted))
    print()