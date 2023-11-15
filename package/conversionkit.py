import os 
import pathlib 
from PIL import Image 
from cairosvg import svg2png
import screen 
from supported_formats import ImgFormats



# code starts here 
# class that represents the given file entity: 
class ImageTransformer(): 
    
    def __init__(self, input_path: str, output_path: str): 
        self.input_path: str = input_path
        self.output_path: str = output_path 


    def jpeg_to_(self, conversion_type: ImgFormats) -> bool:
        try:
            if conversion_type.name == ImgFormats.PNG.name: 
                image_object = Image.open(self.input_path).convert("RGBA")
                image_object.save(self.output_path, "PNG")

            elif conversion_type.name == ImgFormats.WEBP.name: 
                image_object = Image.open(self.input_path).convert("RGB")
                image_object.save(self.output_path, "WEBP")

            elif conversion_type.name == ImgFormats.SVG.name: 
                self.__convert_raster_to_svg_()

            return True
        except: 
            return False 


    def png_to_(self, conversion_type: ImgFormats) -> None: 
        if conversion_type.name == ImgFormats.JPEG.name: 
            pass 

        elif conversion_type.name == ImgFormats.WEBP.name: 
            pass 

        elif conversion_type.name == ImgFormats.SVG.name: 
            pass 

        else: 
            pass


    def webp_to_(self, conversion_type: ImgFormats) -> None: 
        if conversion_type.name == ImgFormats.JPEG.name: 
            pass 

        elif conversion_type.name == ImgFormats.PNG.name: 
            pass 

        elif conversion_type.name == ImgFormats.SVG.name:
            pass 

        else: 
            pass 
        

    def svg_to_(self, conversion_type: ImgFormats) -> None: 
        if conversion_type.name == ImgFormats.PNG.name: 
            pass 

        elif conversion_type.name == ImgFormats.JPEG.name: 
            pass 

        elif conversion_type.name == ImgFormats.WEBP.name: 
            pass

        else:
            pass 


# method to convert raster images to vector images
    def __convert_raster_to_svg_(self, input_path: str, output_path: str): 
        pass




# end of class implementation 



if __name__ == "__main__": 
    module_version: str = "1.0.0"
    print(f"Name: conversionkit.py \nVersion: {module_version}\nFile Path: {__file__}")

# end of program 