# Passo a passo o projeto
# Passo 1:Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")    
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=918, y=373)
pyautogui.write("paulorodribeiro@gmail.com")

# escrever a senha

pyautogui.press("tab")
pyautogui.write("336356ig")

# clicar no botão de logar
pyautogui.click(x=1014, y=488)
time.sleep(3)


# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")  


# Passo 4: Cadastrar 1 produto 
# para cada linha da minha tabela
for linha in tabela.index:


    # Clicar no 1º campo
    pyautogui.click(x=883, y=276)

    # código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
 
# Passo 5: Repetir o processo de cadastro até acabar a base de dados
