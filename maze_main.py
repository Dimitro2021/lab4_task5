""" main for game """

import maze

start, roomA, roomB, roomC = maze.Room("START"), maze.Room("room A"), maze.Room("room B"), maze.Room("room C"),
roomD, roomF, Treasure = maze.Room("room D"), maze.Room("room E"), maze.Room("Treasure")

rooms = [roomA, roomB, roomC, roomD, roomF]

for room in rooms:
    room.set_description(f'You are in the room {room.name} in the MAZE')

start.set_description('Start of the maze')
Treasure.set_description('This is room with treasure')

start.link_room(roomA)
start.link_room(roomB)
roomA.link_room(roomD)
roomA.link_room(roomF, 'river')
roomB.link_room(roomC)
roomC.link_room(roomD)
Treasure.link_room(roomD, 'gulf')
Treasure.link_room(roomF)

mouse = maze.Infocharacter('Mouse', 'A hungry friend', weakness='cheese')
mouse.set_conversation('I will give you some important info, but I want cheese instead')
roomC.set_character(mouse)

sailor = maze.SupportCharacter('Sailor', 'Can cross the river', weakness='coins')
sailor.set_conversation('I can get you on the other side of the river but give me some money')
roomA.set_character(sailor)

dwarf = maze.Infocharacter('Dwarf', 'Has the gold apple', weakness='apple')
dwarf.set_conversation('I want to eat an apple! Why it is so hard?')
Treasure.set_character(dwarf)

cheese = maze.Item('cheese', text='Little peace of yellow cheese')
roomB.set_item(cheese)
apple = maze.Item('apple', text='real big red apple')
coins = maze.Item('coins', 'some money')
roomD.set_item(coins)
rope_ladder = maze.Item('rope ladder', text='something to cross rifts')
roomC.set_item(rope_ladder)

current_room = start
backpack = ['apple']

won = False

print("""hello hero
you are sent here to find gold apple, the ornament of our city
you entered the maze. People gave you just backpack and an apple in it, there are some options for you
there is a maze""")
with open('maze.txt', 'r') as file:
    for line in file:
        print(line)
print('Good luck')


while True:
    if current_room == start and won:
        print("Everyone congratulate you, You are a hero\
THE END")
        break
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()
    print(r"""
You can:
take (take object)
interact, talk (if there is someone in the room)
to change the room input name of the room
""")

    command = input("> ")

    if command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "interact":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you offer?")
            fight_with = input()
            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.interact(fight_with) == True:
                    # What happens if you win?
                    if inhabitant.name == 'Sailor':
                        current_room.character = None
                        current_room = roomF if current_room == roomA else roomA
                        current_room.character = sailor
                    if inhabitant.name == 'Dwarf':
                            print("You put the gold apple in your backpack")
                            backpack.append('gold apple')
                            print('You won the game. Get back to the START to end it')
                            won = True
                    if inhabitant.name == 'Mouse':
                        current_room.character = None
                        print("There is Dwarf in Treasure room, he has a gold apple. He stole it to eat, but it is too hard. I've heard him crying there. Thank you for cheese")
                else:
                    # What happens if you lose?
                    print("That's not what is needed")
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif current_room.move(command) != False:
        # Move in the given direction
        neww = current_room.move(command)
        if current_room == Treasure and 'rope ladder' in backpack and command == 'room D':
            neww = roomD
        current_room = neww if neww is not None else current_room
    else:
        print("I don't know how to " + command)
