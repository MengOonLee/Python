class Room():
    
    # class variable outside the constructor
    num_rooms = 0
    
    def __init__(self, room_name):
        # instance variable inside the constructor
        self.name = room_name
        self.__description = None
        self.__linked_rooms = {}
        self.__character = None
        self.__item = None
        Room.num_rooms = Room.num_rooms + 1
        
    @classmethod
    def number_rooms(cls):
        return cls.num_rooms
        
    def description(self, room_description):
        self.__description = room_description
    
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
                
    @property
    def details(self):
        """
        Returns a string containing the description of the room
        """
        print(f"The {self.name}")
        print("--------------------")
        print(self.__description)
        for direction in self.__linked_rooms:
            room = self.__linked_rooms[direction]
            print(f"The {room.name} is {direction}")
            
    def move(self, direction):
        if direction in self.__linked_rooms:
            return self.__linked_rooms[direction]
        else:
            print("You can't go that way")
            return self