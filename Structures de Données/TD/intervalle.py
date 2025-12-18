class Intervalle:
    def __init__ (self, valmin, valmax):
        self.valmin = valmin
        self.valmax = valmax
    def est_vide(self):
        if self.valmin> self.valmax:
            return True
        return False
    def __len__(self):
        return self.valmax - self.valmin
    def __contains__(self, x):
        return self.valmin <= x <= self.valmax
    def __eq__(self, other):
        return self.valmin == other.valmin and self.valmax == other.valmax
    def __le__(self, other):
        return self.valmin <= other.valmin <= self.valmax or self.valmin <= other.valmax <= self.valmax
    def intersection(self, other):
        if self.valmin <= other.valmin <= self.valmax:
            if other.valmax <= self.valmax:
                return self
            return Intervalle(other.valmin, self.valmax)
        elif self.valmin <= other.valmax <= self.valmax:
            if self.valmin <= other.valmin:
                return self
            return Intervalle(self.valmin, other.valmax)
    def union(self, other):
        if self.valmax < other.valmin:
            return self
        elif other.valmax < self.valmin:
            return other
        else:
            if other.valmax <= self.valmax:
                return Intervalle(other.valmin, self.valmax)
            elif self.valmax <= other.valmax:
                return Intervalle(self.valmin, other.valmax)
    def __str__(self):
        return ("intervalle : [" + str(self.valmin) + ", " + str(self.valmax) + "]")
    
mama = Intervalle(50, 200)
papa = Intervalle(33, 10)
bebe = Intervalle(2, 66)
print(mama.est_vide())
print(bebe.est_vide())
if mama.est_vide() == False and bebe.est_vide() == False:
    print(mama.valmax - mama.valmin)
    print(mama.valmin <= 75 <= mama.valmax)
    print(bebe.valmin <= 555 <= bebe.valmax)
    print(mama.valmin == bebe.valmin and mama.valmax == bebe.valmax)
    print(bebe.valmin <= mama.valmin <= bebe.valmax)
    print(mama.valmin <= bebe.valmax <= mama.valmax)
    print(mama.intersection(bebe))
    print(bebe.union(mama))