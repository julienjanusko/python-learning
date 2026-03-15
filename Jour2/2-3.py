print("# === ANALYSE DE TEXTE ===")
phrase = input("Tape une phrase : ").strip()
words = phrase.split()

# Nombre de mots
nb_mots = len(words)
if not words:
    print("Pas de mot...")
else:    
    print(f"Mots : {nb_mots}")

    # Nombre de caracteres + mot le plus long
    nb_char = 0
    mot_le_plus_long = ""
    longueur_mot = 0

    for a in words:
        longueur_mot = len(a)
        nb_char += longueur_mot
        if longueur_mot > len(mot_le_plus_long):
            mot_le_plus_long = a
    print(f"Caractères (sans espaces) : {nb_char}")
    print(f"Mot le plus long : {mot_le_plus_long} ({len(mot_le_plus_long)} lettres)")
    # mot_le_plus_long = max(words, key=len) // donné par IA après avoir soumis exercice!
    # nb_char = len(phrase.replace(" ", ""))

    # Phrase en majuscule inversée
    print(f"Inversée : {phrase[::-1].upper()}")

    # Liste des mots qui font plus de 4 lettres
    five_plus_letters = [a for a in words if len(a)> 4]
    print(f"Mots de plus de 4 lettres : {five_plus_letters}")


# Exo 3 — Analyse de texte

# L'user tape une phrase. Ton programme affiche :

#     Nombre de mots
#     Nombre de caractères (sans espaces)
#     Le mot le plus long
#     La phrase en majuscules inversée
#     Liste des mots qui font plus de 4 lettres

# Utilise list comprehension pour le dernier point.

#
# OUTPUT ATTENDU
#

# === ANALYSE DE TEXTE ===
# Tape une phrase : Le développeur Python construit des applications

# 📊 Résultats :
# - Mots : 6
# - Caractères (sans espaces) : 42
# - Mot le plus long : "applications" (12 lettres)
# - Inversée : SNOITACILPPA SED TIURTSNOC NOHTYP RUEPPOLEVED EL
# - Mots de plus de 4 lettres : ['développeur', 'Python', 'construit', 'applications']