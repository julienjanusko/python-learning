# Exo 1 — Classe Personnage

# Énoncé : Crée une classe Personnage avec :

#     Attributs : nom, pv (points de vie), attaque
#     Méthode attaquer(autre) → réduit les pv de autre de self.attaque
#     Méthode est_vivant() → retourne True si pv > 0
#     Méthode statut() → retourne "{nom} : {pv} PV"

# Output attendu :

# hero = Personnage("Link", 100, 20)
# monstre = Personnage("Goblin", 50, 10)

# hero.attaquer(monstre)
# print(monstre.statut())    # → Goblin : 30 PV

# hero.attaquer(monstre)
# print(monstre.statut())    # → Goblin : 10 PV

# hero.attaquer(monstre)
# print(monstre.est_vivant()) # → False

class Personnage:
    def __init__(self, nom, pv, attaque):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque

    def attaquer(self, autre):
        autre.pv -= self.attaque 

    def statut(self):
        return f"→ {self.nom} : {self.pv} PV"

    def est_vivant(self):
        if self.pv > 0:
            return True
        return False

hero = Personnage("Link", 100, 20)
monstre = Personnage("Goblin", 50, 10)

hero.attaquer(monstre)
print(monstre.statut())    # → Goblin : 30 PV
print(monstre.est_vivant()) # → True

hero.attaquer(monstre)
print(monstre.statut())    # → Goblin : 10 PV

hero.attaquer(monstre)
print(monstre.est_vivant()) # → False