# Énoncé

# Crée un programme qui permet de :

#     Ajouter un contact (nom + téléphone)
#     Rechercher un contact par nom
#     Afficher tous les contacts
#     Supprimer un contact

# Utilise un dictionnaire pour stocker les contacts.



# Output attendu

# === GESTIONNAIRE DE CONTACTS ===
# 1. Ajouter un contact
# 2. Rechercher un contact
# 3. Afficher tous les contacts
# 4. Supprimer un contact
# 5. Quitter

# Choix : 1
# Nom : Alice
# Téléphone : 0612345678
# ✅ Contact ajouté !

# Choix : 1
# Nom : Bob
# Téléphone : 0698765432
# ✅ Contact ajouté !

# Choix : 3
# 📋 Contacts :
#   Alice : 0612345678
#   Bob : 0698765432

# Choix : 2
# Rechercher : Alice
# 📞 Alice : 0612345678

# Choix : 2
# Rechercher : Charlie
# ❌ Contact non trouvé

# Choix : 4
# Supprimer : Bob
# ✅ Bob supprimé !

# Choix : 5
# 👋 À plus !

annuaire = {}

def ajouter_contact():
    nom = input("Nom : ").strip().capitalize()
    telephone = input("Telephone : ").strip()
    if telephone.isdigit():
        annuaire[nom] = telephone
        return True, "✅ Contact ajouté !"
    return False, "Numero de telephone non valide"

def rechercher_contact():
    nom = input("Rechercher : ").strip().capitalize()
    if nom in annuaire:
        return True, f"📞 {nom} : {annuaire[nom]}"
    return False, "❌ Contact non trouvé"

def afficher_contacts():
    if annuaire:
        print("📋 Contacts :")
        str_ret = ""
        for nom, tel in annuaire:
            str_ret += f"{nom} : {tel}\n"
        return True, str_ret
    else:
        return False, "❌ Pas de contact!"

def supprimer_contact():
    if not annuaire:
        return False, "❌ Pas de contact!"
    else:
        nom = input("Supprimer : ").strip().capitalize()
        if nom in annuaire:
            del annuaire[nom]
            return True, f"✅ {nom} supprimé !"
        return False, f"❌ {nom} non connu dans annuaire!"

def quitter():
    return -1, "👋 À plus !"

operations = {
    "1": ajouter_contact,
    "2": rechercher_contact,
    "3": afficher_contacts,
    "4": supprimer_contact,
    "5": quitter
}

print("# === GESTIONNAIRE DE CONTACTS ===")
while True:
    action = input("1. Ajouter un contact\n2. Rechercher un contact\n3. Afficher tous les contacts\n4. Supprimer un contact\n5. Quitter\n\nVotre choix : ")
    if action in operations:
        success, msg = operations[action]()
        print(msg)
        if success == -1:
            break
    else:
        print("Action non reconnue")
    print()