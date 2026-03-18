def fizzbuzz(n):
    liste = []
    for i in range(n):
        if ((i+1)%3 == 0) and ((i+1)%5 == 0):
            liste.append("FizzBuzz")
        elif (i+1)%3 == 0:
            liste.append("Fizz")
        elif (i+1)%5 == 0:
            liste.append("Buzz")
        else:
            liste.append(i+1)
    return liste

def frequence(mot):
    freq = {}
    for c in mot:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def inverser(liste):
    if not liste:
        return None
    new_liste = []
    for i in range(len(liste) - 1, -1, -1):
        new_liste.append(liste[i])
    return new_liste

def est_palindrome(mot):
    return list(mot) == inverser(list(mot))

def moyenne(liste):
    if not liste:
        return None
    nb = 0
    for i in liste:
        nb += i
    return nb / len(liste)

def notes_eleves(dico):
    if not dico:
        return None
    new_dico = {}
    for value in dico:
        new_dico[value] = moyenne(dico[value])
    return new_dico

def trier(liste):
    if not liste:
        return None
    for x in range(len(liste) - 1):
        for y in range(x + 1, len(liste)):
            if liste[x] > liste[y]:
                liste[x], liste[y] = liste[y], liste[x]
    return liste

def mot_le_plus_long(phrase):
    if not phrase:
        return None
    liste_phrase = phrase.split()
    mot = ""
    for x in liste_phrase:
        if len(x) > len(mot):
            mot = x
    return mot

print(fizzbuzz(15))
print(frequence("aba"))
print(est_palindrome("hello"))
print(notes_eleves({"Ali": [12, 15, 8], "Sara": [18, 14, 16]}))
print(trier([5, 2, 8, 1, 9]))
print(mot_le_plus_long("je suis un developpeur"))