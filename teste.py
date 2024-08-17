import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Coordenadas do pixel: ({x}, {y})")