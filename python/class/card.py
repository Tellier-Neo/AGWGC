# Fichier permetant de définir la classe Card et ses attributs
# Chaque carte a des attributs comme le nom, le rang, le coût, la catégorie, les emplacements, les statistiques et la description

class Card:
    def __init__(self, name, rank, cost, category, slot1, slot2, hp, defense, spec, speed, description):
        self.name = name # Nom de la carte (ex: Delta force, Abrams, Su33, Systeme de défense aérien Mamba etc.)
        self.rank = rank # Rang de la carte (ex: 1, 2, 3, 4 ou 5)
        self.cost = cost # Coût de la carte (ex: 100, 200, 300 etc.)
        self.category = category # Catégorie de la carte (ex: infanterie, char, aérien, naval, support etc.)
        self.slot1 = slot1 # Emplacement d'arme ou de capacité 1 de la carte
        self.slot2 = slot2 # Emplacement d'arme ou de capacité 2 de la carte
        self.hp = hp # Points de vie de la carte
        self.defense = defense # Points de défense de la carte (reduction des dégâts reçus par une autre catégorie)
        self.spec = spec # Spécialisation de la carte (ex: anti-infanterie, anti-char, anti-aérien, brouillage etc.)
        self.speed = speed # Vitesse de la carte (nombre de case de déplacement ou distance d'attaque)
        self.description = description # Description de la carte

    def damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def information(self):
        info = f"Nom: {self.name}\n"
        info += f"Rang: {self.rank}\n"
        info += f"Coût: {self.cost}\n"
        info += f"Catégorie: {self.category}\n"
        info += f"Emplacement 1: {self.slot1}\n"
        info += f"Emplacement 2: {self.slot2}\n"
        info += f"Points de vie: {self.hp}\n"
        info += f"Points de défense: {self.defense}\n"
        info += f"Spécialisation: {self.spec}\n"
        info += f"Vitesse: {self.speed}\n"
        info += f"Description: {self.description}\n"
        return info
    