# Le projet : Un mini RPG jouable en console

#     Création de personnage — choix Mage ou Guerrier, nom, stats
#     Menu principal — Jouer, Charger, Sauvegarder, Quitter
#     Combat — contre des ennemis générés aléatoirement avec random
#     Système de niveaux — gagner de l'XP, monter de niveau, améliorer ses stats
#     Sauvegarde — ton système JSON du J9

from personnage import Guerrier, Mage
from stats import stats_guerrier, stats_mage
from sauvegarde import sauvegarder_personnage, charger_personnage
from combat import combat

VERSION = 0.1
STATS_BONUS = 10

def repartir_stats_bonus(points_max, unique_stat):
    points_restants = points_max
    bonus = {"atk": 0, "int": 0, "hp": 0, unique_stat: 0}
    while points_restants:
        print(f"Vous avez encore {points_restants} points à ajouter à vos statistiques de base")
        stat_id = input(f"1.ATK [{bonus["atk"]}]\n2.INT [{bonus["int"]}]\n3.HP [{bonus["hp"]}]\n4.{unique_stat.upper()} [{bonus[unique_stat]}]\n> ").strip()
        stat_point = input("Combien :\n> ").strip()
        try:
            stat_point = int(stat_point)
        except:
            print("Ce n'est pas un chiffre... Retour à l'assignation des stats bonus!")
            continue

        if stat_point < 0:
            stat_point = 0
            continue
        elif stat_point > points_restants:
            stat_point = points_restants
            
        if stat_id == "1":
            bonus["atk"] += stat_point
        elif stat_id == "2":
            bonus["int"] += stat_point
        elif stat_id == "3":
            bonus["hp"] += stat_point
        elif stat_id == "4":
            bonus[unique_stat] += stat_point
        else:
            print("Choix non existant...")
            continue
        points_restants -= stat_point
    return bonus

def creation_personnage():
    while True:
        choix = input("\nQuel personnage voulez vous créer?\n1. Guerrier\n2. Mage\n> ").strip()
        if choix == "1":
            # Guerrier
            unique_stat = "armor"
        elif choix == "2":
            # Mage
            unique_stat = "mana"
        else:
            print("Choix non reconnu...")
            continue

        # Initialisation perso + stats initiale
        nom_personnage = input("\nCréation personnage en cours...\nNom : ").strip()
        bonus = repartir_stats_bonus(STATS_BONUS, unique_stat)

        # Creation Personnage
        if choix == "1":
            me = Guerrier(nom_personnage, bonus["hp"]+stats_guerrier["hp"], bonus["atk"]+stats_guerrier["atk"], bonus["int"]+stats_guerrier["int"], bonus["armor"]+stats_guerrier["armor"])
        elif choix == "2":
            me = Mage(nom_personnage, bonus["hp"]+stats_mage["hp"], bonus["atk"]+stats_mage["atk"], bonus["int"]+stats_mage["int"], bonus["mana"]+stats_mage["mana"])
        return me


print(f"-------     Finql RPG {VERSION}     -------")
while True:
    menu = input("1. Nouvelle partie\n2. Charger partie\n3. Quitter\n> ").strip()
    if menu == "1":
        # Création personnage
        me = creation_personnage()
    elif menu == "2":
        # Chargement personnage
        me = charger_personnage()
        if me is None:
            continue
    elif menu == "3":
        # Quitter
        quit()
    else:
        print("Commande incorrect...")
        continue
    break       

while True:
    menu = input("=== MENU ===\n1. Combattre\n2. Voir stats\n3. Sauvegarder\n4. Quitter\n> ").strip()
    if menu == "1":
        # Combat
        me = combat(me)
    elif menu == "2":
        # Stats perso
        me.statut()
    elif menu == "3":
        # Sauvegarder personnage
        sauvegarder_personnage(me)
    elif menu == "4":
        # Quitter
        break
    else:
        print("Commande incorrect...")
        continue