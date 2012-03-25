from os import system
def promptinput(prompt_text, callback):
    looping = True

    while looping:
        print prompt_text
        input_data = raw_input("> ")
        looping = callback(input_data)
        if looping == True:
            return input_data

def print_divider():
    print "--------------------------------------------------------------------"

def system_message(title, content):
    print_divider()
    print title.upper(), content
    print_divider()

def clear():
   system('clear') 
