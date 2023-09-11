# !/usr/bin/python3

###############################################################################################################################
# Programmer.name = Nelson Chidi                                                                                              #
# Programmer.nick_name = Nelmatrix                                                                                            #
# Programmer.GitHub.name = NelMatrix743                                                                                       #
# Programmer.GitHub.url = https://github.com/NelMatrix743                                                                     #
# source_code.version = 1.0.0                                                                                                 #
#                                                                                                                             #
###############################################################################################################################

# The main module of the image converter program
import argparse 
import os 
import pathlib
from collections.abc import Iterator 
from package import screen, supported_formats

# simple exception class 
class WrongOutputException(Exception): 
    pass


PROG_DESCRIPTION: str = """This is a simple command line utility to convert images from one format to another. 
                        Supported image formats are: JPEG, PNG, SVG, WEBP
                        """
EXIT_MESSAGE: str = """ This is a simple exit message"""
INVALID_INPUT_ERROR: str = "Invalid input: The file you provided is either not an image file or it is corrupted!"
INVALID_OUTPUT_ERROR: str = "Invalid output: The output file-path you provided does not exist!"


def parser_initialiser() -> argparse.ArgumentParser: 
    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(description=PROG_DESCRIPTION, epilog=EXIT_MESSAGE)  

    group_1: argparse._ArgumentGroup = argument_parser.add_argument_group(title="INPUT OPTIONS")
    group_2: argparse._ArgumentGroup = argument_parser.add_argument_group(title="FORMAT OPTIONS")
    group_3: argparse._ArgumentGroup = argument_parser.add_argument_group(title="OUTPUT OPTIONS")

    input_type_group: argparse._MutuallyExclusiveGroup = group_1.add_mutually_exclusive_group(required=True)
    img_type_group: argparse._MutuallyExclusiveGroup = group_2.add_mutually_exclusive_group(required=True)

    input_type_group.add_argument("-i", metavar="INPUT_FILE", help="accepts only one input file from specified file path")
    input_type_group.add_argument("-d", metavar="INPUT_DIRECTORY", help="accepts multiple input file from specified directory path")

    img_type_group.add_argument("-j", "--JPEG", help="converts the input image file to JPEG/JPG format", action="store_true")
    img_type_group.add_argument("-p", "--PNG", help="converts the input image file to PNG format", action="store_true")
    img_type_group.add_argument("-s", "--SVG", help="converts the input image file to SVG format", action="store_true")
    img_type_group.add_argument("-w", "--WEBP", help="converts the input image file to WEBP format", action="store_true")

    group_3.add_argument("-o", metavar="OUTPUT_DESTINATION", help="specifies the output file path inclusive of the file's name")

    return argument_parser


def run_single_conversion_task(args_: argparse.Namespace, input_: str, output_: str) -> None:
    pass 


def run_multiple_conversion_task(args_: argparse.Namespace, iterator_: Iterator[str], output_: str) -> None: 
    pass 


def selected_type(argg: argparse.Namespace) -> str:
    if argg.JPEG: 
        return ".jpg"
    if argg.PNG: 
        return ".png"
    if argg.SVG: 
        return ".svg"
    if argg.WEBP: 
        return ".webp"


# parsing output name: 
def name_with_exten(argument: argparse.Namespace, name:str) -> str:
    for element in name.split('.'): 
        if element.upper()  in {"JPEG", "JPG", "PNG", "WEBP", "SVG"}: 
            return name 
    name += selected_type(argument)
    return name 
# end of function 


def return_seperator(string: str) -> str|None: 
    if string.find('/') != -1: 
        return '/'
    elif string.find('\\') != -1: 
        return '\\'
    return None # if the string has no seperator  


def is_a_valid_imagefile(name: str) -> bool: 
    if (name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png") 
        or name.endswith(".svg") or name.endswith(".webp")): 
        return True 
    return False


def parse_output_file_path(arg: argparse.Namespace) -> str|None:
    raw_ : str = arg.o # output  
    sep_ : str = return_seperator(raw_)
    # writing code to check if the file path seperator (based on the platform) is present in the output: 
    if not sep_:
        return os.path.join(os.getcwd(), name_with_exten(arg, raw_))
    
    components: str = raw_.split(sep_)
    if is_a_valid_imagefile(components[-1]) and os.path.exists(str.join(sep_, components[0:len(components)-2])): 
        return raw_
    
    raise WrongOutputException # wrong output 
    

def custom_output_file_path(a_0x0:argparse.Namespace, in_path: str) -> str: 
    sep_ : str = return_seperator(in_path)
    output_name: str = in_path
    if sep_: 
        output_name = in_path.split(sep_)[-1] # name + extension
    output_name = output_name.split('.')[0]
    return os.path.join(os.getcwd(), (output_name+selected_type(a_0x0)))


def parse_output_directory_path(arg: argparse.Namespace) -> str|None: 
    raw_ : str = arg.o 
    sep_ : str = return_seperator(raw_)
    # continue from here:
    



def supported_file_input_iterator(input_: str) -> Iterator[str]: 
    for entity in os.listdir(input_):
        if os.path.isfile(os.path.join(input_, entity)) and is_a_valid_imagefile(entity):
            yield entity 


# main function of this program
def run_program(parser: argparse.ArgumentParser) -> None: 
    input_path: str = None 
    output_path: str = None 

    screen.welcome_screen() # displaying the welcome screen
    args_namespace = parser.parse_args()

    # single input file
    if args_namespace.i: 
        _file: str = args_namespace.i
       # some code comes here first:
        if os.path.exists(_file) and os.path.isfile(_file):# parse input file path 
            file_name, file_exten = tuple(os.path.basename(_file).split('.'))
            if not file_exten.upper() in {"JPEG", "JPG", "PNG", "WEBP", "SVG"}: 
                screen.error_message_display(INVALID_INPUT_ERROR)
                return
            input_path = _file  # path is valid and leads to a media (image) file  
        else: 
            screen.error_message_display("")
            return
        if args_namespace.o:# parse output/destination path 
           try: 
               output_path = parse_output_file_path(args_namespace)
           except WrongOutputException: 
               screen.error_message_display(INVALID_OUTPUT_ERROR)       
        else: 
            output_path = custom_output_file_path(args_namespace, input_path) # return custom output path 
        
        run_single_conversion_task(args_namespace, input_path, output_path)

    # multiple input files          
    if args_namespace.d:  
        _path: str = args_namespace.d
        if not (os.path.exists(_path) and os.path.isdir(_path)): # input path is exists and if it is a directory 
           screen.error_message_display("")
           return
        valid_input_terator: Iterator[str] = supported_file_input_iterator(_path)
        if args_namespace.o: 
            pass

        run_multiple_conversion_task(args_namespace, valid_input_terator)


if __name__ ==  "__main__": 

    run_program(parser_initialiser())
    exit("Exited sucessfully!")

# end of program 