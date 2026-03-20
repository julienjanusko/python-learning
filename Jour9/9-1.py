# diviser(10, 2)   → 5.0
# diviser(10, 0)   → "Erreur : division par zéro !"
# diviser("a", 2)  → "Erreur : types invalides !"

def diviser(x, y):
    try:
        print(f"{int(x)/int(y)}")
    except ValueError:
        print("Ce n'est pas un nombre")
    except ZeroDivisionError:
        print("Division par 0")

diviser(10,2)
diviser(10,0)
diviser("a",2)