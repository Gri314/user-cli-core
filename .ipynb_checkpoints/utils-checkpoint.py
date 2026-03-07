# Utilities (utils.py)
## To avoid clutter elsewhere

import commands

# list of commands instanceable anywhere
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
    
    def execute(self, command):
        self.command_list[command]()

# Search after keyphrase through a string
## returns everything after the given command key
def grab_subphrase(phrase: str, key: str) -> str:
    if not key in phrase:
        return None ## specified key was not present, handles 1 expection
    return phrase[ phrase.index(key) + len(key): ] ## return everything after the key
    