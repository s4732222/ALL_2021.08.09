import pywinauto
import time
import pynput

app = pywinauto.application.Application()

app.start("C:/Program Files/ArcGIS/Pro/bin/ArcGISPro.exe")


time.sleep(5)

print("ιεGISζε")

ctr = pynput.keyboard.Controller()

with ctr.pressed(
    pynput.keyboard.KeyCode.from_vk(17),
    'o'):pass

time.sleep(5)