#Passo a passo
#Passo 1: Abrir o navegador 
#Passo 2: Pesquisar o site 
#Passo 3: Fazer login
#Passo 4: Registrar primeiro produto
#Passo 5: Registrar demais produtos 

#Comandos importantes 
#pyautogui.write -> escrever um texto 
#pyautogui.press-> apertar uma tecla
#pyautogui.click ->  clicar em algum lugar da tela 
#pyautogui.hotkey -> combinação de teclas



import pyautogui 
import time 

pyautogui.PAUSE = 0.3

#PASSO 1
pyautogui.press ("win")
time.sleep (5)
pyautogui.write ("navegador opera GX")
time.sleep (45)
pyautogui.press ("enter")
time.sleep (20)

#PASSO 2
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep (20)

#PASSO 3 
pyautogui.click (x=462, y=364)
pyautogui.write ("ana.paula.vila.borba@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("senhamood")
pyautogui.click (x=716, y=527)
time.sleep (10)

#PASSO 4
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click (x=559, y=244)

    codigo = tabela.loc [linha, "codigo"]
    pyautogui.write (str(codigo))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "tipo"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "categoria"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press ("tab")
    obs = str (tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write (obs)

    pyautogui.press ("enter")
    
    pyautogui.scroll (5000)





