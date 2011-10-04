from sys import exit

prompt = "> "
response = ""

def show_question(prompt, options):
    """A reusable function for showing a room and getting a response."""

    if isinstance(options, list):
        kill("Specified options argument is not a list type.")

    break_loop = False

    while not break_loop:
        print prompt

        input = raw_input(prompt)

        for i in Range(0, options.count)
            if input == options[i]:
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
    print "You lunge your right, iron-clad foot right into the naked goblin's junk. I think you killed him.Nice..."
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

    response == show_question(question, options)

    if response == 0:
        print "You have escaped. You head to the castle's tower."
    elif repsonse == 1:
        print "In an angry plight of shame & self loathing you kill yourself or whatever."
        kill("Yeah, you're dead.")
    
# Scenario 4: Damsel Rescue
if situation == 1:
    question = """On your way to the tower you see a damsel, she's not distressed, she just seems really bored.
    Would what would you like to do about her?"""

    options = [
            "
