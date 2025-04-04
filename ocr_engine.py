from PIL import Image
import cv2
import numpy as np
import easyocr

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def extract_text(image_path):
    reader = easyocr.Reader(['en'])  # Chỉ định ngôn ngữ, có thể thêm 'vi' nếu cần tiếng Việt
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)
