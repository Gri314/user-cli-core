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
            "quit": commands.quit
        }
    
    def update(self):
        ## use the io layer to grab .json input
        ## add these commands to the list
        return None
    
    def execute(self, command: str):
        return self.command_list[command]()

# Search after keyphrase through a string
## returns everything after the given command key
def grab_subphrase(phrase: str, key: str) -> str:
    if not key in phrase:
        return None ## specified key was not present, handles 1 expection
    return phrase[ phrase.index(key) + len(key): ] ## return everything after the key

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