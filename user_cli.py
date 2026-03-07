# User Command-Line-Interface (user_cli.py)
## I deal with user input and relate that input to various functions within the program
## My goal is to make it as simple as possible for the user (presumably nonproficient technology users) to accomplish their task
## My commands are simply interpretable and hard to break -- safe on hardware and forgiving of user mistakes

import utils as u

## instantiate necessary commands before operation
syst_commands = u.command_builder()

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
    if command: syst_commands.execute(command)
    
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
                say(f"This response cannot be casted to type {expected_type}.")
            
    
    return outbox

value = get_user_input("Please enter your favorite number: ", int)

value = get_user_input("Please enter your second favorite number: ", int)

print(value)