
# Crée une fonction valider_mdp(mdp) qui vérifie :

#     Au moins 8 caractères
#     Au moins 1 majuscule
#     Au moins 1 chiffre

# La fonction retourne True ou False + un message expliquant pourquoi c'est refusé.

# === VALIDATEUR DE MOT DE PASSE ===
# Mot de passe : abc
# ❌ Trop court (minimum 8 caractères)
# ❌ Pas de majuscule
# ❌ Pas de chiffre

# Mot de passe : abcdefgh
# ❌ Pas de majuscule
# ❌ Pas de chiffre

# Mot de passe : Abcdefg1
# ✅ Mot de passe valide !

# Mot de passe : quit
# 👋 À plus !

print("=== VALIDATEUR DE MOT DE PASSE ===")

def valider_mdp(mdp):
    message = ""
    taille_mdp = len(mdp)
    got_upper = any(c.isupper() for c in mdp)
    got_lower = any(c.islower() for c in mdp)
    got_digit = any(c.isdigit() for c in mdp)
    
    if taille_mdp < 8:
        score -= 1
        message += "❌ Trop court (minimum 8 caractères)\n"
    if not got_upper:
        score -= 1
        message += "❌ Pas de majuscule\n"
    if not got_lower:
        score -= 1
        message += "❌ Pas de minuscule\n"
    if not got_digit:
        score -= 1
        message += "❌ Pas de chiffre\n"     
    if message:
        return False, message
    return True, "✅ Mot de passe valide\n"

while True:
    mdp = input("Mot de passe : ").strip()
    if mdp == "quit":
        print("👋 À plus !")
        break
    is_valid, message = valider_mdp(mdp)
    print(message)