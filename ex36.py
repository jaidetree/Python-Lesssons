from sys import exit

response = ""

def show_question(prompt, options):
    """A reusable function for showing a room and getting a response."""

    if not isinstance(options, list):
        print "Options is a: " + str(type(options))
        kill("Specified options argument is not a list type.")

    while True:
        print "\n" + prompt

        print "\nYour choices are:\n"

        for i in range(0, len(options)):
            print "{}.) \"{}\"".format(i + 1, options[i])

        input = raw_input("> ")

        for i in range(0, len(options)):
            if input == options[i] or ( input.isdigit() and int(input) - 1 == i):
                return i

        print "That was not a valid response. Try again."

def kill(message):
    print message
    exit()

# Initial variables
question = ""
options = []
situation = 0

# Starting Room
question = """Your journey starts at a decreped castle with a sign that reads "GO AWAY" what appears to be written in blood. 
Do you enter the castle?"""
options = [ 
    "Yes",
    "No" 
    ]

response = show_question(question, options)

if response == 0:
    print "Alright. You entered the castle. Good job hero."
elif response == 1:
    print "Fine... be that way. Hope you don't get eaten by a bear..."
    kill("You encounter a bear who totally eats you and shits you out in the woods, unbeknownst to the rest of this plane of existence.")
    
# Scenario 2: Goblin bullshit.
question = """Upon searching around for snacks you stumble upon an angry, naked goblin shouting elvish obscentities at you. How would you handle this situation?"""
options = [
        "Threaten to send him to the moon",
        "Kick him in the junk",
        "Rip his head off"
        ]

response = show_question(question, options)

if response == 0:
    print "The naked goblin does not like the moon, he now comences clubbing you to death...with his penis."
    kill("...and a few harsh blows later you're cold lifeless body hugs the castle floor for eternity. Also, that naked goblin is probably going to defile your corpse. Just so you know...") 
elif response == 1:
    print "You lunge your right, iron-clad foot right into the naked goblin's junk. I think you killed him. Nice..."
    situation = 1
elif response == 2:
    print "Jesus christ! You just ripped that things head off, the poor bastard screamed so loud you've awaken the castle's ghosts which snatch you from the ground and throw you in a dungeon."
    situation = 2

# Scenario 3: Dungeon time
if situation == 2:
    question = """Well, your needless display of violence just got you thrown into the ghost king's sex dungeon.
    What now?"""
    options = [
            "Escape",
            "I want to die!!!"
            ]

    response = show_question(question, options)

    if response == 0:
        print "You have escaped. You head to the castle's tower."
    elif response == 1:
        print "In an angry plight of shame & self loathing you kill yourself or whatever."
        kill("Yeah, you're dead.")

    situation = 0
    
# Scenario 4: Damsel Rescue
if situation == 1:
    question = """On your way to the tower you see a damsel, she's not distressed, she just seems really bored and is staring out a window with her back turned to you."
    Would what would you like to do about her?"""

    options = [
            "I don't care",
            "Offer her a cigarette",
            "Try to start a conversation"
            ]

    response = show_question( question, options )

    if response == 0:
        print "You decide to ignore her and move on towards the top of the tower. Probably a safe bet this being a castle full of ghosts and naked goblins and all."
    elif response == 1:
        print "Sounding immencely delighted by your offer, you approach her, right as you reach to hand her one of your smokes she shanks you and takes your money." 
        kill("Now bleeding and poor, no one wants anything to do with you. You're just left there to die.")
    elif response == 2:
        print "You try to ask her wassup but she just sighs and continues staring out the window. Defeated, you tronce forward."

    response = 0

# Scenario 5: Gold

question = """You made it to the top of the tower! Upon endering the room you find out there's an eleveator which will take you to the front gate, oh and piles of gold just laying about. Curse the lazy slobs that dwelled here beforeth!
Make your move."""

options = [
        "Take the gold",
        "Leave",
        "Go to bed"
        ]

response = show_question(question, options)

if response == 1:
    print "You take the gold, you leave the castle. You're a better man for it. Well played."
elif repsonse == 2:
    print "You leave but you didn't take the gold, which of course a duke comes and arrests you. This castle was forbidden and you have no gold to bribe him. You're just gonna rot in a jail cell somewhere."
elif response == 3:
    print "Not knowing what to do, you decide to go to bed. You mysteriously die in your sleep."
    kill("It wasn't that mysterious, you were drunk and choked on your own vomit. Way to go Hendrix.") 

print "You won the game. Sweet dreams!"
