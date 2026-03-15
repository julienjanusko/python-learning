print("=== CARNET DE CONTACTS ===")
contacts = {}

while True:
    action = input("Action (ajouter/chercher/lister/supprimer/quitter) : ").strip().lower()
    if action == "ajouter":
        nom = input("Nom : ").strip().capitalize()
        numero = input("Numéro : ").strip()
        if not numero.isdigit():
            print("Mauvais numero (seulement des chiffres svp) !")
            continue
        contacts[nom] = numero
        print(f"✅ {nom} ajouté !")

    elif action == "supprimer":
        nom = input("Nom : ").strip().capitalize()
        if nom not in contacts:
            print("Ce nom n'existe pas !")
        else:
            contacts.pop(nom)
            print(f"❌ \"{nom}\" supprimé(e) !")

    elif action == "lister":
        for i, (nom, numero) in enumerate(contacts.items()):
            print(f"{i+1}) {nom} : {numero}")

    elif action == "chercher":
        nom = input("Nom : ").strip().capitalize()
        if nom not in contacts:
            print(f"⚠️ Contact \"{nom}\" non trouvé.")
        else:
            print(f"📞 {nom} : {contacts[nom]}")

    elif action == "quitter":
        del contacts
        print("👋 À plus !")
        break

    else:
        print("Commande inconnue !")



# === CARNET DE CONTACTS ===
# Action (ajouter/chercher/lister/supprimer/quitter) : ajouter
# Nom : Marie
# Numéro : 0612345678
# ✅ Marie ajouté !

# Action : chercher
# Nom : Marie
# 📞 Marie : 0612345678

# Action : lister
# 📒 Tous les contacts :
#  - Marie : 0612345678

# Action : chercher
# Nom : Paul
# ⚠️ Contact "Paul" non trouvé.

# Action : quitter
# 👋 À plus !