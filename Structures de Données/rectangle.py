class Rectangle:
    nb_angle_droits = 4 # attribut de classe : cette ligne s applique a tt les variables de cette classe
    def __init__(self, longueur, largeur): 
        self.longueur = longueur #on fait une encapsulation
        self.largeur = largeur
        #ici on definit des valeurs à une variable concernée : c'est un attribut != attribut de classe ou elle s applique a tt le monde#
    
    def calculer_aire(self): # ca c une methode
        return self.longueur*self.largeur


rectangle1 = Rectangle(6, 4)
print(rectangle1.longueur)
print(rectangle1.largeur)
print(rectangle1.calculer_aire())
rectangle1.longueur = 10
print(rectangle1.longueur)
print(type(rectangle1))
print(rectangle1)

rectangle2 = Rectangle(5,2)
print(rectangle2.longueur)
print(rectangle2.largeur)
print(rectangle2.calculer_aire())
print(rectangle1.nb_angle_droits)
print(rectangle2.nb_angle_droits)


#la methode __str__ a pour azffichage l emplacement sur la ram de la variable, on peut la redefinir pr qu elle affiche autre chose-