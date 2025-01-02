from PIL import Image
import pytesseract

class Converter:
    def convert(self, data)->str:
        if isinstance(data, Image.Image):
            return self.convert_image(data)
        
        return "Unsupported data type"
    
    def convert_image(self, data: Image)->str:
        return pytesseract.image_to_string(data)
    

if __name__ == "__main__":
    converter = Converter()
    path = "test/test_image.jpg"
    print(converter.convert(Image.open(path)))