from functions import promptinput
class ShipHull(object):
    def __init__(self):
        self.inventory = None
        self.heard_door_warning = False
        self.looks = [
            {'name': 'look_door', 'label': 'House'}
        ]
        self.gets = [
            {'name': 'get_note', 'label': 'Weapons'}
        ]
        self.places = [
            {'name': 'enter_quarters', 'label': 'Quarters'}
        ]
        self.uses = [
            {'name': 'use_keypad', 'label': 'Keypad' }
        ]

    def prompt(self):
        print "You've arrived at the ship's hull.  It's grey, dark, and dripping what you can only safely assume is fecal matter.  Your journey takes a pause when you reach the end of the hull and find a door with a electronic keypad, don't ask why but the buttons are in english."
    

