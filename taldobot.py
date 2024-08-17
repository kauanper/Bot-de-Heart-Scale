import pyautogui
import time
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def capturar_extrair_texto(x, y, largura, altura):  #printa a area e transforma em texto
    imagem = pyautogui.screenshot(region = (x, y, largura, altura)) 
    texto = pytesseract.image_to_string(imagem)
    return texto

time.sleep(5)

while True:

    achou = 0

    #curar o pokemon e voltar até a agua
    pyautogui.keyDown('z')
    time.sleep(7)
    pyautogui.keyUp('z')
    
    time.sleep(0.5)
            
    for i in range (10):
        if i != 5:
            pyautogui.keyDown('k')
            time.sleep(0.02)
            pyautogui.keyUp('k')
            time.sleep(0.5)
        else:
            pyautogui.keyDown('k')
            time.sleep(0.02)
            pyautogui.keyUp('k')
            time.sleep(3)
            
    time.sleep(1)
    for i in range (8):
        pyautogui.keyDown('j')
        time.sleep(0.02)
        pyautogui.keyUp('j')
        time.sleep(0.5)
        
    time.sleep(1)
    for i in range (4):
        pyautogui.keyDown('k')
        time.sleep(0.02)
        pyautogui.keyUp('k')
        time.sleep(0.5)
        
    time.sleep(0.5)
        
    #quando ele ta perto da agua
    while True:
        
        if achou == 38:
            pyautogui.keyDown('8')
            time.sleep(0.1)
            pyautogui.keyUp('8')
            
            time.sleep(5)
            break
    
        pyautogui.press('4')
        time.sleep(4)

        texto = capturar_extrair_texto(557, 140, 50, 30) #mensagem da pesca

        time.sleep(1)
            
        if 'Not' not in texto: #achou bixo
            pyautogui.keyDown('z')
            time.sleep(0.5)
            pyautogui.keyUp('z')
            time.sleep(12)
            
            #   pyautogui.click(380, 858) # abrir chat
            
            texto3 = capturar_extrair_texto(57, 944, 368, 50) #frisk
            time.sleep(3)
                   
            if "revistou" not in texto3: #checar 
                pyautogui.keyDown('k')
                time.sleep(0.2) 
                pyautogui.keyUp('k')
                time.sleep(0.2)
                pyautogui.keyDown('l') 
                time.sleep(0.2)
                pyautogui.keyUp('l')
                time.sleep(0.2)
                pyautogui.keyDown('z') 
                time.sleep(0.2)
                pyautogui.keyUp('z')
                time.sleep(2) #sair da batalha
            else:
            
                #pyautogui.click(396, 688) # colocar a seta no lutar
                
                pyautogui.keyDown('i') #lutar   
                time.sleep(0.1)
                pyautogui.keyUp('i')
                time.sleep(0.1)
                pyautogui.keyDown('z') #apertar  
                time.sleep(0.1)
                pyautogui.keyUp('z')                             
                time.sleep(0.5)
                pyautogui.keyDown('z') #thief
                time.sleep(0.1)
                pyautogui.keyUp('z')
                time.sleep(11)   #animaçao do golpe
                #   pyautogui.click(1852, 418) 
                                                        
                time.sleep(0.5)
                pyautogui.click(1891, 424) #clica no pokemon
                time.sleep(0.7)
                      
                for i in range(2): #desce ate o item
                    pyautogui.keyDown('k')
                    time.sleep(0.2)
                    pyautogui.keyUp('k')
                    time.sleep(0.5)
                    
                pyautogui.press('z') #pegar o item
                time.sleep(1.2)
                    
                
                achou+=1
                                    
        else:
            pyautogui.press('z')
            time.sleep(1)   