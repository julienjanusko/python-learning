from personnage import Guerrier, Mage, Ennemi, Personnage
import random

ennemi_nom = ["Orc", "Elf maléfique", "Gobelin"]

def lvl_ennemi(niveau):
    niveau_ennemi = niveau - random.randint(0,3)
    if niveau_ennemi <= 0:
        return 1
    return niveau_ennemi

def combat(me):
    tour = 1
    # Nouvel ennemi
    ai_lvl = lvl_ennemi(me.level)
    ai = Ennemi(random.choice(ennemi_nom), random.randint(1, 2) * ai_lvl, random.randint(1, 5) * ai_lvl, random.randint(5, 10) * ai_lvl, ai_lvl)

    while True:
        print(f"--- Tour {tour} ---")
        while True:
            choix = input(f"Que fais-tu ?\n1. Attaque normale\n2. {me.competence}\n3. Récupération\n> ").strip()
            if choix in ["1", "2", "3"]:
                break
            print("Choix incorrect...")
            
        if choix == "1":
            me.attaquer(ai)
            ai.statut()
        elif choix == "2":
            me.competence_speciale(ai)
            ai.statut()
        elif choix == "3":
            me.recuperation()

        if not ai.est_vivant():
            combat_actif = 0
            break

        # Tour AI
        ai_choice = random.choice([1, 2])
        if ai_choice == 1:
            ai.attaquer(me)
            me.statut()
        elif ai_choice == 2:
            ai.recuperation()
            me.statut()

        if not me.est_vivant():
            break

        tour += 1
    me.update_exp(ai)
    return me