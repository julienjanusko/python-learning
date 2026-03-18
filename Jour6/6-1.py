# Exo 1 — Crée une fonction carre(n) qui retourne n²

# Exo 2 — Crée une fonction est_pair(n) qui retourne True si pair, False sinon

# Exo 3 — Crée une fonction maximum(liste) qui retourne le plus grand élément (sans utiliser max())

# Exo 4 — Crée une fonction compter(mot, lettre) qui retourne combien de fois lettre apparaît dans mot

# Exo 5 — Crée une fonction inverser(liste) qui retourne la liste inversée (réutilise ce que t'as appris !)

# Exo 6 — Crée une fonction moyenne(liste) qui retourne la moyenne des nombres


def carre(n):
    return n*n

def est_pair(n):
    return n%2 == 0

def maximum(liste):
    if not liste:
        return None
    tmp = liste[0]
    for a in liste:
        if a > tmp:
            tmp = a
    return tmp

def compter(mot, lettre):
    if not mot:
        return None
    cpt = 0
    for c in mot:
        if c == lettre:
            cpt += 1
    return cpt

def inverser(liste):
    if not liste:
        return None
    new_liste = []
    for i in range(len(liste) - 1, -1, -1):
        new_liste.append(liste[i])
    return new_liste

def moyenne(liste):
    if not liste:
        return None

    nb = 0
    for i in liste:
        nb += i
    return nb / len(liste)

print(carre(2))
print(est_pair(3))
print(maximum([2,3,27,2,99,0]))
print(compter("Belle","l"))
print(inverser([2,3,4,1,0]))
print(moyenne([1,2,3,4,5,6]))
