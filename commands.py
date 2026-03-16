# Commands file
## could be editable by user, maybe?

import utils as u

# list of commands instanceable anywhere
# this allows for the definition of new user commands at runtime
class command_builder:
    def __init__(self):
        self.command_list = {
            ## hardcoded commands
            "esc": escape,
            "quit": quit,
            "new_file": create_new_file
        }
    
    def update(self):
        ## use the io layer to grab .json input
        ## add these commands to the list
        return None
    
    def execute(self, command: str):
        return self.command_list[command]()

# Hardcoded, Unchanging Commands
## The user should not edit these ##

escape_keyphrase = "COMMAND_ESCAPE_LOOP"
def escape() -> str:
    print("<SYST>: ESCAPING ...")
    return escape_keyphrase

quit_keyphrase = "COMMAND_QUIT_ALL"
def quit():
    print("<SYST>: EXITING PROGRAM ...")
    return quit_keyphrase

# Functions

## Say something out to the user
## prompt: what are you saying?
## speaker: which actor is talking?
def say(prompt: str, speaker = "ARBY") -> None:
    print(f"<{speaker}>: {prompt}")

## Custom input function
## checks for system commands before returning a response
def command_checker(user_prompt: str) -> str:
    outbox = input(f"<ARBY>: {user_prompt}\n<USER>: ")
    command = u.grab_subphrase(outbox, "--")
    if command: 
        outbox = syst_commands.execute(command)
    
    return outbox

## Get user input
## user_prompt: what the user sees when they're entring the value
## expected_type: what type should the user response be?
def get_user_input(user_prompt: str, expected_type: type) -> list:
    outbox = command_checker(user_prompt)
    try:
        outbox = expected_type(outbox) ## attempt to cast to the correct type
    except:
        say(f"Expected type {expected_type}, but recieved type {type(outbox)}")
        for k in range(10, 0, -1):
            outbox = command_checker(f"Please ensure your response can be casted to {expected_type}. Type \'--esc\' to leave this loop. {k} attempts remaining.")
            try:
                outbox = expected_type(outbox)
                break
            except:
                if outbox == BREAK_THIS_LOOP:
                    return None
                say(f"This response cannot be casted to type {expected_type}.")
            
    
    return outbox