import numpy
import time 
import pyautogui
import webbrowser

numero_telefono = '57 321 9963163'

msm = open('./mensaje.txt')

mensaje = []
for i in msm:
    if i != '\n':
        mensaje.append(i)

print(len(mensaje))

n = numpy.random.randint(0, 83)

url = 'https://web.whatsapp.com/send?phone='

webbrowser.open(url + numero_telefono)
time.sleep(10)
pyautogui.write(mensaje[n])
pyautogui.press('Enter')
