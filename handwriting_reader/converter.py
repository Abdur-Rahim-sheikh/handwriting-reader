from io import BytesIO
from PIL import Image
import pytesseract
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Converter:
    def convert(self, content: BytesIO)->str:

        try:
            data = Image.open(content)
            return self.convert_image(data)
        except Exception as e:
            logger.error(f"Error in converting image: {e}")
        
        return "Unsupported data type"
    
    def convert_image(self, data: Image)->str:
        return pytesseract.image_to_string(data)
    

if __name__ == "__main__":
    converter = Converter()
    path = "test/test_image.jpg"
    with open(path, "rb") as f:
        content = BytesIO(f.read())
    print(converter.convert(content))