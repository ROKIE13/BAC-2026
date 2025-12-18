def longueur(n):
    if n <= 0:
        return 0
    else:
        compteur = 0
        if n % 2 == 1:
            compteur += 1
    return compteur + longueur(n // 2)


print(longueur(66))