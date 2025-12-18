import random

class Piece:
    def alea(self):
        return random.randint(0, 1)

    def moyenne(self, n):
        tirage = []
        for i in range(n):
            tirage.append(self.alea())
        return sum(tirage)/n
p = Piece()
print(p.moyenne(100))