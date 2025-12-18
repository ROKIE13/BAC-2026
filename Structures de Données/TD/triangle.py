class Triangle:
    def __init__(self, cote1, cote2, hyp):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hyp = hyp
    def __lt__(self):
        if self.cote1 ** 2 + self.cote2 ** 2 == self.hyp ** 2:
            return True
        return False
    
triangoru = Triangle(7.2, 5.4, 9)
if triangoru.cote1 ** 2 + triangoru.cote2** 2 == triangoru.hyp ** 2:
    print("Le triangle est rectangle")
else:
    print("Le triangle n'est pas rectangle")