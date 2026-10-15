class Character():
    
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.__conversation = None
        
    # Describe this character
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
        
    # Set what this character will say when talked to
    def conversation(self, conversation):
        self.__conversation = conversation
        
    # Talk to this character
    def talk(self):
        if self.__conversation is not None:
            print(f"[{self.name} says]: {self.__conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")
            
    # Fight with this character
    def no_fight(self):
        print(f"{self.name} doesn't want to fight with you")
    
class Enemy(Character):
    
    num_enemies = 0
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.__weakness = None
        Enemy.num_enemies = Enemy.num_enemies + 1
        
    @classmethod
    def number_enemies(cls):
        return cls.num_enemies
    
    def weakness(self, item_weakness):
        self.__weakness = item_weakness
    
    def fight(self, combat_item):
        if combat_item == self.__weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            Enemy.num_enemies = Enemy.num_enemies - 1
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return False
        
class Friend(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        
    def hug(self):
        print(f"{self.name} hugs you back!")