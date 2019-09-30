import random 

class Ability:
    def __init__(self, name, mxdmg):
        '''
        Create Instance Variables:
        name:String
        max_damage: Integer
        '''
        self.name = name 
        self.mxdmg = mxdmg

        
    def attack(self):
        return random.randint(0, self.mxdmg)

class Armor:
    def __init__(self, name, maxx_block):
        self.name = name
        self.maxx_block = maxx_block

    def block(self):
        block = random.randint(0, self.maxx_block)
        return block
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.current_health: starting_health 
   
    def add_ability(self, ability):
        self.abilities.append(ability)
        

    def attack(self):
        for ability in self.abilities:
            return ability.attack()

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        for block in self.armors
        return block

    def 

    



if __name__ == "__main__":
    ability = Ability("Punch", 90)
    another_ability = Ability("Love", 100)
    hero = Hero("Black Panther", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    