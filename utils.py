# Utilities (utils.py)
## To avoid clutter elsewhere

from time import localtime
from os import getcwd

import commands
import io_layer as io

# list of commands instanceable anywhere
# this allows for the definition of new user commands at runtime
class command_builder:
    def __init__(self):
        self.command_list = {
            ## hardcoded commands
            "esc": commands.escape,
            "quit": commands.quit,
            "new_file": commands.create_new_file
        }
    
    def update(self):
        ## use the io layer to grab .json input
        ## add these commands to the list
        return None
    
    def execute(self, command: str):
        return self.command_list[command]()

# Search after keyphrase through a string
## returns everything after the given command key
def grab_subphrase(phrase: str, key: str, max_length = None) -> str:
    if not key in phrase:
        return None ## specified key was not present, handles 1 expection
    if max_length:
        pass
    else:
        max_length = len(phrase)
    return phrase[ phrase.index(key) + len(key):max_length ] ## return everything after the key, up to max length

# Reading variables from files into memory

## grab just the value after a variable name in a string
def grab_sub_value(phrase, variable_name, expected_type):
    value = phrase.index(variable_name)
    phrase = phrase[(value + len(variable_name)):]
    if "," in phrase:
        phrase = phrase[0:phrase.index(',')]
    if ":" in phrase:
        phrase = phrase[1:]
    if "\n" in phrase:
        phrase = phrase[:-2]
    if "}" in phrase:
        phrase = phrase[:-1]
    
    try:
        outbox = expected_type(phrase)
    except Exception:
        return f"err: Locating varible: varaible location {phrase} to type {expected_type}."
    return outbox

## initialize the required varaibles file necessary for all work to be done
## which contains saved information so the program can run next time
def initialize_reqfile() -> str:
    directory = getcwd() + "\\req"
    filename = "req_vars.data"
    is_file_missing = io.create_new_file(directory, filename, "# description: Required Variables: All needed during runtime")
    if not is_file_missing: 
        ## check if it is empty
        with open(directory + "\\" + filename, 'r') as file:
            values = file.readlines()
        if values != None:
            return "fail: File nonempty"
    initial_data = [
        "{ last_opened: 2, version: 3}",
        "last_opened: None",
        "version: 0.2"
    ]
    io.append_lines(directory, filename, initial_data)
    return "succ: Initialized fully."

## look in the req_file for a specfic variable 
def pull_var_from_file(file_location, file_name, variable_name, expected_type):
    lines = io.read_all(file_location, file_name)
    if variable_name not in lines[1]:
        ## search for the variable name in any line
        index = 0
        for i in range(0, len(lines)):
            if variable_name in lines[i]:
                index = i
                break
    else:
        index = grab_sub_value(lines[1], variable_name, int)
    
    ## now that index is held, seek the value in this line of the file
    try:
        outbox = grab_sub_value(lines[index].strip(), variable_name, expected_type)
    except Exception:
        return f"err: could not find {index} lines in the file."
    return outbox

# Creation and Editing of Log Files

## global log number
log_number = 0

## create a new log
def get_logtime() -> str:
    timenow = localtime()
    outbox = ""
    for i in range(0, len(timenow)-2):
        outbox = outbox + "." + str(timenow[i])
    return outbox

def create_new_log(log_name: str, initial_line: str) -> tuple:
    timenow = get_logtime()
    path = getcwd() + "\\logs"
    file = log_name + timenow + ".txt"
    io.create_new_file(path, file, f"# Log Number: {log_number} @ {timenow}" + " Descriptor: " + initial_line)
    
    return (path, file)

def log_to(log_location: str, log_name: str, message_author: str, log_message: str):
    timenow = localtime()
    outbox_message = f"[By {message_author} on {timenow.tm_mon}.{timenow.tm_mday}.{timenow.tm_year} @ {timenow.tm_hour}:{timenow.tm_min}:{timenow.tm_sec}]: "
    outbox_message = outbox_message + log_message
    outbox = io.append_lines(log_location, log_name, [outbox_message])
    return outbox