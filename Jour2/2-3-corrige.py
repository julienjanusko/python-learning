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
    nb_char_total = len(phrase.replace(" ", ""))
    mot_le_plus_long = max(words, key=len)
    print(f"Caractères (sans espaces) : {nb_char_total}")
    print(f"Mot le plus long : {mot_le_plus_long} ({len(mot_le_plus_long)} lettres)")

    # Phrase en majuscule inversée
    print(f"Inversée : {phrase[::-1].upper()}")

    # Liste des mots qui font plus de 4 lettres
    five_plus_letters = [a for a in words if len(a)> 4]
    print(f"Mots de plus de 4 lettres : {five_plus_letters}")