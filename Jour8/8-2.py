# Exo 2 : Système de combat au tour par tour

# Reprends ta classe Personnage et crée un combat automatique :

#     Le héros et le monstre s'attaquent chacun leur tour
#     Le combat continue tant que les deux sont vivants
#     À chaque tour, affiche le statut des deux
#     À la fin, affiche le gagnant

# 💡 Indice : boucle while + ta méthode est_vivant()

class Personnage:
    def __init__(self, nom, pv, attaque):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.maxpv = pv

    def attaquer(self, autre):
        if autre.pv - self.attaque <= 0:
            autre.pv = 0
        else:
            autre.pv -= self.attaque 

    def statut(self):
        return f"→ {self.nom} : {self.pv}/{self.maxpv} PV"

    def est_vivant(self):
        return self.pv > 0


hero = Personnage("Héros", 100, 25)
monstre = Personnage("Goblin", 100, 10)

print("=== COMBAT ===")
winner = ""
tour = 1
while hero.est_vivant() and monstre.est_vivant():
    print(f"Tour {tour}")
    hero.attaquer(monstre)
    print(monstre.statut())
    if not monstre.est_vivant():
        winner = hero.nom
        break

    monstre.attaquer(hero)
    print(hero.statut())
    if not hero.est_vivant():
        winner = monstre.nom
        break

    print()
    tour += 1

print(f"🏆 {winner} remporte le combat !")

# === COMBAT ===
# Tour 1 :
# Héros attaque Goblin pour 25 dégâts !
# Goblin : 75/100 PV
# Goblin attaque Héros pour 10 dégâts !
# Héros : 90/100 PV

# Tour 2 :
# Héros attaque Goblin pour 25 dégâts !
# Goblin : 50/100 PV
# Goblin attaque Héros pour 10 dégâts !
# Héros : 80/100 PV

# Tour 3 :
# Héros attaque Goblin pour 25 dégâts !
# Goblin : 25/100 PV
# Goblin attaque Héros pour 10 dégâts !
# Héros : 70/100 PV

# Tour 4 :
# Héros attaque Goblin pour 25 dégâts !
# Goblin : 0/100 PV
# Goblin est mort !

# 🏆 Héros remporte le combat !