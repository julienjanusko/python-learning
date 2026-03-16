# Énoncé

# Crée un gestionnaire de liste de courses :

#     Ajouter un article
#     Supprimer un article
#     Afficher la liste (numérotée)
#     Vider la liste
#     Quitter

# Output attendu

# === LISTE DE COURSES ===

# 1. Ajouter
# 2. Supprimer
# 3. Afficher
# 4. Vider
# 5. Quitter

# Choix : 1
# Article : Pain
# ✅ "Pain" ajouté !

# Choix : 1
# Article : Lait
# ✅ "Lait" ajouté !

# Choix : 3
# 📋 Ta liste :
#   1. Pain
#   2. Lait

# Choix : 2
# Article à supprimer : Pain
# ✅ "Pain" supprimé !

# Choix : 3
# 📋 Ta liste :
#   1. Lait

# Choix : 4
# 🗑️ Liste vidée !

# Choix : 3
# 📋 La liste est vide.

# Choix : 5
# 👋 À plus !

liste_course = []

def ajouter_course():
    article = input("Article : ").strip().capitalize()
    liste_course.append(article)
    return True, f"✅ \"{article}\" ajouté !"

def supprimer_course():
    article = input("Article : ").strip().capitalize()
    if article in liste_course:
        liste_course.remove(article)
        return True, f"✅ \"{article}\" supprimé !"
    return False, f"✅ \"{article}\" n'existe pas !"

def afficher_course():
    if not liste_course:
        return False, "📋 La liste est vide."
    lst = "📋 Ta liste :\n"
    for i, article in enumerate(liste_course):
        lst += f"{i+1}. {article}\n"
    return True, lst

def vider_course():
    if not liste_course:
        return False, "📋 La liste est déjà vide."
    liste_course.clear()
    return True, "🗑️ Liste vidée !"

def quitter_course():
    return -1, "👋 À plus !"

operations = {
    "1" : ajouter_course,
    "2" : supprimer_course,
    "3" : afficher_course,
    "4" : vider_course,
    "5" : quitter_course
}

print("=== LISTE DE COURSES ===")
while True:
    action = input("1. Ajouter\n2. Supprimer\n3. Afficher\n4. Vider\n5. Quitter\n\nVotre choix : ").strip()
    if action in operations:
        is_success, msg = operations[action]()
        print(msg)
        if is_success == -1:
            break
    else:
        print("Commande inconnue")
    print()
