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

print("=== CALCULATRICE ===")
accepted_operations = ["+", "-", "*", "/"]

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
    if operation in accepted_operations:
        if(operation == "+"):
            print(f"✅ {nombre_1} + {nombre_2} = {addition(nombre_1, nombre_2)}")
        elif(operation == "-"):
            print(f"✅ {nombre_1} - {nombre_2} = {soustraction(nombre_1, nombre_2)}")
        elif(operation == "*"):
            print(f"✅ {nombre_1} * {nombre_2} = {multiplication(nombre_1, nombre_2)}")            
        elif(operation == "/"):
            resultat = division(nombre_1, nombre_2)
            if resultat is not None:
                print(f"✅ {nombre_1} / {nombre_2} = {resultat}")
    else:
        print("⚠️ Verifiez vos input svp!")
    print()


# === CALCULATRICE ===
# Premier nombre : 10
# Deuxième nombre : 3
# Opération (+, -, *, /) : *
# ✅ 10.0 * 3.0 = 30.0

# Premier nombre : 8
# Deuxième nombre : 0
# Opération (+, -, *, /) : /
# ⚠️ Division par zéro impossible !

# Premier nombre : quit
# 👋 À plus !