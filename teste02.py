import time
import pyautogui
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

time.sleep(3)
imagem = pyautogui.screenshot(region = (57, 944, 368, 50))
texto = pytesseract.image_to_string(imagem)
print(texto)
imagem.save('captura.png')
