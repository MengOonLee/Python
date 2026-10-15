class Item():
  
    def __init__(self, item_name):
        self.name = item_name
        self.__description = None
        
    def description(self, item_description):
        self.__description = item_description
    
    def describe(self):
        print(f"The [{self.name}] is here - {self.__description}")