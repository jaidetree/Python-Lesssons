from sys import exit
import re
from functions import *
from spaceship import *
from inventory import *

class GameEngine(object):

    def __init__(self, rooms):
        self.death_messages = [
            "Way to go skippy! No, wait, you're dead!",
            "I wouldn't want to be you right now. You know. Because you're dead.",
            "You are D-E-A-D dead!",
            "You died. Was your run as good for you as it was for me?"
        ]
        self.rooms = rooms
        self.room = {}
        self.looks = []
        self.gets = []
        self.places = []
        self.uses = []
        self.inventory = Inventory()
    
    def play(self, start_room = "spaceship"):
        if len(self.rooms) < 1:
            print "There's no rooms!"
            exit()

        self.room = room = self.rooms[start_room]
        self.looks = room.looks
        self.gets = room.gets
        self.places = room.places
        self.uses = room.uses

        while True:
            next_room = promptinput(room.prompt(), self.process_response)

            if next_room != False:
                self.room = room = self.rooms[next_room] 

    def process_response(self, command_string):
        subjects = re.match('^([a-z]+) ([a-z\s]+\s)?([-a-z0-9]+)$', command_string, re.IGNORECASE)
        return_data = self._run_command(subjects.group(1), subjects.group(3))

        if not return_data:
            self.print_error()
            return False

        return return_data

    def _run_command(self, command_type, subject):
        group = []

        if command_type == "use":
            group = self.uses
        elif command_type == "look":
            group = self.looks
        elif command_type == "enter":
            group = self.places
        elif command_type == "get":
            group = self.gets

        for item in group:
            if item['label'].lower() == subject.lower():
                action = getattr(self.room, item['name'])
                action()
                return True

        return False

    def print_error(self):
        print "\nERROR: DOES NOT COMPUTE!!!\n\n"

    def dead(self):
        print self.death_messages[randint(0, len(self.death_messages)-1)]
        exit()

game = GameEngine({'spaceship': SpaceShip()})
game.play()

# inventory.add_to_inventory('flask', 'Exquisite Flask')

# inventory.list_inventory()
