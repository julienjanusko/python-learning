# Le joueur choisit sa classe (Mage ou Guerrier) et affronte un ennemi contrôlé par l'ordi (choix aléatoire).

# Chaque tour le joueur choisit une action :

#     Attaque normale
#     Compétence spéciale (boule de feu pour Mage, à toi d'inventer pour Guerrier)
#     Récupération

# L'ennemi joue aléatoirement une de ces 3 actions.

# Output attendu :

# === CHOIX DE CLASSE ===
# 1. Mage
# 2. Guerrier
# > 1

# Tu es Gandalf le Mage ! Ton ennemi : Conan le Guerrier

# === TOUR 1 ===
# Que fais-tu ?
# 1. Attaque normale
# 2. Boule de feu 🔥 (mana: 50)
# 3. Récupération
# > 2

# Gandalf lance une boule de feu sur Conan !
# → Conan : 70/100 PV

# Conan attaque Gandalf !
# → Gandalf : 85/100 PV

# === TOUR 2 ===
# ...

# 🏆 Gandalf remporte le combat !

import random

class Personnage:
    def __init__(self, nom, pv, attaque):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.maxpv = pv

    def subir_degats(self, degats):
        self.pv -= degats

    def attaquer(self, autre):
        autre.subir_degats(self.attaque)
        print(f"Attaque normale de {self.nom} !")

    def statut(self):
        if self.pv <= 0:
            self.pv = 0
        return f"→ {self.nom} : {self.pv}/{self.maxpv} PV"
    
    def recuperation(self):
        print(f"{self.nom} lance Récupération!")

    def est_vivant(self):
        return self.pv > 0


class Mage(Personnage):
    def __init__(self, nom, pv, attaque, mana, classe = "Mage", competence = "Boule de feu 🔥 (mana : 40)"):
        super().__init__(nom, pv, attaque)
        self.manamax = mana
        self.mana = mana
        self.classe = classe
        self.competence = competence

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
        self.mana += 10
        if self.mana > self.manamax:
            self.mana = self.manamax
        print(f"{self.nom} a récupéré du mana! Mana = {self.mana}/{self.manamax}")

    def statut(self):
        return(f"{self.nom} : HP = {self.pv}/{self.maxpv} // Mana = {self.mana}/{self.manamax}")
    
    def competence_speciale(self, autre):
        self.boule_de_feu(autre)


class Guerrier(Personnage):
    def __init__(self, nom, pv, attaque, armure, classe = "Guerrier", competence = "Charge"):
        super().__init__(nom, pv, attaque)
        self.maxpv = self.pv
        self.armure = armure
        self.armuremax = armure
        self.classe = classe
        self.competence = competence

    def recuperation(self):
        self.armure += 5
        if self.armure > self.armuremax:
            self.armure = self.armuremax
        print(f"{self.nom} lance Récupération")

    def subir_degats(self, degats):
        degats_pv = degats - (degats * self.armure / 100)
        self.pv -= round(degats_pv)
        self.armure -= round(degats - degats_pv) / 2

    def charge(self, autre):
        print(f"{self.nom} lance une charge puissante sur {autre.nom} !")
        autre.subir_degats(self.attaque+5)

    def statut(self):
        return(f"{self.nom} : [HP = {self.pv}/{self.maxpv} || Armure = {self.armure}/{self.armuremax}]")

    def competence_speciale(self, autre):
        self.charge(autre)


while True:
    classe = input("=== CHOIX DE CLASSE ===\n1. Mage\n2. Guerrier\n> ").strip()
    if classe == "1":
        me = Mage("Dumbledore", 100, 2, 100)
        ai = Guerrier("Hulk", 100, 15, 80)
        break
    elif classe == "2":
        me = Guerrier("Hulk", 100, 15, 80)
        ai = Mage("Dumbledore", 100, 2, 100)
        break
    else:
        print("Choix incorrect")

print(f"\nTu es {me.nom} le {me.classe} ! Ton ennemi : {ai.nom} le {ai.classe}")

cpt = 1
while True:
    print(f"=== TOUR {cpt} ===")
    # Tour humain
    while True:
        choix = input(f"Que fais-tu ?\n1. Attaque normale\n2. {me.competence}\n3. Récupération\n> ").strip()
        if choix in ["1", "2", "3"]:
            break
        print("Choix incorrect...")
        
    if choix == "1":
        me.attaquer(ai)
        print(ai.statut())
    elif choix == "2":
        me.competence_speciale(ai)
        print(ai.statut())
    elif choix == "3":
        me.recuperation()

    if not ai.est_vivant():
        winner = me.nom
        break

    # Tour AI
    ai_choice = random.choice([1, 2, 3])
    if ai_choice == 1:
        ai.attaquer(me)
        print(me.statut())
    elif ai_choice == 2:
        ai.competence_speciale(me)
        print(me.statut())
    elif ai_choice == 3:
        ai.recuperation()
        print(me.statut())

    if not me.est_vivant():
        winner = ai.nom
        break

    cpt += 1
    print()

print(f"🏆 {winner} remporte le combat !")