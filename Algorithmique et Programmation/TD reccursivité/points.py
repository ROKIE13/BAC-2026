def numero_castor(x, y):
    if x == 0 and y == 0:
        return 0
    if y ==0:
        return 1 + numero_castor(0, x-1)
    else:
        return 1 + numero_castor(x+1, y-1)

print(numero_castor(2, 2))