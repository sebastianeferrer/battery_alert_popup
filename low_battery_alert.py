#!/usr/bin/env python3
from easygui import msgbox
from time import sleep
import psutil

low_battery_msg = 'Bateria {}% ¡Cargar ahora!'
sample_rate_s = 60
image = "low_battery.png"
battery = psutil.sensors_battery()

while not battery.power_plugged: 
    msgbox(low_battery_msg.format(round(battery.percent)), image=image)
    sleep(sample_rate_s)
    battery = psutil.sensors_battery()


