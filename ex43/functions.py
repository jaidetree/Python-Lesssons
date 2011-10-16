def promptinput(prompt_text, callback):
    looping = True

    while looping:
        print prompt_text
        input_data = raw_input("> ")
        looping = callback(input_data)
        if looping:
            return input_data
