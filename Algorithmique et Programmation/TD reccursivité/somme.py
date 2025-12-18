def somme(n, i): #cas où l'on veut uniquement une somme d'enties commencant d'un nb précis (3 au lieu de 1 par exemple comme nb de départ)
    if n > i:
        return 0
    else:
        return n + somme (n + 1, i)

a = somme(2, 7)
print(a)

def somme(n): #cas où on fait l'addition de tous les n entiers juqu'à une certaine longueur
    if n > 0:
        return n + somme(n-1)
    return 0
print(somme(7))