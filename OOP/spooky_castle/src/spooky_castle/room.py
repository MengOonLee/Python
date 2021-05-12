class Room():
    
    # class variable outside the constructor
    number_of_rooms = 0
    
    def __init__(self, room_name):
        # instance variable inside the constructor
        self.__name = room_name
        self.__description = None
        self.__linked_rooms = {}
        self.__character = None
        self.__item = None
        
        Room.number_of_rooms = Room.number_of_rooms + 1
    
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        """
        Returns a string containing the description of the room
        """
        return self.__description
    
    @description.setter
    def description(self, room_description):
        self.__description = room_description
    
    @property
    def link_room(self):
        return self.__linked_rooms
        
    @link_room.setter
    def link_room(self, room_to_link, direction):
        self.__linked_rooms[direction] = room_to_link
        
    @property
    def character(self):
        return self.__character
    
    @character.setter
    def character(self, new_character):
        self.__character = new_character
        
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item_name):
        self.__item = item_name

            
#    def set_name(self, room_name):
#        self.name = room_name
    
    def describe(self):
        print(self.__description)
        
    def get_details(self):
        print("The " + self.__name)
        print("--------------------")
        print(self.__description)
        for direction in self.__linked_rooms:
            room = self.__linked_rooms[direction]
            print("The " + room.name + " is " + direction)
            
    def move(self, direction):
        if direction in self.__linked_rooms:
            return self.__linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
