def afficher (arbre, marge, profondeur):
    print(" " * marge + str(arbre[0]))
    if len(arbre) != 1:
        profondeur += 1
        afficher(arbre[1], marge + 1, profondeur)
        if len(arbre) ==3:
            afficher(arbre[2], marge + 1, profondeur)

afficher([10, [7, [5], [9, [8], [10]]], [15, [18, [17]]]], 0, 0)
afficher([7, [3, [9, [10], [13]], [2, [15], [17]]], [8, [1, [12], [14]], [5]]], 0, 0)
afficher(['A', ['B', ['E'], ['F']], ['C', ['G'], ['H']]], 0, 0)


