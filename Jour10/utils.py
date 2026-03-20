from personnage import Personnage, Guerrier, Mage

def xp_pour_level_up(self):
    return 100 * (self.level ** 2)
    