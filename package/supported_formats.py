# simple enum class containing the supported image formats: 
from enum import Enum 

# enum class
class ImgFormats(Enum): 
    JPEG: str = 0 
    PNG: str  = 1
    SVG: str = 2 
    WEBP: str = 3

# end of enum class implementation 

if __name__ == "__main__": 
    module_version: str = "1.0.0"
    print(f"Name: supported_formats.py \nVersion: {module_version}\nFile Path: {__file__}")