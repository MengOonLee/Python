from spooky_castle.rpginfo import RPGInfo
from spooky_castle.item import Item
from spooky_castle.room import Room
from spooky_castle.character import Enemy, Friend

if __name__ == '__main__':

    RPGInfo.info()

    kitchen = Room("kitchen")
    kitchen.description("A dank and dirty room buzzing with flies.")

    dining_hall = Room("dining_hall")
    dining_hall.description("A large room with ornate golden decorations on each wall.")

    ballroom = Room("ballroom")
    ballroom.description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

    print("There are " + str(Room.number_rooms()) + " rooms to explore.")

    kitchen.link_room(dining_hall, "south")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")

    dave = Enemy("Dave", "A smelly zombie")
    # Add some conversation for Dave when he is talked to
    dave.conversation("Brrlgrh... rgrhl... brains...")
    # Set a weakness
    dave.weakness("cheese")
    dining_hall.character = dave

    catrina = Friend("Catrina", "A friendly skeleton")
    catrina.conversation("Why hello there.")
    ballroom.character = catrina

    cheese = Item("cheese")
    cheese.description("A large and smelly block of cheese.")
    ballroom.item = cheese

    book = Item("book")
    book.description("A really good book entitled 'Knitting for dummies'.")
    dining_hall.item = book

    current_room = kitchen
    backpack = []

    dead = False
    while dead == False:
        print("\n")
        current_room.details

        inhabitant = current_room.character
        if inhabitant is not None:
            inhabitant.describe()

        item = current_room.item
        if item is not None:
            item.describe()

        command = input("> ")

        # Check whether a direction was typed
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "fight":
            # You can check whether an object is an instance of a particular class with
            # isinstance() - useful! This code means "If the character is an Enemy"
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()
                # Do I have this item?
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.character = None
                        if Enemy.number_enemies() == 0:
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print(f"You don't have a {fight_with}")
            elif inhabitant is not None and isinstance(inhabitant, Friend):
                inhabitant.no_fight()
            else:
                print("There is no one here to fight with")
        elif command == "hug":
            if inhabitant is not None:
                if isinstance(inhabitant, Enemy):
                    print("I wouldn't do that if I were you...")
                else:
                    inhabitant.hug()
            else:
                print("There is no one here to hug :(")
        elif command == "take":
            if item is not None:
                print(f"You put the {item.name} in your backpack")
                backpack.append(item.name)
                current_room.item = None

    RPGInfo.author = "Raspberry Pi Foundation"
    RPGInfo.credits()