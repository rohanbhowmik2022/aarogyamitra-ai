import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Configure Tesseract executable path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extract text from an image file using Tesseract OCR.
    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error processing image: {e}"

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file by converting pages to images and using Tesseract OCR.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    try:
        pages = convert_from_path(pdf_path)
        text = ""
        for page_number, page in enumerate(pages, start=1):
            temp_image_path = f"temp_page_{page_number}.jpg"
            page.save(temp_image_path, "JPEG")
            text += extract_text_from_image(temp_image_path) + "\n"
            os.remove(temp_image_path)  # Clean up temporary image file
        return text
    except Exception as e:
        return f"Error processing PDF: {e}"

if __name__ == "__main__":
    file_path = input("Enter the path to the image or PDF file: ").strip()
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        print("Extracting text from image...")
        print(extract_text_from_image(file_path))
    elif file_path.lower().endswith('.pdf'):
        print("Extracting text from PDF...")
        print(extract_text_from_pdf(file_path))
    else:
        print("Unsupported file format. Please provide an image or PDF file.")