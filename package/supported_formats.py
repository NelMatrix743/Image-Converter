# simple enum class containing the supported image formats: 
from enum import Enum 

# enum class
class ImgFormats(Enum): 
    JPEG: str = 0 
    PNG: str  = 1
    SVG: str = 2 
    WEBP: str = 3

# end of enum class implementation 