def calculer1(x, y):
    x = 878
    y = y+1
    print("x = " + str(x))
    print("y = " + str(y))
    return x


def calculer2(a, b):
    x = 33
    y = 44
    a = 2*x
    print("x = " + str(x))
    print("y = " + str(y))
    print("a = " + str(a))
    print("b = " + str(b))
    return b

x = 11
y = 22
print("x = " + str(x))
print("y = " + str(y))

a = calculer1(x,y)

print("Calcul 1 = " + str(a))
print("x = " + str(x))
print("y = " + str(y))
print("a = " + str(a))

b = calculer2(x,y)

print("Calcul 2 = " + str(b))
print("x = " + str(x))
print("y = " + str(y))
print("a = " + str(a))
print("b = " + str(b))


