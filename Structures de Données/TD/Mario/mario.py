import random

class Mario:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
    def tomber(self, valeur):
        self.y = self.y - valeur
    def avancer(self):
        self.x = self.x + 2
        if random.randint(1, 5) == 1:
            self.tomber(1)
    def reculer(self):
        if self.x > 0:
            self.x = self.x - 1
            if random.randint(1, 20) == 1:
                self.x = self.x + 10
    def sauter(self):
        if self.y < 10:
            self.y += 1
            self.x +=1
            if random.randint(1, 10) == 1:
                self.tomber(5)
    def est_mort(self):
        return self.y <= 0
    def a_gagne(self):
        return self.x >= 42


mario = Mario(0, 6)
compteur = 0
avc = ["Avancer", "avancer", "AVANCER", "avance", "avancé", "a", "avc"]
rec = ["Reculer", "reculer", "RECULER", "recule", "reculé", "r", "rec"]
saut = ["Sauter", "sauter", "SAUTER", "saute", "sauté", "s", "saut"]
print("Bienvenue dans le jeu mario. Sur ce jet, tu pourras préciser si tu veux avancer, reculer ou sauter.")
print("Il faut que posx atteigne 42 pour gagner la partie. cependant, si posy atteint 0, alors Mario tombe dans la lave et la partie sera perdue")
comm_cons = {"avan" : 0, "sut" : 0, "recul" : 0}

while mario.est_mort() == False and mario.a_gagne() == False:
    activite = input("Quel action tu veux faire : ")
    if activite in avc:
        comm_cons["avan"] += 1
        comm_cons["sut"] = 0
        comm_cons["recul"] = 0
        if comm_cons["avan"] >= 3:
            print("Tu ne peux pas réaliser une même action plus de 3 fois d'affilée")
        else:
            mario.avancer()
    elif activite in rec:
        comm_cons["recul"] += 1
        comm_cons["sut"] = 0
        comm_cons["avan"] = 0
        if comm_cons["recul"] >= 3:
            print("Tu ne peux pas réaliser une même action plus de 3 fois d'affilée")
        else:
            mario.reculer()
    elif activite in saut:
        comm_cons["sut"] += 1
        comm_cons["avan"] = 0
        comm_cons["recul"] = 0
        if comm_cons["sut"] >= 3:
            print("Tu ne peux pas réaliser une même action plus de 3 fois d'affilée")
        else:
            mario.sauter()
    else:
        print("La commande n'existe pas")
    
    compteur += 1
    print("Nb tours : " + str(compteur) + ", posx : " + str(mario.x) + ", posy : " + str(mario.y))

    if mario.est_mort() == True:
        print("Mario est mort, partie perdue")
    elif mario.a_gagne() == True:
        print("Mario est arrivé au bout, partie gagnée")
    

        
            


    