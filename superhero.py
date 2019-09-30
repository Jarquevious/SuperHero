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
        self.abilities: []
        self.armors: []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.current_health: starting_health 


if __name__ == "__main__":
    my_hero = Hero("Black Panther", 200)
    print(my_hero.name)
    print(my_hero.current_health)
