from functions import promptinput
class SpaceShip(object):
   
    def __init__(self):
        self.has_weapons = False
        self.weapon_name = ""
        self.looks = [
            {'name': 'look_spacecraft', 'label': 'Spacecraft'},
            {'name': 'look_house', 'label': 'House'}
        ]
        self.gets = [
            {'name': 'get_weapons', 'label': 'Weapons'}
        ]
        self.places = [
            {'name': 'enter_spacecraft', 'label': 'Spacecrafts'}
        ]
        self.uses = []
        
    def prompt(self):
        return "You were enjoying a Saturday afternoon outside your house and suddenly a giant spacecraft crashes right into your backyard.  What are you going to do about it?"

    def look_spacecraft(self):
        return "You take a look at the spacecraft.  You realize by it's harsh jagged edges that it's probably not friendly.  You may need to get some weapons."

    def look_house(self):
        return "Looking at your house you realize it's fully intact, not a scratch on it. Oh but all your neighbors are dead."

    def get_weapons(self):
        self.weapon_name = promptinput("You run right into your house and rip apart your microwave, attach a spatula, a nail gun, and some various kitchenwhere to form what appears to be a very deadly weapon. You give it the name:", self.validate_weapon_name)

        print "You named your weapon {}, it's weird that you called it that, but ok. You make your way back to the spaceship in your backyard.".format(self.weapon_name)

    def validate_weapon_name(self,data):
        if isinstance(data, str) and not data.isdigit():
            return True
        else:
            return False

    def enter_spacecraft(self):
        prompt = "You enter the spacecraft spacecraft.  As soon as you enter a horrific looking alien with razor sharp teeth and blood dripping claws lunges at you!"
        
        if has_weapons:
            prompt += "Reacting quickly, you pull out your {} and blast it's face off.  Killing it instantly!".format(self.weapon_name);
        else:
            prompt += "Having no arms to defend your self it just rips you to shreds and eat your guts."
            return 'dead'

        return 'ship_hull'

