
while True:
    try:
        test = int(input("Un chiffre stp :"))
        break
    except ValueError:
        print("Ce n'est pas un chiffre")

while True:
    try:
        prenom = input("Ton prénom : ").strip()
        if not prenom:
            raise ValueError("Chaine vide!!!")
        break
    except ValueError as e:
        print(f"Erreur : {e}")
    except (KeyboardInterrupt, EOFError):
        print("Pas d'echappatoire")

age =  int(input("Ton âge : "))
ville = "Dijon"
is_majeur = False

if age >= 18:
    is_majeur = True



#Resume
print("=== PROFIL ===")
print(f"{prenom}, {age} ans, habite à {ville}.")
print(f"Statut : Majeur")
print(f"Dans 10 ans tu auras {age + 10} ans")