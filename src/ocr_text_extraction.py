
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Set path to tesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Load image using OpenCV
image_path = '../images/sample_text_image.png'
img_cv = cv2.imread(image_path)

# Convert to RGB
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img_rgb)
print("🔍 Extracted Text:\n", text)
