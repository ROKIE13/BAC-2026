def is_goodpar(expression):
    valeurs = []
    for elt in expression:
        print(elt)
        if elt == '(' or elt == '[':
            valeurs.append(elt)
        elif elt == ')':
            if valeurs == [] or valeurs.pop() != '(':
                return False
        elif elt == ']':
            if valeurs == [] or valeurs.pop() != '[' :
                return False
    return valeurs == []

print(is_goodpar('3+(5−7)*3]'))
             
    




