""" Game """

class Room:
    """ room in the game """
    def __init__(self, name, info = '') -> None:
        self.name, self.info = name, info
        self.neighbours, self.item, self.character = {}, None, None

    def set_description(self, text):
        """ description of the room """
        self.info = text

    def link_room(self, room2, direction):
        """ neighbours of the room """
        self.neighbours[direction] = room2

    def set_character(self, character):
        """ characters in this room """
        self.character = character

    def set_item(self, item):
        """ item in this room """
        self.item = item

    def get_details(self):
        """ print room details """
        print(f'{self.name}\n--------------------\n{self.info}')
        for room in self.neighbours.items():
            print(f'The {room[1].name} is {room[0]}')

    def get_item(self):
        """ return item """
        return self.item

    def get_character(self):
        """ return character """
        return self.character

    def move(self, direction):
        """ move """
        return self.neighbours[direction]



class Enemy:
    """ enemies """
    defeated = 0
    def __init__(self, name, description, words='', weakness=None) -> None:
        self.name, self.description, self.words, self.weakness = name, description, words, weakness
        self.weakness = weakness

    def set_conversation(self, words):
        """ words of the enemy when you meet him/her """
        self.words = words

    def set_weakness(self, objt):
        """ weakness of the enemy """
        self.weakness = objt

    def describe(self):
        """ to print info """
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        """ to talk """
        print(f'[{self.name} says]: {self.words}')

    def fight(self, item):
        """ fighting """
        if item == self.weakness:
            Enemy.defeated += 1
            return True
        return False

    def get_defeated(self):
        return Enemy.defeated


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
