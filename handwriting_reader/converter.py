from PIL import Image
import pytesseract
class Converter:
    def convert(self, data)->str:
        if isinstance(data, Image):
            return self.convert_image(data)
        
        return "Unsupported data type"
    
    def convert_image(self, data: Image)->str:
        return pytesseract.image_to_string(data)