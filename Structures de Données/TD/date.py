class Date:
    moisdan = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    def __str__(self):
        return str(self.jour) + " " + str(self.moisdan[self.mois - 1] + " " + str(self.annee))
    def __lt__(self, other):
        if self.annee < other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois < other.mois:
                return True
        elif self.mois == other.jour:
            if self.jour < other.jour:
                return True
        return False

date_du_jour1 = Date(int(input()), int(input()), int(input()))
print(date_du_jour1)
date_du_jour2 = Date(int(input()), int(input()), int(input()))
print(date_du_jour2)
print(date_du_jour1 < date_du_jour2)
