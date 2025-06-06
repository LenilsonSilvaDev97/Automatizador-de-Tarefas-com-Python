import pyautogui
import time
pyautogui.PAUSE = 0.5

#pyautogui -> fazer automação com Python 

# pyautogui.click -> clicar em um lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

#começar escrevendo em portugues o passo a posso do codigo
# Passo 1: entrar no sistea da empresa:https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")    

# Passo 2: Login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espear 3 segundos

time.sleep(3)

pyautogui.click(x=718, y=560)
pyautogui.write("testandopyautogui@gmail.com")

# Preencher a senha

pyautogui.press("tab")
pyautogui.write("senhadificil")

# Botão logar

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)    

# Passo 3: importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print (tabela)

# passo 4: Cadastrar os produtos
for linha in tabela.index: #para cada linha da minha tabela
    pyautogui.click(x=615, y=392)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
   
    if obs!= "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)


# Passo 5: Repetir todos os passos 

    
 