import random

x = random.randint(1, 50)
i = 0

print("=== JEU DU DEVINEUR ===")
print("Je pense à un nombre entre 1 et 50...")


while True:
    try:
        nombre = int(input("Choisir un nombre : "))
    except ValueError:
        print("Ceci n'est pas un chiffre")
        continue
    except(EOFError, KeyboardInterrupt):
        print("Pas d'échappatoire")
        continue
    i += 1
    if nombre == x:
        print(f"Bien joué tu as trouvé en {i} essai(s) !")
        break
    elif nombre > x:
        print("Plus bas !")
    elif nombre < x:
        print("Plus haut !")
