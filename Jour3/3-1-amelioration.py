def addition(nb1, nb2):
    return nb1 + nb2

def soustraction(nb1, nb2):
    return nb1 - nb2

def multiplication(nb1, nb2):
    return nb1 * nb2

def division(nb1, nb2):
    if nb2 == 0:
        print("⚠️ Division par zéro impossible !")
        return None
    return nb1 / nb2

operations = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division
}

print("=== CALCULATRICE ===")
while True:
    nombre_1 = input("Premier nombre : ").strip()
    if nombre_1 == "quit":
        print("👋 À plus !")
        break
    nombre_2 = input("Deuxieme nombre : ").strip()

    try:
        nombre_1 = float(nombre_1)
        nombre_2 = float(nombre_2)
    except ValueError:
        print("⚠️ Ce ne sont pas des nombres !")
        continue

    operation = input("Opération (+, -, *, /) : ")
    if operation in operations:
        func = operations[operation]
        resultat = func(nombre_1, nombre_2)
        if resultat is not None:
            print(f"✅ {nombre_1} {operation} {nombre_2} = {int(resultat) if resultat == int(resultat) else resultat}")  
    else:
        print("⚠️ Verifiez l'opérateur!")
    print()