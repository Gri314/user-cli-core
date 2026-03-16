# User Command-Line-Interface (user_cli.py)
## I deal with user input and relate that input to various functions within the program
## My goal is to make it as simple as possible for the user (presumably nonproficient technology users) to accomplish their task
## My commands are simply interpretable and hard to break -- safe on hardware and forgiving of user mistakes

import utils as u
import commands as c

# Command mapping to actual functions


# Program Opening Script

c.say("Getting started...")
u.initialize_reqfile()
version = u.pull_var_from_file(u.getcwd() + "\\req", "req_vars.data", "version", float)
c.say(f"System ready at version {version}.")

value = c.get_user_input("Welcome. What is your first command?", str)
