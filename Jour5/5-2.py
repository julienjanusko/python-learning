# Exo 2 - Gestionnaire de tâches persistant

# Énoncé :
# Crée un gestionnaire de tâches (todo list). L'utilisateur peut ajouter, voir, supprimer et marquer comme faite une tâche. Tout est sauvegardé dans un fichier taches.json. Quand on relance le programme, les tâches sont toujours là.

# Concepts : json.dump(), json.load(), os.path.exists()

# Output attendu :

# === ✅ TODO LIST ===
# 1. Ajouter une tâche
# 2. Voir les tâches
# 3. Terminer une tâche
# 4. Supprimer une tâche
# 5. Quitter

# Choix : 1
# Tâche : Faire les courses
# ✅ Tâche ajoutée !

# Choix : 1
# Tâche : Apprendre Python
# ✅ Tâche ajoutée !

# Choix : 2
# 📋 Mes tâches :
# 1. [ ] Faire les courses
# 2. [ ] Apprendre Python

# Choix : 3
# Numéro : 2
# ✅ "Apprendre Python" terminée !

# Choix : 2
# 📋 Mes tâches :
# 1. [ ] Faire les courses
# 2. [✓] Apprendre Python

# Choix : 4
# Numéro : 1
# 🗑️ "Faire les courses" supprimée !

# Choix : 5
# 💾 Sauvegardé. À plus !

import os
import json

FICHIER_TODO = "taches.json"

def charger_taches():
    if os.path.getsize(FICHIER_TODO) <= 2:
        return []
    with open(FICHIER_TODO, "r") as f:
        return json.load(f)

def sauvegarder_taches(data):
    with open(FICHIER_TODO, "w") as f:
        json.dump(data, f, indent=4)    

def ajouter_tache():
    tache = input("Tâche : ").strip().capitalize()

    #On vérifie d'abord qu'il y a du contenu dans le fichier taches.json
    data = charger_taches()
    data.append({"tache": tache, "complete": False})
    sauvegarder_taches(data)
    return "✅ Tâche ajoutée !"

def voir_taches():
    data = charger_taches()
    if not data:
        return "Pas de tache en cours!"
    ret = ""
    for i, t in enumerate(data):
        checked = " "
        if t["complete"]:
            checked = "✓"
        ret += f"{i+1}. [{checked}] {t['tache']}\n"
    return ret

def terminer_tache():
    liste_taches = charger_taches()
    if not liste_taches:
        return "Pas de tache en cours!"

    numero_tache = input("Numéro : ").strip()

    try:
        numero_tache = int(numero_tache)
    except ValueError:
        return "Tache saisie non valide"

    if numero_tache > len(liste_taches) or numero_tache <= 0:
        return "Erreur dans la saisie du numero de tache..."

    if liste_taches[numero_tache - 1]["complete"]:
        return f'{liste_taches[numero_tache - 1]["tache"]} déjà terminée !'

    liste_taches[numero_tache - 1]["complete"] = True

    sauvegarder_taches(liste_taches)

    return f'✅ {liste_taches[numero_tache - 1]["tache"]} terminée !'

def supprimer_tache():
    liste_taches = charger_taches()
    if not liste_taches:
        return "Pas de tache en cours!"

    numero_tache = input("Numéro : ").strip()

    try:
        numero_tache = int(numero_tache)
    except ValueError:
        return "Tache saisie non valide"

    if numero_tache > len(liste_taches) or numero_tache <= 0:
        return "Erreur dans la saisie du numero de tache..."

    ret = f'✅ {liste_taches[numero_tache - 1]["tache"]} supprimée !'

    del liste_taches[numero_tache - 1]

    sauvegarder_taches(liste_taches)

    return ret

operators = {
    "1" : ajouter_tache,
    "2" : voir_taches,
    "3" : terminer_tache,
    "4" : supprimer_tache
}

if not os.path.exists(FICHIER_TODO):
    print("To Do liste non trouvée. Création faite!")
    with open(FICHIER_TODO, "w") as f:
        f.write("")

print("=== ✅ TODO LIST ===")
while True:
    action = input("1. Ajouter une tâche\n2. Voir les tâches\n3. Terminer une tâche\n4. Supprimer une tâche\n5. Quitter\n\nChoix : ").strip()
    if action == "5":
        print("💾 Sauvegardé. À plus !")
        break
    if action in operators:
        print(operators[action]())
    else:
        print("Commande inconnue!")
    print()