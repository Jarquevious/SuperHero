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
        attack_total = 0
        for ability in self.abilities:
            attack_total =+ ability.attack()
        return attack_total 

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        defend_total = 0 
        for armor in self.armors: 
             defend_total += armor.block() 
        return defend_total

    def take_damage(self, damage): 
        self.current_health -= damage

    def is_alive(self):
        if self.current_health <=0:
            return False
        else: 
            return True 

    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(self.attack())
            #print(opponent.take_damage(self.attack()))
            self.take_damage(opponent.attack())
            #print(self.take_damage(opponent.attack()))

            if self.is_alive() == True and opponent.is_alive() == True:
                print("DRAW!!!")

            else:
                if self.is_alive() == True:
                    print(f'WOOHOO! {self.name} is the WINNER!!!!')
                elif opponent.is_alive() == True: 
                    print(f'YEEEEEHAAAAA!! {opponent.name} is the WINNER!!!!')


    



if __name__ == "__main__":
    hero1 = Hero("Black Panther")
    hero2 = Hero("Beast")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    
    
    
    
    
    # hero = Hero("Black Panther", 200)
    # hero.take_damage(150)
    # print (hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive)
    
    # ability = Ability("Punch", 90)
    # another_ability = Ability("Love", 100)
    # hero = Hero("Black Panther", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())
    