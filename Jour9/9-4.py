# Exo 4 — Boss 🔥 : Sauvegarde RPG

# Reprends tes classes Personnage, Mage, Guerrier de J8 et ajoute :

#     sauvegarder_personnage(personnage) → sauvegarde dans save.json
#     charger_personnage() → recharge le personnage depuis le fichier
#     Gère tous les cas d'erreur possibles

# p = Mage("Gandalf", 100, 30, 50)
# sauvegarder_personnage(p)
# → 💾 Gandalf sauvegardé !

# p2 = charger_personnage()
# p2.afficher()
# → 🧙 Gandalf | PV: 100 | ATK: 30 | Mana: 50

import random
import json

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


def charger_personnage():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)    
    except FileNotFoundError:
        data = {}
    except FileExistsError:
        data = {}
    except IOError as e:
        return False

    nom = list(data.keys())[0]
    pv = data[nom]["pv"]
    atk = data[nom]["atk"]
    if "mana" in data[nom]:
        mana = data[nom]["mana"]
        return Mage(nom, pv, atk, mana)
    else:
        armure = data[nom]["armure"]
        return Guerrier(nom, pv, atk, armure)

def sauvegarder_personnage(personnage):
    nom = personnage.nom
    pv = personnage.pv
    atk = personnage.attaque

    stats = {
        "pv" : pv,
        "atk" : atk
    }
    data = {
        nom : stats
    }

    if isinstance(personnage, Mage):
        data[nom]["mana"] = personnage.mana
    else:
        data[nom]["armure"] = personnage.armure

    try:
        with open("save.json", "w") as f:
            json.dump(data, f, indent=4)   
            print(f"→ 💾 {nom} sauvegardé !") 
    except FileNotFoundError:
        data = {}
    except FileExistsError:
        print("Erreur")
    except IOError as e:
        return False
    return

mage = Mage("Gandalf", 100, 10, 50)
sauvegarder_personnage(mage)

p2 = charger_personnage()
print(p2.statut())