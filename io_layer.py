# io_layer
## specifically for file interactions
## python is already pretty good about preventing corruptions, but this way we are EXTRA safe ...
##  I intend to use this application with sensitive information, so this is necessary for legality (in Texas)

## tries to read a file of that name, handles exception as No file exists
## returns if the file exists there or ot
def does_file_exist_here(file_location: str, file_name: str) -> bool:
    try:
        with open(file_location + "\\" + file_name, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

## get the number of lines in a file
## can "safely" check very large files
def get_number_of_lines(file_location: str, file_name: str) -> int:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'r') as file:
            outbox = sum(1 for line in file)
        return outbox
    except Exception:
        return None
    
## checks for a files' existence, then writes a message to a new file if it doesn't
## returns True if it worked, False if it didn't
def create_new_file(file_location: str, file_name: str, optional_initial_message = "") -> bool:
    if does_file_exist_here(file_location, file_name):
        return None
    try:
        if optional_initial_message != "":
            if not "\n" in optional_initial_message:
                optional_initial_message = optional_initial_message + "\n"
        with open(file_location + "\\" + file_name, 'w') as file:
            file.write(optional_initial_message)
        return True
    except Exception:
        return False

## get a specific line of a text file, will be useful for logs later
## you can strip these lines later if you feel like it.
def read_line(file_location: str, file_name: str, line_number: int) -> str:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'r') as file:
            i = 0
            for line in file:
                if line_number == i:
                    file.close()
                    return line
                i = i + 1
        ## Never reached the desired line
        return None
    except Exception:
        return None

## add lines at the end of a file, using the \n newline character
def append_lines(file_location: str, file_name: str, lines_to_append: list[str], include_newline = True) -> bool:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        newline_character = "\n" if include_newline else " "
        with open(file_location + "\\" + file_name, 'a') as file:
            for line in lines_to_append:
                file.write(line + newline_character)
    except Exception:
        return None

## read all lines up to the given number 
## READS ALL these lines into memory
def read_up_to_line(file_location: str, file_name: str, line_number: int):
    if not does_file_exist_here(file_location, file_name):
        return ":: error noFileDetected"
    try:
        with open(file_location + "\\" + file_name, 'r') as file:
            i = 0
            outbox = ["" for k in range(0, line_number+1)] 
            for line in file:
                outbox[i] = line
                if line_number == i:
                    file.close()
                    return outbox
                i = i+1
        ## there were not enough lines in the file
        return ":: error notEnoughLines"
    except Exception:
        return ":: error otherException"

## overwrite a certain line in a file
## TRIES TO READ ENTIRE FILE INTO MEMORY
def replace_line(file_location: str, file_name: str, line_number: int, replacement_text: str) -> str:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'r+') as file:
            lines = file.readlines()
            i, flag = 0, False
            for line in lines:
                if i == line_number:
                    flag = True
                    break
                i = i + 1
            if not flag:
                return ":: error NotEnoughLines"
            
            if "\n" not in replacement_text:
                replacement_text = replacement_text + "\n"
            lines[line_number] = replacement_text
        return ":: success"
    except Exception:
        return ":: error OtherException"
    
## Read the entire file into memory as a list, with no newline chars
def read_all(file_location: str, file_name: str) -> list[str]:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception:
        return ["err: OtherException (file too large?)"]
    