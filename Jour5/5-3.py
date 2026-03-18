# Exo 3 - Classement de joueurs V2 (avec sauvegarde)

# Énoncé :
# Reprends ton classement de joueurs du Jour 4 et ajoute la persistance ! Les joueurs sont sauvegardés dans classement.json. Ajoute aussi une fonction rechercher un joueur et modifier le score d'un joueur existant.

# Concepts : Tout ce qu'on a vu + refactoring d'un ancien code

# Output attendu :

# === 🏆 CLASSEMENT V2 ===
# 1. Ajouter joueur
# 2. Voir classement
# 3. Rechercher joueur
# 4. Modifier score
# 5. Supprimer joueur
# 6. Quitter

# Choix : 1
# Nom : Alice
# Score : 150
# ✅ Alice ajouté !

# Choix : 3
# Rechercher : Alice
# 🔍 Alice - 150 pts

# Choix : 4
# Nom : Alice
# Nouveau score : 200
# ✅ Score de Alice mis à jour !

# Choix : 2
# 🏆 Classement :
# 1. Alice - 200 pts

# Choix : 6
# 💾 Sauvegardé. À plus !

import json
import os

FICHIER_JSON = "classement.json"

def get_from_json():
    if os.path.getsize(FICHIER_JSON) <= 2:
        return []
    with open(FICHIER_JSON, "r") as f:
        return json.load(f)

def add_to_json(data):
    with open(FICHIER_JSON, "w") as f:
        json.dump(data, f, indent=4)

def ajouter_joueur():
    nom = input("Nom : ").strip()
    score = input("Score : ").strip()
    if score.isdigit():
        data = get_from_json()
        data.append({"nom": nom, "score": int(score)})
        add_to_json(data)
        return f"✅ {nom} ajouté!"
    return "Erreur dans la saisi du score"

def voir_classement():
    data = get_from_json()
    if not data:
        return "Classement vide!"
    data.sort(key=lambda x: x["score"], reverse=True)
    display = "🏆 Classement :\n"
    for i, joueur in enumerate(data):
        display += f"{i+1}. {joueur['nom']} - {joueur['score']} pts\n"
    return display

def supprimer_joueur():
    data = get_from_json()
    if not data:
        return "Classement vide!"
    nom = input("Nom : ").strip()
    for joueur in data:
        if joueur["nom"] == nom:
            data.remove(joueur)
            add_to_json(data)
            return f"✅ {nom} retiré!"
    return f"{nom} non trouvé!"

def rechercher_joueur():
    data = get_from_json()
    if not data:
        return "Classement vide!"
    nom = input("Nom : ").strip()
    for joueur in data:
        if joueur["nom"] == nom:
            return f"🔍 {nom} - {joueur['score']} pts"
    return f"{nom} non trouvé!"

def modifier_score():
    data = get_from_json()
    if not data:
        return "Classement vide!"
    nom = input("Nom : ").strip()
    score = input("Nouveau score : ").strip()

    try:
        score = int(score)
    except ValueError:
        return "Ce n'est pas un chiffre..."

    for joueur in data:
        if joueur["nom"] == nom:
            joueur["score"] = score
            add_to_json(data)
            return f"✅ Score de {nom} mis à jour !"
    return f"{nom} non trouvé!"

actions = {
    "1" : ajouter_joueur,
    "2" : voir_classement,
    "3" : rechercher_joueur,
    "4" : modifier_score,
    "5" : supprimer_joueur
}

if not os.path.exists(FICHIER_JSON):
    print("Fichier non présent... Création classement.json effectué!")
    with open(FICHIER_JSON, "w") as f:
        f.write("[]")

print("=== CLASSEMENT ===")
while True:
    action = input("1. Ajouter joueur\n2. Voir classement\n3. Rechercher joueur\n4. Modifier le score\n5. Supprimer joueur\n6. Quitter\n\nVotre choix: ").strip()
    if action == "6":
        print("👋 À plus !")
        break
    elif action not in actions:
        print("Commande inconnue!\n")
        continue
    print(actions[action]())
    print()