from time import time, sleep
import numpy as np
import board
import sounddevice as sd
import neopixel
import config

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print (current_time + " - TALKLIGHT STARTED")

# SCRIPT
pixels = neopixel.NeoPixel(config.LED_PIN, config.LED_COUNT, brightness=config.LED_BRIGHTNESS)
pixels.fill(config.COLOR_OFF)

def led_status(volume):
    if volume > config.THRESHOLD and config.STATUS == False:
        pixels.fill(config.COLOR_ON)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print (current_time + " - TALKLIGHT ON")
        config.STATUS = True
        sleep(config.SLEEP - time() % config.SLEEP)
    elif config.STATUS == True:
        pixels.fill(config.COLOR_OFF)
        config.STATUS = False
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print (current_time + " - TALKLIGHT OFF")

def print_sound(indata, outdata, frames, time, status):
    # volume_norm = np.linalg.norm(indata)*10
    volume_norm = np.linalg.norm(indata)*1000
    led_status(int(volume_norm))
    # print ("|" * int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(100 * config.RATE)
