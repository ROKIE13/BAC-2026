class Carre:
    def __init__(self, cote ):
        self.cote = cote
    def perimetre(self):
        return self.cote * 4
        
    def aire(self):
        return self.cote ** 2

carreu = Carre(5)
print(carreu.perimetre())
print(carreu.aire()) 