# Commands file
## could be editable by user, maybe?

escape_keyphrase = "COMMAND_ESCAPE_LOOP"
def escape() -> str:
    print("<SYST>: ESCAPING ...")
    return escape_keyphrase

quit_keyphrase = "COMMAND_QUIT_ALL"
def quit():
    print("<SYST>: EXITING PROGRAM ...")
    return quit_keyphrase

def create_new_file():
    filename = get_user_input("What is the new file's name?", str)
    value = get_user_input("Should the file exist somewhere else? (Y/N)", str)
    if "Y" in value:
        filepath = get_user_input("Please specify a new path: ", str)
    else:
        filepath = u.getcwd() + "\\user_files"
    return filename, filepath