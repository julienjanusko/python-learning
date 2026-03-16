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
    return f"✅ \"{article}\" ajouté !"

def supprimer_course():
    article = input("Article : ").strip().capitalize()
    if article in liste_course:
        liste_course.remove(article)
        return f"✅ \"{article}\" supprimé !"
    return f"❌ \"{article}\" n'existe pas !"

def afficher_course():
    if not liste_course:
        return "📋 La liste est vide."
    lst = "📋 Ta liste :\n"
    for i, article in enumerate(liste_course):
        lst += f"{i+1}. {article}\n"
    return lst

def vider_course():
    if not liste_course:
        return "📋 La liste est déjà vide."
    liste_course.clear()
    return "🗑️ Liste vidée !"

operations = {
    "1" : ajouter_course,
    "2" : supprimer_course,
    "3" : afficher_course,
    "4" : vider_course
}

print("=== LISTE DE COURSES ===")
while True:
    action = input("1. Ajouter\n2. Supprimer\n3. Afficher\n4. Vider\n5. Quitter\n\nVotre choix : ").strip()
    if action == "5":
        print("👋 À plus !")
        break
    if action in operations:
        print(operations[action]())
    else:
        print("Commande inconnue")
    print()
