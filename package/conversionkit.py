import os 
import pathlib 
from base64 import b64encode 
from PIL import Image 
from cairosvg import svg2png
from package.supported_formats import ImgFormats
from package import screen



# code starts here 
# class that represents the given file entity: 
class ImageTransformer(): 
    
    def __init__(self, input_path: str | None = None, output_path: str | None = None): 
        self.input_path: str = input_path
        self.output_path: str = output_path 


    def to_JPEG_(self, input_type: ImgFormats) -> bool:
        try:
            if input_type.name == ImgFormats.PNG.name: 
                image_object = Image.open(self.input_path).convert("RGB") # Converting from RGBA to RGB
                image_object.save(self.output_path, "JPEG")

            elif input_type.name == ImgFormats.WEBP.name: 
                image_object = Image.open(self.input_path) # webp is already in RGB. No conversion required.
                image_object.save(self.output_path, "JPEG")

            elif input_type.name == ImgFormats.SVG.name: 
                pass
            return True
        except: 
            return False


    def to_PNG_(self, input_type: ImgFormats) -> bool: 
        try:
            if input_type.name == ImgFormats.JPEG.name or input_type.name == ImgFormats.JPG.name or input_type.name == ImgFormats.WEBP.name: 
                image_object = Image.open(self.input_path).convert("RGBA")
                image_object.save(self.output_path, "PNG")

            else: # SVG Format 
                pass 
            return True
        except: 
            return False


    def to_WEBP_(self, input_type: ImgFormats) -> bool: 
        try:
            if input_type.name == ImgFormats.JPEG.name or input_type.name == ImgFormats.JPG.name: 
                image_object = Image.open(self.input_path)
                image_object.save(self.output_path, "WEBP")

            elif input_type.name == ImgFormats.PNG.name: 
                image_object = Image.open(self.input_path).convert("RGB") #WEBP is based on the RGB color space
                image_object.save(self.output_path, "WEBP")

            elif input_type.name == ImgFormats.SVG.name:
                pass
            return True
        except: 
            return False
        

    def to_SVG_(self, input_type: ImgFormats) -> bool: 
        try:
            if input_type.name == ImgFormats.PNG.name: 
                self.__convert_raster_to_svg_(input_type.PNG.name.lower())

            elif input_type.name == ImgFormats.JPEG.name or input_type.name == ImgFormats.JPG.name: 
                self.__convert_raster_to_svg_(input_type.JPEG.name.lower())

            elif input_type.name == ImgFormats.WEBP.name: 
                self.__convert_raster_to_svg_(input_type.WEBP.name.lower())
            return True
        except: 
            return False


# method to convert raster images to vector images
    def __convert_raster_to_svg_(self, image_format: str): 
        with open(self.input_path, "rb") as file:
            base_64: bytes = b64encode(file.read()) # reading binary content into byte string

        base_64_str: str = base_64.decode("utf-8") # decode bytes to str
        
        # Image properties
        img_obj = Image.open(self.input_path)
        width, height = img_obj.size # returning image dimension in the format(width, height)

        SVG_CODE: str = f"""<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{width}px" height="{height}px" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <image xlink:href="data:image/{image_format};charset=utf-8;base64,{base_64_str}" height="{height}px"  width="{width}px"/>
</svg>
"""     # writing the svg content to a file: 
        with open(self.output_path, "w") as file:
            file.write(SVG_CODE) # creating a file and writing SVG content to the file



# end of class implementation 



if __name__ == "__main__": 
    module_version: str = "1.0.0"
    print(f"Name: conversionkit.py \nVersion: {module_version}\nFile Path: {__file__}")


# end of program 