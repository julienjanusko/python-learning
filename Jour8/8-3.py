# Énoncé : Crée deux sous-classes de Personnage :

#     Guerrier → attribut bonus armure (int), quand il reçoit une attaque les dégâts sont réduits de self.armure
#     Mage → attribut bonus mana (int), nouvelle méthode boule_de_feu(autre) qui inflige 50 dégâts et coûte 20 mana (si pas assez de mana → print "Pas assez de mana !")

# Puis fais-les combattre !

# Output attendu :

# === TEST HÉRITAGE ===
# Gandalf lance une boule de feu sur Aragorn !
# → Aragorn : 75/120 PV
# Mana restant : 80

# Aragorn attaque Gandalf !
# → Gandalf : 60/80 PV

# Gandalf tente une boule de feu sans mana...
# Pas assez de mana !

# À toi ! 🔥

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

    def statut(self):
        if self.pv <= 0:
            self.pv = 0
        return f"→ {self.nom} : {self.pv}/{self.maxpv} PV"

    def est_vivant(self):
        return self.pv > 0
    
class Mage(Personnage):
    def __init__(self, nom, pv, attaque, mana):
        super().__init__(nom, pv, attaque)
        self.manamax = mana
        self.mana = mana

    def boule_de_feu(self, autre):
        if self.mana >= 20:
            print(f"{self.nom} lance une boule de feu sur {autre.nom} !")
            autre.subir_degats(50)
            self.mana -= 20
        else:
            print("Pas assez de mana...")

    def recuperation(self):
        self.mana += 10
        if self.mana > self.manamax:
            self.mana = self.manamax

class Guerrier(Personnage):
    def __init__(self, nom, pv, attaque, armure):
        super().__init__(nom, pv, attaque)
        self.maxpv = self.pv
        self.armure = armure
        self.armuremax = armure

    def recuperation(self):
        self.armure += 5
        if self.armure > self.armuremax:
            self.armure = self.armuremax

    def subir_degats(self, degats):
        degats_pv = degats - (degats * self.armure / 100)
        self.pv -= degats_pv
        self.armure -= (degats - degats_pv) / 2 

mage = Mage("Gandalf", 100, 5, 50)
guerrier = Guerrier("Conan", 100, 15, 40)

print("=== TEST HÉRITAGE ===")
while mage.est_vivant() and guerrier.est_vivant():
    mage.recuperation()
    guerrier.recuperation()

    mage.boule_de_feu(guerrier)
    print(guerrier.statut())
    if not guerrier.est_vivant():
        winner = mage.nom
        break

    guerrier.attaquer(mage)
    print(mage.statut())
    if not mage.est_vivant():
        winner = guerrier.nom
        break

    print()

print(f"🏆 {winner} remporte le combat !")