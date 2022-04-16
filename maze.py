""" Game """

class Room:
    """ room in the game """
    rooms = []
    def __init__(self, name, info = '') -> None:
        self.name, self.info = name, info
        self.neighbours, self.item, self.character = [], None, None
        Room.rooms.append(self)

    def set_description(self, text):
        """ description of the room """
        self.info = text

    def add_neighbour(self, room2, typee):
        """ add neighbour """
        self.neighbours.append([room2, typee])

    def link_room(self, room2, typee="tunnel"):
        """ all neighbours of all rooms """
        self.add_neighbour(room2, typee)
        room2.add_neighbour(self, typee)

    def set_character(self, character):
        """ characters in this room """
        self.character = character

    def set_item(self, item):
        """ item in this room """
        self.item = item

    def get_details(self):
        """ print room details """
        print(f'{self.name}\n--------------------\n{self.info}')
        print('There are some rooms:')
        for room in self.neighbours:
            print(f'A {room[1]} to {room[0].name}')

    def get_item(self):
        """ return item """
        return self.item

    def get_character(self):
        """ return character """
        return self.character

    def move(self, direction):
        """ move """
        for room in self.neighbours:
            if room[0].name == direction:
                if room[1] != 'tunnel':
                    print(f"You can't cross {room[1]} without adder or by yourself")
                    return None
                return room[0]
        return False

class Character:
    """ character """
    def __init__(self, name, description, words='', weakness=None) -> None:
        self.name, self.description, self.words, self.weakness = name, description, words, weakness

    def set_conversation(self, words):
        """ words of the enemy when you meet him/her """
        self.words = words

    def describe(self):
        """ to print info """
        print(f'{self.name} is here!\n{self.description}')

    def interact(self, item):
        """ interact """
        if item == self.weakness:
            return True
        return False


class Infocharacter(Character):
    """ gives you info """
    def __init__(self, name, description, info='', words='', weakness=None) -> None:
        super().__init__(name, description, words, weakness)
        self.info, self.known = info, False



    def give_info(self):
        """ information """
        return self.info

    def talk(self):
        """ to talk """
        print(f'[{self.name} says]: {self.words}')

class SupportCharacter(Character):
    """ support character(tive you support) """

    def give_help(self, item):
        """ give help """
        return True if self.weakness == item else False

class Item:
    """ item """
    def __init__(self, name, text='') -> None:
        self.name, self.text = name, text

    def set_description(self, text):
        """ description of the item """
        self.text = text

    def describe(self):
        """ to describe item """
        print(f'The {self.name} is here - {self.text}')

    def get_name(self):
        """ name """
        return self.name
