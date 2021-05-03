class Item():
  
    def __init__(self, item_name):
        self.__name = item_name
        self.__description = None
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, item_name):
        self.__name = item_name
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, item_description):
        self.__description = item_description
        
    def describe(self):
        print("The [" + self.__name + "] is here - " + self.__description)