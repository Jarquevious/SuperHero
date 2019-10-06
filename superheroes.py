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
        self.deaths = 0
        self.kills = 0
   
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon) 

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
        while self.is_alive() and opponent.is_alive():
            if not self.abilities and not opponent.abilities:
                print("Draw")
                return
            else:
                damage = self.attack()
                print(self.name + ': ' + str(damage))
                opponent.take_damage(damage)
                damage = opponent.attack()
                print(opponent.name + ': ' + str(damage))
                self.take_damage(damage)

        if self.is_alive():
            print(self.name + ' won!')
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print(opponent.name + ' won!')
            opponent.add_kill(1)
            self.add_death(1)

    def add_kill(self, num_kills):
        self.kills += num_kills  

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    

class Team:
    def __init__(self, name, hello=100):
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

class Arena:    
    def __init__(self):
        self.team_one: None
        self.team_two: None

    def create_ability(self):
        name = input("Enter Name of Ability: ")
        strength = int(input("Enter Ability Attack Strength: "))
        ability = Ability(name, strength)
        return ability

    def create_weapon(self):
        name = input("Enter Weapon Name: ")
        strength = int(input("Enter Weapon Attack Strength: "))
        weapon = Weapon(name, strength)
        return weapon

    def create_armor(self):
        name = input("Enter Armor Name: ")
        block_power = int(input("Enter Blocking Strength: "))
        armor = Armor(name, block_power)
        return armor

    def create_hero(self):
        name = input("Enter Hero Name: ")
        hero = Hero(name)
        menu_option = 0
        while menu_option != '4':
            menu_option = input("Enter 1 to add an ability\nEnter 2 to add a weapon\nEnter 3 to add an armor\nEnter 4 when you're Finish\n")
            if menu_option == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif menu_option == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif menu_option == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
            elif menu_option == '4':
                print('Finished creating ' + hero.name)
            else:
                print('Please select a value 1-4')
        return hero

    '''Prompt the user to build team_one '''
    def build_team_one(self):
        team_name = input('Name your Team?\n')
        self.team_one = Team(team_name)
        num_heroes = input(f'How many heroes do you want on team {self.team_one}?\n')
        for i in range(int(num_heroes)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
        
        self.team_one.view_all_heroes()
    
    '''Prompt the user to build team_two '''
    def build_team_two(self):
        team_name = input('Name your team\n')
        self.team_two = Team(team_name)
        num_heroes = input(f'How many heroes do you want on team {self.team_two}?\n')
        for i in range(int(num_heroes)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

        self.team_two.view_all_heroes()

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def count_alive(self, team):
        ''' Count number of heroes alive on a team'''
        alive = 0
        for hero in team.heroes:
            if hero.is_alive():
                alive += 1
        return alive
    
    def count_kills(self, team):
        ''' Count kills on a team'''
        team_kills = 0
        for hero in team.heroes:
            team_kills += hero.kills
        return team_kills      

    def count_deaths(self, team):
        ''' Count deaths on a team'''
        team_deaths = 0
        for hero in team.heroes:
            team_deaths += hero.deaths  
        return team_deaths

    def who_won(self):
        '''Prints which team won to terminal'''
        team_one_alive = self.count_alive(self.team_one)
        team_two_alive = self.count_alive(self.team_two)
        if team_one_alive > team_two_alive:
            print (self.team_one.name + ' won!')
        elif team_one_alive < team_two_alive:
            print (self.team_two.name + ' won!')
        else:
            print ('Draw!')
    def show_stats(self):
        ''' Prints team statistics to terminal'''
        team1_kills = self.count_kills(self.team_one)
        team1_deaths = self.count_deaths(self.team_one)
        average1_kills = team1_kills // len(self.team_one.heroes)
        average1_deaths = team1_deaths // len(self.team_one.heroes) 

        team2_kills = self.count_kills(self.team_two)
        team2_deaths = self.count_deaths(self.team_two)
        average2_kills = team2_kills // len(self.team_two.heroes)
        average2_deaths = team2_deaths // len(self.team_two.heroes)

        self.who_won()
        print(self.team_one.name + ' average kills: ' + str(average1_kills))
        print(self.team_one.name + ' average deaths: ' + str(average1_deaths))
        print(self.team_one.name + "'s surviving heroes: ")
        self.team_one.show_surviving_heroes()
        
        print(self.team_two.name + ' average kills: ' + str(average2_kills))
        print(self.team_two.name + ' average deaths: ' + str(average2_deaths))
        print(self.team_two.name + "'s surviving heroes: ")
        self.team_two.show_surviving_heroes()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

# if __name__ == "__main__":
#     hero1 = Hero("Black Panther")
#     hero2 = Hero("Beast")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)
    
    
    
    
    
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
    