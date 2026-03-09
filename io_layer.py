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

## checks for a files' existence, then writes a message to a new file if it doesn't
## returns True if it worked, False if it didn't
def create_new_file(file_location: str, file_name: str, optional_initial_message = "") -> bool:
    if does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'w') as file:
            file.write(optional_initial_message)
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
                    return line
                i = i + 1
            return None
    except Exception:
        return None

## overwrite a specific line of a file
## returns None if the file does not exist
## returns True if it worked, false if it didn't (for example, line did not exist)
def write_line(file_location: str, file_name: str, line_number: int, leave_input_untouched = False) -> bool:
    if not does_file_exist_here(file_location, file_name):
        return None
    try:
        with open(file_location + "\\" + file_name, 'r+') as file:
            i = 0
            for line in file:
                if line_number == i:
                    