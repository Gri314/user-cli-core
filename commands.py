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

