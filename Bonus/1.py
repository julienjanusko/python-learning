# Entrée : [1, 2, 3, 4, 5]
# Sortie : [5, 4, 3, 2, 1]

# Exo 1
liste = [1, 2, 3, 4, 5]
inverse = []

for i in range(len(liste) - 1, -1, -1):
    inverse.append(liste[i])
print(inverse)

# Exo 2
liste = [1, 3, 3, 5, 5, 5, 7]
new_liste = []
for a in liste:
    if a not in new_liste:
        new_liste.append(a)
liste = new_liste
print(liste)

# Exo 3
liste = [10, 45, 23, 78, 5, 78]
liste.sort(reverse=True)

new_liste = []
for a in liste:
    if a not in new_liste:
        new_liste.append(a)
liste = new_liste

print(liste[1])

# Exo 4
mot = "banana"
compteur = {}
for char in mot:
    if char in compteur:
        compteur[char] += 1
    else:
        compteur[char] = 1
print(compteur)

# Exo 5
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
c = {}

for value in a:
    if value in b:
        c[value] = a[value] + b[value]
    else:
        c[value] = a[value]

for value in b:
    if value not in c:
        c[value] = b[value]

print(c)

# Exo 6
compteur = {"a": 1, "b": 2, "c": 3}
new_dict = {}
# value = a, dict[value] = 1, temp = 1
for value in compteur:
    temp = compteur[value]
    new_dict[temp] = value

print(new_dict)

# Exo 7
personnes = [
    {"nom": "Ali", "age": 25},
    {"nom": "Sara", "age": 30},
    {"nom": "Tom", "age": 25},
    {"nom": "Léa", "age": 30},
]

resultat = {}

for personne in personnes:
    age = personne["age"]
    nom = personne["nom"]
    if age in resultat:
        resultat[age].append(nom)
    else:
        resultat[age] = [nom]

print(resultat)