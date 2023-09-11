import colorama 
from colorama import Fore, Back, Style

# initialising the colorama to enable console text formatting especially on MS-DOS Windows cmd 
colorama.init() 



def welcome_screen() -> None:
    """ Displays welcome message """ 
    pass


def sucess_message_display(message: str) -> None: 
    """ Displays success message when a task is sucessfully completed """
    pass


def error_message_display(message: str) -> None: 
    """ Displays error message when a task is not sucessfully completed due to an error """
    pass


def in_process_message_display(message: str) -> None: 
    """ Displays a message when the program is currently processing a file """
    pass 



if __name__ == "__main__": 
    module_version: str = "1.0.0"
    print(f"Name: screen.py \nVersion: {module_version}")

# end of program 