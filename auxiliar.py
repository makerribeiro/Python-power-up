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

pyautogui.click(x=918, y=373)
pyautogui.write("paulorodribeiro@gmail.com")

# escrever a senha

pyautogui.press("tab")
pyautogui.write("336356ig")

# clicar no botão de logar
pyautogui.click(x=1014, y=488)
time.sleep(3)



print(pyautogui.position())

