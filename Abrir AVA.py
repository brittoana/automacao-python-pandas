import pyautogui # type: ignore
import time

#PASSO 1:abrir o navegador 
#PASSO 2:buscar link
#PASSO 3:fazer login

#PASSO 1 
pyautogui.press ("win")
time.sleep (3)
pyautogui.write ("Chrome")
time.sleep (5)
pyautogui.press ("enter")
time.sleep (3)
pyautogui.click (x=677, y=668)
time.sleep (2)

#PASSO 2
pyautogui.write ("ava.catolica.edu.br")
pyautogui.press ("enter")
time.sleep (10)
pyautogui.click (x=1014, y=344)
time.sleep (5)
pyautogui.click (x=1019, y=596)
time.sleep (2)
pyautogui.click (x=1096, y=613)
time.sleep (2)
pyautogui.click (x=1010, y=463)
time.sleep (15)
pyautogui.click (x=1086, y=675)



