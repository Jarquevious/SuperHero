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

class Weapon(Ability):
    def attack(self):
        return random.randint(self.mxdmg // 2, self.mxdmg)


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

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return 1
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

    def attack(self, opponents):
        ''' Sets up each time to check if they are alive and if they are it will set them up to fight.'''

        alive_heroes = []
        alive_opponents = []

        for i in self.heroes:
                if i.status == "alive":
                    alive_heroes.append(self.heroes.index(i))
        
        for x in opponents.heroes:
                if x.status == "alive":
                    alive_opponents.append(opponents.heroes.index(x))

        while len(alive_heroes) > 0 and len(alive_opponents) > 0:
            random_hero_1 = self.heroes[random.choice(alive_heroes)]
            random_hero_2 = opponents.heroes[random.choice(alive_opponents)]

            random_hero_1.fight(random_hero_2)

            for death1 in self.heroes:
                if death1.status == "dead":
                    alive_heroes.pop(self.heroes.index(death1))
            
            for death2 in opponents.heroes:
                if death2.status == "dead":
                    alive_opponents.pop(opponents.heroes.index(death2))
        
        if len(alive_heroes) > 0:
            return self.name
        elif len(alive_opponents) > 0:
            return opponents.name
        elif len(alive_heroes) == len(alive_opponents):
            return "Draw!"

    def update_kills(self, kills):
        """Updates a heroes kill count for kills made in team battles """
        for hero in self.heroes:
            hero.add_kill(kills)

    def alive_heroes(self):
        '''Makes a list of alive heroes from team '''
        alive_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)
            return alive_heroes

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = 100
            hero.status = "Alive"

    def find_hero(self, name):
        """Find index of specific hero on a team """
        hero_index = -1
        for x, hero in enumerate(self.heroes):
            if hero.name == name:
                hero_index = x
        return hero_index

    def stats(self):
        '''Print team statistics'''

        for hero in self.heroes:
            print("------------------------------------")
            print("Hero: {} | Kills: {} : | Deaths: {}".format(hero.name, hero.kills, hero.deaths))

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
    