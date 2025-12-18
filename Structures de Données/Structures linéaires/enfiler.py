def enfile(liste, tup):
    
    for elt in tup:
        liste = [elt] + liste
    return liste

f = []
f = enfile(f, (1, 2))
f = enfile(f, (-42, 42))
print(f) 
print(f.pop())