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

##