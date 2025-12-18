def longueur(n):
    if n <= 0:
        return 0
    else:
        return 1 + longueur(n // 10)

print(longueur(1202222))