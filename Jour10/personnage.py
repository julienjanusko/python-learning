import random

class Personnage:
    def __init__(self, nom, pv, attaque, intelligence, experience = 1, level = 1):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.intelligence = intelligence
        self.experience = experience
        self.maxpv = pv
        self.level = level

    def subir_degats(self, degats):
        self.pv -= degats
        if self.pv <= 0:
            self.pv = 0

    def attaquer(self, autre):
        autre.subir_degats(self.attaque)
        print(f"Attaque normale de {self.nom} !")

    def statut(self):
        print(f"#####     {self.nom}\n#####     Level : {self.level}\n#####     Atk : {self.attaque}\n#####     Int : {self.intelligence}\n#####     HP : {self.pv}/{self.maxpv}\n", end='')
    
    def recuperation(self):
        print(f"{self.nom} lance Récupération!")

    def est_vivant(self):
        return self.pv > 0
    
    def xp_pour_level_up(self):
        return 100 * (self.level ** 2)

    def update_exp(self, autre):
        self.experience += autre.experience
        while self.experience >= self.xp_pour_level_up():
            self.experience -= self.xp_pour_level_up()
            self.level_up()

    def level_up(self):
        self.maxpv += 10
        self.pv = self.maxpv
        self.attaque += 2
        self.intelligence += 2
        self.level += 1
        print(f"{self.nom} a augmenté d'1 niveau! [Lvl = {self.level}]. Stats mis à jour")

class Mage(Personnage):
    def __init__(self, nom, pv, attaque, intelligence, mana, level = 1, competence = "Boule de feu 🔥"):
        super().__init__(nom, pv, attaque, intelligence, level=level)
        self.manamax = mana
        self.mana = mana
        self.competence = competence
        self.classe = "Mage"

    def boule_de_feu(self, autre):
        if self.mana >= 40:
            autre.subir_degats(50)
            self.mana -= 40
            if self.mana < 0:
                self.mana = 0
            print(f"{self.nom} lance une boule de feu sur {autre.nom} !")
        else:
            print(f"{self.nom} lance une boule de feu... Mais annulée car pas assez de mana!")

    def recuperation(self):
        self.mana += 50
        if self.mana > self.manamax:
            self.mana = self.manamax
        print(f"{self.nom} a récupéré du mana! Mana = {self.mana}/{self.manamax}")

    def statut(self):
        super().statut()
        print(f"#####     Mana : {self.mana}/{self.manamax}")
        print(f"#####     Classe : Mage     #####")
    
    def competence_speciale(self, autre):
        self.boule_de_feu(autre)

    def level_up(self):
        super().level_up()
        self.intelligence += 3
        self.manamax += 10
        self.mana = self.manamax

class Guerrier(Personnage):
    def __init__(self, nom, pv, attaque, intelligence, armure, level = 1, competence = "Charge"):
        super().__init__(nom, pv, attaque, intelligence, level=level)
        self.armure = armure
        self.armuremax = armure
        self.competence = competence
        self.classe = "Guerrier"

    def recuperation(self):
        self.armure += 5
        if self.armure > self.armuremax:
            self.armure = self.armuremax
        print(f"{self.nom} lance Récupération")

    def subir_degats(self, degats):
        degats_pv = degats - (degats * self.armure / 100)
        self.pv -= round(degats_pv)
        self.armure -= round(degats - degats_pv) / 2
        if self.armure < 0:
            self.armure = 0

    def charge(self, autre):
        print(f"{self.nom} lance une charge puissante sur {autre.nom} !")
        autre.subir_degats(self.attaque+5)

    def statut(self):
        super().statut()
        print(f"#####     Armure : {self.armure}/{self.armuremax}")
        print(f"#####     Classe : Guerrier     #####")

    def competence_speciale(self, autre):
        self.charge(autre)

    def level_up(self):
        super().level_up()
        self.attaque += 3
        self.armuremax += 5
        self.armure = self.armuremax

class Ennemi(Personnage):
    def __init__(self, nom, pv, attaque, intelligence, level):
        super().__init__(nom, pv, attaque, intelligence, level = level)
        self.classe = "Ennemi"
        self.experience = level * 200

    def recuperation(self):
        self.pv += 5
        if self.pv > self.maxpv:
            self.pv = self.maxpv