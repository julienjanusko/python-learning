# L'utilisateur entre des nombres un par un (tape stop pour finir).
# Ensuite affiche :

#     La liste des nombres
#     Le total
#     La moyenne
#     Le min et le max
#     La liste triée

######## Output attendu #######
# === STATISTIQUES ===

# Nombre : 15
# Nombre : 8
# Nombre : 23
# Nombre : 4
# Nombre : 12
# Nombre : stop

# 📊 Résultats :
# Nombres : [15, 8, 23, 4, 12]
# Total   : 62
# Moyenne : 12.4
# Min     : 4
# Max     : 23
# Trié    : [4, 8, 12, 15, 23]

numbers = []

while True:
    action = input("Nombre : ").strip()
    if action == "stop":
        break
    else:
        try:
            action = int(action)
        except ValueError:
            print("⚠️ Ce n'est pas un nombre !")
            continue
        numbers.append(action)

print("📊 Résultats :")
if not numbers:
    print("Pas de nombre saisi!")
else:
    print(f"Nombres : {numbers}")
    total = sum(numbers)
    print(f"Total : {total}")
    print(f"Moyenne : {total/len(numbers)}")
    print(f"Min : {min(numbers)}")
    print(f"Max : {max(numbers)}")
    numbers.sort()
    print(f"Trié : {numbers}")