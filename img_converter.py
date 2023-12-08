# !/usr/bin/python3

###############################################################################################################################
# Programmer.name = Nelson Chidi                                                                                              #
# Programmer.nick_name = Nelmatrix                                                                                            #
# Programmer.GitHub.username = NelMatrix743                                                                                   #
# Programmer.GitHub.url = https://github.com/NelMatrix743                                                                     #
# source_code.version = 1.0.0                                                                                                 #
#                                                                                                                             #
###############################################################################################################################

# The main module of the image converter program
import argparse 
import os 
import pathlib
import time
import colorama
from collections.abc import Iterator 
from package import screen, conversionkit, supported_formats



# simple exception class 
class PathDoesNotExistsException(Exception): 
    pass


PROG_DESCRIPTION: str = """This is a simple command line utility to convert images from one format to another. 
                        Supported image formats are: JPEG, PNG, SVG, && WEBP.
                        """
EXIT_MESSAGE: str = """ This is a simple exit message"""

#=============================================================== ERROR MESSAGES ================================================================================#
NOT_A_PATH_TO_A_FILE_ERROR: str = """ERROR! The pathname you entered leads to a directory.\nUse the (-d) option if you want to process files in a directory."""

NOT_A_SUPPORTED_FILE_INPUT_ERROR: str = "ERROR! This file is not supported. Conversion cannot take place.\nPlease enter the pathname of a valid image file."

INPUT_PATH_DOES_NOT_EXISTS_ERROR: str = "ERROR! The pathname you entered does not exists on your system. Please enter a valid pathname."

PATH_IS_NOT_A_DIRECTORY_OR_DOES_NOT_EXISTS_ERROR: str = "ERROR! The pathname you entered does not represent a directory or it does not exists on your system."

OUTPUT_PATH_DOES_NOT_EXISTS_ERROR: str = "ERROR! The output pathname you provided does not exist."

OUTPUT_DIRECTORY_PATH_DOES_NOT_EXISTS_ERROR: str = "ERROR! The output pathname you provided is invalid, or it does not exists on your system." 
#===============================================================================================================================================================#


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

    group_3.add_argument("-o", metavar="OUTPUT_DESTINATION", help="specifies the output absolute-path (use output file name for single input)")

    return argument_parser


def input_image_type(file_name: str): 
    file_extension: str = file_name.split('.')[-1]
    
    if file_extension == "jpeg" or file_extension == "jpg":
        return supported_formats.ImgFormats.JPEG
    
    if file_extension == "png": 
        return supported_formats.ImgFormats.PNG
    
    if file_extension == "webp":
        return supported_formats.ImgFormats.WEBP
    
    if file_extension == "svg": 
        return supported_formats.ImgFormats.SVG



# convert a single input image file to the specified output image format;
def run_single_conversion_task(args_: argparse.Namespace, input_: str, output_: str) -> None:

    img_object: conversionkit.ImageTransformer = conversionkit.ImageTransformer(input_, output_)
    format_: supported_formats.ImgFormats = input_image_type(os.path.basename(input_)) 
    conversion_sucessful: bool
    screen.in_process_message_display("\n [*] Loading input file ...............%\n\n")
    time.sleep(0.7) # sleep for 0.7 seconds
    screen.success_message_display(f"[+] INPUT :: {input_}\n")
    screen.success_message_display(f"[+] OUTPUT:: {output_}\n\n")
    screen.in_process_message_display("[*] File conversion in progress............%\n\n")
    if args_.JPEG: 
        conversion_sucessful = img_object.to_JPEG_(format_)
    elif args_.PNG: 
        conversion_sucessful = img_object.to_PNG_(format_)
    elif args_.WEBP: 
        conversion_sucessful = img_object.to_WEBP_(format_)
    elif args_.SVG: 
        conversion_sucessful = img_object.to_SVG_(format_)
    
    if conversion_sucessful:
        screen.success_message_display("File conversion successful! Output file has been written to disk.\n")
        return
    screen.error_message_display("File conversion failure! Cannot convert file.\n")
    

# convert multiple input image file to the speciied output image format;
def run_multiple_conversion_task(args_: argparse.Namespace, iterator_: Iterator[str], output_: str) -> None: 
    img_object: conversionkit.ImageTransformer = conversionkit.ImageTransformer()
    conversion_sucessful: bool
    for each_file in iterator_: 

        img_object.input_path = each_file
        base_name: str = os.path.basename(each_file)
        file_name:str = base_name.split('.')[0]
        file_extension: str = base_name.split('.')[-1]

        format_: supported_formats.ImgFormats = input_image_type(base_name)
        if args_.JPEG:
            if file_extension == "jpeg" or file_extension == "jpg":
                continue
            img_object.output_path = os.path.join(output_, (file_name + ".jpg"))
            conversion_sucessful = img_object.to_JPEG_(format_)
        elif args_.PNG:
            if file_extension == "png": 
                continue
            img_object.output_path = os.path.join(output_, (file_name + ".png"))
            conversion_sucessful = img_object.to_PNG_(format_)
        elif args_.WEBP:
            if file_extension == "webp": 
                continue
            img_object.output_path = os.path.join(output_, (file_name + ".webp"))
            conversion_sucessful = img_object.to_WEBP_(format_)
        elif args_.SVG:
            if file_extension == "svg":
                continue
            img_object.output_path = os.path.join(output_, (file_name + ".svg"))
            conversion_sucessful = img_object.to_SVG_(format_)



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
    if (name.split('.'))[-1].upper()  in {"JPEG", "JPG", "PNG", "WEBP", "SVG"}: 
            return name 
    name += selected_type(argument)  # append the extension to the file name, regardless;
    return name 
