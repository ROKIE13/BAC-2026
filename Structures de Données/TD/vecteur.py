class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)
    def __str__(self):
        return "Nouveau Vecteur ("+ str(self.x) + ", " + str(self.y) + ")"
vector1 = Vecteur(2, 5)
vector2 = Vecteur(1, 3)
print(vector1+vector2)