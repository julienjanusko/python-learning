import json
from personnage import Mage, Guerrier

SAVE_FILE = "rpg_save.json"

def charger_personnage():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)    
    except FileNotFoundError:
        data = {}
    except FileExistsError:
        data = {}
    except IOError as e:
        return None
    
    if not data:
        return None
    
    if(data["classe"] == "Mage"):
        perso = Mage(data["nom"], data["pv"], data["attaque"], data["intelligence"], data["mana"], data["level"], data["competence"])
        perso.manamax = data["manamax"]
    elif(data["classe"] == "Guerrier"):
        perso = Guerrier(data["nom"], data["pv"], data["attaque"], data["intelligence"], data["armure"], data["level"], data["competence"])
        perso.armuremax = data["armuremax"]
    perso.maxpv = data["pvmax"]
    perso.experience = data["experience"]

    return perso
    

def sauvegarder_personnage(personnage):
    nom = personnage.nom
    pv = personnage.pv
    pvmax = personnage.maxpv
    attaque = personnage.attaque
    intelligence = personnage.intelligence
    level = personnage.level
    competence = personnage.competence
    classe = personnage.classe
    experience = personnage.experience


    data = {
        "nom" : nom,
        "pv" : pv,
        "pvmax" : pvmax,
        "attaque" : attaque,
        "intelligence" : intelligence,
        "experience" : experience,
        "level" : level,
        "competence" : competence,
        "classe" : classe     
    }

    if isinstance(personnage, Mage):
        data["mana"] = personnage.mana
        data["manamax"] = personnage.manamax
    else:
        data["armure"] = personnage.armure
        data["armuremax"] = personnage.armuremax
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)   
            print(f"→ 💾 {nom} sauvegardé !") 
    except FileNotFoundError:
        print("Erreur : impossible de sauvegarder")
    except FileExistsError:
        print("Erreur")
    except IOError as e:
        return False
    return