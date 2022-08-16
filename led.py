import config
import neopixel
import sys

pixels = neopixel.NeoPixel(config.LED_PIN, config.LED_COUNT, brightness=config.LED_BRIGHTNESS, auto_write=True)

def led_on():
    pixels.fill(config.COLOR_ON)

def led_off():
    pixels.fill(config.COLOR_OFF)

if len(sys.argv) > 1 and sys.argv[1] == "on":
    led_on()
elif len(sys.argv) < 1 and sys.argv[1] == "off":
    led_off()
else:
    led_off()

