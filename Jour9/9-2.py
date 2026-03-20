# sauvegarder("notes.txt", "Python c'est cool")
# lire("notes.txt")     → "Python c'est cool"
# lire("nope.txt")      → "Erreur : fichier introuvable !"

def sauvegarder(fichier, texte):
    with open(fichier, "w") as f:
        f.write(texte)

def lire(fichier):
    try:
        with open(fichier, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")

sauvegarder("notes.txt", "Python c'est cool")
lire("notes.txt")
lire("nope.txt")