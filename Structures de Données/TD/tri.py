class Mystere:
    def __init__(self):
        self.liste = []
    def add(self, x):
        if len(self.liste)==0 or x>=self.liste[len(self.liste)-1]:
            self.liste.append(x)
        elif x < self.liste[0]:
            self.liste = [x] + self.liste
        else:
            for i in range(len(self.liste)):
                if x>self.liste[i] and x<=self.liste[i+1]:
                    self.liste=self.liste[:i+1]+[x]+self.liste[i+1:]
                    break
l = Mystere()
for i in [78, 89, 10, 50, 7, 42]:
    l.add(i)
print(l.liste)