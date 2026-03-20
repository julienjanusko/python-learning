import json

JSON_FILE = "contacts.json"

def read_json(file):
    # Lecture
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est corrompu. Réinitialisation.")
        return {}
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")
        return False

def ajouter_contact(nom, tel):
    contact_data = {"nom" : nom, "tel" : tel}

    data = read_json(JSON_FILE)
    
    # Ajout
    data[nom] = tel

    # Ecriture
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")
        return False
    
def lire_contacts():
    
    data = read_json(JSON_FILE)
    if not data:
        print("Pas de contact")
        return
    
    for nom, tel in data.items():
        print(f"-> {nom} : {tel}")

def supprimer_contact(nom):

    data = read_json(JSON_FILE)
    if not data:
        print("Pas de contact")
        return 
    
    if nom in data:
        del data[nom]
    else:
        print(f"{nom} n'existe pas!")
        return
    
    # Ecriture
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")
        return False
    print(f"{nom} supprimé!")

ajouter_contact("Alice", "0612345678")
ajouter_contact("Bob", "0698765432")
lire_contacts()
supprimer_contact("Alice")
supprimer_contact("Luc")