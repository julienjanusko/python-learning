# 📝 Exo 1 - Journal personnel

# Énoncé :
# Crée un programme de journal intime. L'utilisateur peut ajouter une entrée (avec la date auto) ou lire toutes les entrées. Les entrées sont sauvegardées dans un fichier journal.txt et persistent après fermeture du programme.

# Concepts : open(), mode "a" et "r", module datetime

#     Pour la date : from datetime import datetime puis datetime.now().strftime("%d/%m/%Y %H:%M")

# Output attendu :

# === 📔 MON JOURNAL ===
# 1. Écrire une entrée
# 2. Lire le journal
# 3. Quitter

# Choix : 1
# Votre texte : Aujourd'hui j'ai appris les fichiers en Python
# ✅ Entrée ajoutée !

# Choix : 2
# 📖 Mon journal :
# [25/05/2025 14:32] Aujourd'hui j'ai appris les fichiers en Python
# [25/05/2025 15:01] Je commence à kiffer Python

# Choix : 3
# 👋 À plus !

import os
from datetime import datetime

FICHIER_JOURNAL = "journal.txt"

def ecrire_texte():
    texte = input("Votre texte : ").strip().capitalize()
    date_heure = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(FICHIER_JOURNAL, "a") as f:
        f.write(f"[{date_heure}] {texte}\n")
    return "✅ Entrée ajoutée !"

def lire_journal():
    with open(FICHIER_JOURNAL, "r") as f:
        content = f.read()
    return content

operations = {
    "1" : ecrire_texte,
    "2" : lire_journal
}

print("=== 📔 MON JOURNAL ===")

if not os.path.exists(FICHIER_JOURNAL):
    print("Journal non trouvé... Création faite de journal.txt")
    with open(FICHIER_JOURNAL, "w") as f:
        f.write("")

while True:
    action = input("1. Écrire une entrée\n2. Lire le journal\n3. Quitter\n\nChoix : ").strip()
    if action == "3":
        print("👋 À plus !")
        break
    if action in operations:
        print(operations[action]())
    else:
        print("Commande non reconnue")
    print()