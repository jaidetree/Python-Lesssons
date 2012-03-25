from sys import exit
from random import randint
import re
from functions import *
from inventory import *
from spaceship import *

class GameEngine(object):

    def __init__(self, rooms):
        self.death_messages = [
            "Way to go skippy! No, wait, you're dead...",
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
        """Run through the games. Make sure you set the rooms array in this class' object initialization."""

        if len(self.rooms) < 1:
            print "There's no rooms!"
            exit()

        self.room = room = self.rooms[start_room]
        self.looks = room.looks
        self.gets = room.gets
        self.places = room.places
        self.uses = room.uses
        
        room.inventory = self.inventory
        
        clear()
        system_message('starting:', 'Spacecraft Adventure Danger')

        while True:
            next_room = self.process_response(promptinput(room.prompt(), self.validate_response))
            if isinstance(next_room, str) and self.rooms.has_key(next_room):
                self.room = room = self.rooms[next_room] 
                clear()
            elif next_room == "dead":
                self.dead();

    def validate_response(self, data):
        """As of right now this method just makes sure we're looking at a string for our commands."""

        if isinstance(data, str) and not data.isdigit():
            return True
        else:
            return False

    def process_response(self, command_string):
        """This functions processes the main commands used to control the game."""

        subjects = re.match('^([a-z]+) ([a-z\s]+\s)?([-a-z0-9]+)$', command_string, re.IGNORECASE)
        return_data = False

        if subjects != None:
            return_data = self._run_command(subjects.group(1), subjects.group(3))

        elif command_string.lower() == "help":
            self.help()

        elif not return_data:
            self.print_error()
            return False

        return return_data

    def _run_command(self, command_type, subject):
        """Runs the command from our current room module based on what the user entered."""

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
            if item.get('label').lower() == subject.lower():
                action = getattr(self.room, item.get('name'))
                return_data = action()

                if return_data == None:
                    return_data = True

                return return_data

        return False

    def print_error(self):
        """Used when we recieve a command the system has nothing to do with it."""
        system_message('error:', 'DOES NOT COMPUTE')

    def dead(self):
        """The player has died in the story"""
        system_message("GAME OVER:", self.death_messages[randint(0, len(self.death_messages)-1)])
        exit()
    
    def help(self):
        """Lists the available room actions/items/places to go."""

        clear()

        if len(self.places):
            system_message('help:', "Places you can go to")
            for place in self.places:
                print "enter {}".format(place['label']) 

        if len(self.looks):
            system_message('help:', "Sights to see")
            for sight in self.looks:
                print "look [at|the] {}".format(sight['label'])

        if len(self.gets):
            system_message('help:', "Items to get")
            for item in self.gets:
                print "get {}".format(item['label'])

        if len(self.uses):
            system_message('help:', "Objects to use")
            for item in self.uses:
                print "get {}".format(item['label'])

game = GameEngine({'spaceship': SpaceShip()})
game.play()

# inventory.add_to_inventory('flask', 'Exquisite Flask')

# inventory.list_inventory()
