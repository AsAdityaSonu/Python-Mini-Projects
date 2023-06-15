import pytesseract
import os
from PIL import Image

def image_to_text(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)

# path to your image
image_path = r"Mini_Project 11\test.png"
# or image_path = "Mini_Project 11\\test.png"
image_to_text(image_path)

if not os.path.exists(image_path):
    print("File does not exist:", image_path)
    exit(1)
