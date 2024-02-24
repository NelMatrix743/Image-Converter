import colorama 
from colorama import Fore, Back, Style


__programmer_info: str = Fore.GREEN + " Programmer.nick_name: Nelmatrix" + (" "*67) + Fore.GREEN  + "v-1.0.0\n"

# Program welcome screen art
program_banner_: str = r"""
 ___ __   __     _      _____  _____       ____   ___   _   _ __     __ _____  ____    _____  _____  ____
|_ _||  \/  |   / \    / ____|| ____|     / ___| / _ \ | \ | |\ \   / /| ____||  _  \ |_   _|| ____||  _  \
 | | | |\/| |  / _ \   | |  _ |  _|       | |    | | | |  \| | \ \ / / |  _|  | |_) |   | |  |  _|  | |_) |
 | | | |  | | / ___ \  | |_| || |___      | |___ | |_| | |\  |  \ V /  | |___ |  _ <    | |  | |___ |  _ <
|___||_|  |_|/_/   \_\ \ ____||_____|     \____| \___/ |_| \_|   \_/   |_____||_| \_\   |_|  |_____||_| \_\ """ + "\n" + __programmer_info

#_sp: str = ' ' * 40
# program sub banner
#sub_banner_: str = ('\n'+'|'+("="*105)+'|'+'\n')+('|='+_sp+Fore.YELLOW+" IMAGE FORMAT CONVERTER"+_sp+Fore.BLUE+'=|'+'\n')+('|'+'='*105 +'|')

def welcome_screen() -> None:  
    """ Displays welcome message and program banner(ascii-art) """ 
    print(Fore.BLUE, Style.BRIGHT, program_banner_, Style.RESET_ALL, end="") # print banner and reset terminal color;
    #print(Fore.BLUE, Style.BRIGHT, sub_banner_)


def success_message_display(message: str, type_indicator: str = '+', start_newline: int = 0, end_newline: int = 0) -> None: 
    """ Displays success message when a task is sucessfully completed """
    nwln_start: str = '\n' * start_newline
    nwln_end: str = '\n' * end_newline
    __message__: str = Fore.GREEN + Style.BRIGHT + f"[{type_indicator}] " + message + Style.RESET_ALL
    print(nwln_start, __message__, end=nwln_end) # print message and reset color;


def error_message_display(message: str, type_indicator: str = '-', start_newline: int = 0, end_newline: int = 0) -> None: 
    """ Displays error message when a task is not sucessfully completed due to an error """
    nwln_start: str = '\n' * start_newline
    nwln_end: str = '\n' * end_newline
    __message__: str = Fore.RED + Style.BRIGHT + f"[{type_indicator}] " + message + Style.RESET_ALL
    print(nwln_start, __message__, end=nwln_end) # print message and reset color;


def in_process_message_display(message: str, type_indicator: str = '*', start_newline: int = 0, end_newline: int = 0) -> None:
    """ Displays a message when the program is currently processing a file """
    nwln_start: str = '\n' * start_newline
    nwln_end: str = '\n' * end_newline
    __message__: str = Fore.YELLOW + Style.BRIGHT + f"[{type_indicator}] " + message + Style.RESET_ALL
    print(nwln_start, __message__, end=nwln_end) # print message and reset color;



if __name__ == "__main__": 
    welcome_screen()
    module_version: str = "1.0.0"
    print(f"Name: screen.py \nVersion: {module_version}\nFile Path: {__file__}")

# end of program 