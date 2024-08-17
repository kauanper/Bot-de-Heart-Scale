import pyautogui
import time
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def capturar_extrair_texto(x, y, largura, altura):  #printa a area e transforma em texto
    imagem = pyautogui.screenshot(region = (x, y, largura, altura)) 
    texto = pytesseract.image_to_string(imagem)
    
time.sleep(5)    
    
while True:
        
        pyautogui.press('4')
        time.sleep(5)
    
        texto = capturar_extrair_texto(557, 140, 50, 30) #mensagem da pesca

        time.sleep(1)
        
        if 'not' not in texto: #achou bixo
            pyautogui.keyDown('z')
            time.sleep(1)
            pyautogui.keyUp('z')
            time.sleep(11)
            
            pyautogui.keyDown('z')
            time.sleep(1)
            pyautogui.keyUp('z')
            
            pyautogui.keyDown('z')
            time.sleep(1)
            pyautogui.keyUp('z')
            time.sleep(6)
        
        time.sleep(1)    
            
        pyautogui.click(1891, 424) #clica no pokemon
        
        time.sleep(1)
        
        texto = capturar_extrair_texto(1750, 474, 30, 25) #opção do pokemon (checar se tem item ou nao)
        break
    
    
    
