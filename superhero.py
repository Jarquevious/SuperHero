import random 
class Ability:
    def __init__(self, force, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
        self.name = force  
        self.attack_strength = 5
       #TODO: Instantiate the variables listed in the docstring with then
       # values passed in
    
    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
    #random.randint(0, 5) 
        return random.randint(0, 5)

if __name__ == "__main__":
            ability = Ability("Debugging Ability", 20)
            print(ability.name)
            print(ability.attack())