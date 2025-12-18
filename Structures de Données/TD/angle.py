from math import *

class Angle:
    def __init__(self, valeur):
        self.angle = valeur
    def __str__(self):
        return str(self.angle) + " degrés"
    def ajoute(self, other):
        self.angle += other.angle
        return str(self.angle) + " degrés"
    def cosinus(self):
        self.angle = self.angle * (pi/180)
        return cos(self.angle)
    def sinus(self):
        self.angle = self.angle * (pi/180)
        return sin(self.angle)
papa = Angle(60)
mama = Angle(75)
print(papa)
print(papa.ajoute(mama))
print(papa.cosinus())
print(papa.sinus())