# end of function 


def return_seperator(string: str) -> str | None: 
    if '/' in string: 
        return '/'
    if '\\' in string: # using double backslashes to escape backslash escape sequence error; 
        return '\\'
    return None # if the string has no seperator  


def is_a_valid_imagefile(name: str) -> bool: 
    if (name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png") 
        or name.endswith(".svg") or name.endswith(".webp")): 
        return True 
    return False


def parse_output_file_path(arg: argparse.Namespace) -> str | None:
    raw_ : str = arg.o # output;
    refined_ : str = os.path.realpath(raw_) # to refine the provided pathname for further processing;
    sep_ : str | None = return_seperator(refined_)

    components: list[str] = refined_.split(sep_)
    pre_output_file_name: str = components.pop(-1) # remove and store filename because it is does not exist yet;
    
    if os.path.exists(str.join(sep_, components)):
        components.append(name_with_exten(arg, pre_output_file_name))
        return str.join(sep_, components)  # return the final pathname result;

    raise PathDoesNotExistsException # wrong output;
    

def custom_output_file_path(a_0x0:argparse.Namespace, in_path: str) -> str: 
    sep_ : str | None = return_seperator(in_path)
    output_name: str = in_path
    if sep_: 
        output_name = in_path.split(sep_)[-1] # name + extension;
    output_name = output_name.split('.')[0]
    return os.path.join(os.getcwd(), (output_name+selected_type(a_0x0)))



def parse_output_directory_path(output_dir_: argparse.Namespace) -> str | None: 
    raw_ : str = output_dir_.o 
    raw_ = os.path.realpath(raw_) # refining the output;    

     # check if the specified output path exists and if it is a directory:
    if os.path.exists(raw_) and os.path.isdir(raw_):
        return raw_
    else:  # input directory path does not exists;
        return None
    
    

def supported_file_input_iterator(input_: str) -> Iterator[str]: 
    realpath = os.path.realpath(input_)
    for entity in os.listdir(realpath):
        if os.path.isfile(os.path.join(realpath, entity)) and is_a_valid_imagefile(entity):
            yield os.path.join(realpath, entity) 


# main function of this program;
def run_program(parser: argparse.ArgumentParser) -> None: 
    screen.welcome_screen() # display the welcome screen;
    print('\n', end='') # move a line below;

    input_path: str | None = None 
    output_path: str | None = None 

    args_namespace: argparse.Namespace = parser.parse_args() # instantiating argument namespace;

    # SINGLE INPUT FILE (file mode); 
    if args_namespace.i: 
        _file: str = args_namespace.i

        if os.path.exists(_file):
            if os.path.isfile(_file):
                file_name, file_exten = os.path.basename(_file).split('.')
                if not file_exten.upper() in {"JPEG", "PNG", "JPG", "WEBP", "SVG"}: 
                    screen.error_message_display(NOT_A_SUPPORTED_FILE_INPUT_ERROR) # file is not an image, or it a wrong image file format;
                    return
                input_path = _file  # path is valid and leads to a supported image file;  
                
            else: # if the pathname leads to a directory instead of a file;
                screen.error_message_display(NOT_A_PATH_TO_A_FILE_ERROR) 
                return
        else: # path does not exists;
            screen.error_message_display(INPUT_PATH_DOES_NOT_EXISTS_ERROR)
            return
        
        if args_namespace.o:  # parse output/destination path;
           try: 
               output_path = parse_output_file_path(args_namespace)
           except PathDoesNotExistsException: 
               screen.error_message_display(OUTPUT_PATH_DOES_NOT_EXISTS_ERROR)  
               return
        else: 
            output_path = custom_output_file_path(args_namespace, input_path) # return custom output path; 
        run_single_conversion_task(args_namespace, input_path, output_path)
        return # terminate the function;


    # MULTIPLE INPUT FILES (directory mode);
    if args_namespace.d:  
        in_path: str = args_namespace.d
        if not (os.path.exists(in_path) and os.path.isdir(in_path)):
           screen.error_message_display(PATH_IS_NOT_A_DIRECTORY_OR_DOES_NOT_EXISTS_ERROR)
           return
        valid_input_iterator: Iterator[str] = supported_file_input_iterator(in_path)

        if args_namespace.o:
            # parse output directory for storing converted image files;
            output_path = parse_output_directory_path(args_namespace)
            if not output_path:
                screen.error_message_display(OUTPUT_DIRECTORY_PATH_DOES_NOT_EXISTS_ERROR)
                return
            
        else: # if user did not specify output directory:
            output_path = os.path.join(os.getcwd(), "OUTPUT-DIRECTORY")
            if not os.path.exists(output_path):
                os.mkdir(output_path) # create the output directory
        
        run_multiple_conversion_task(args_namespace, valid_input_iterator, output_path)
        return # terminate the function;



if __name__ ==  "__main__": 

    # initialising colorama to enable console color formatting especially on MS-DOS Windows cmd.exe application
    colorama.init() 

    # run main function;
    run_program(parser_initialiser())

    print("\n\n", end='') # move two lines below;
# end of program;