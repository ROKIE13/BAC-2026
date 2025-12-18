def puissance(n):
    if n > 0:
        return 2 * puissance(n-1)
    else:
        return 1

print(puissance(5))