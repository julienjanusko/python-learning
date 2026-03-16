# Énoncé

# Gère un classement de joueurs avec scores :

#     Ajouter un joueur (nom + score)
#     Afficher le classement trié par score (décroissant)
#     Supprimer un joueur
#     Quitter

# Indice : utilise une liste de listes → [["Alice", 150], ["Bob", 90]]
# Output attendu

# === CLASSEMENT ===

# 1. Ajouter joueur
# 2. Voir classement
# 3. Supprimer joueur
# 4. Quitter

# Choix : 1
# Nom : Alice
# Score : 150
# ✅ Alice ajouté(e) !

# Choix : 1
# Nom : Bob
# Score : 230
# ✅ Bob ajouté(e) !

# Choix : 1
# Nom : Charlie
# Score : 90
# ✅ Charlie ajouté(e) !

# Choix : 2
# 🏆 Classement :
#   1. Bob — 230 pts
#   2. Alice — 150 pts
#   3. Charlie — 90 pts

# Choix : 3
# Nom : Alice
# ✅ Alice supprimé(e) !

# Choix : 2
# 🏆 Classement :
#   1. Bob — 230 pts
#   2. Charlie — 90 pts

# Choix : 4
# 👋 À plus !

joueurs = []

def ajouter_joueur():
    nom = input("Nom : ").strip()
    score = input("Score : ").strip()
    if score.isdigit():
        joueurs.append([nom, int(score)])
        return f"✅ {nom} ajouté!"
    return "Erreur dans la saisi du score"

def voir_classement():
    if not joueurs:
        return "Pas de joueur dans le classement!"
    joueurs.sort(key=lambda x: x[1], reverse=True)
    display = "🏆 Classement :\n"
    for i, joueur in enumerate(joueurs):
        display += f"{i+1}. {joueur[0]} - {joueur[1]} pts\n"
    return display

def supprimer_joueur():
    if not joueurs:
        return "Classement vide!"
    nom = input("Nom : ").strip()
    for joueur in joueurs:
        if joueur[0] == nom:
            joueurs.remove(joueur)
            return f"✅ {nom} retiré!"
    return f"{nom} non trouvé!"

actions = {
    "1" : ajouter_joueur,
    "2" : voir_classement,
    "3" : supprimer_joueur
}

print("=== CLASSEMENT ===")

while True:
    action = input("1. Ajouter joueur\n2. Voir classement\n3. Supprimer joueur\n4. Quitter\n\nVotre choix: ").strip()
    if action == "4":
        print("👋 À plus !")
        break
    elif action not in actions:
        print("Commande inconnue!\n")
        continue
    print(actions[action]())
    print()