def solutions_possibles(score):
    if score < 0:
        resultat = []
    elif score == 0:
        resultat = [[0]]
    else:
        resultat = []
        for coup in [3, 5, 7]:
            liste = solutions_possibles(score - coup)
            for solution in liste:
                solution.append(coup + solution[len(solution)-1])
                resultat.append(solution)
    return resultat

print(solutions_possibles(11))