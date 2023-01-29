# Write your code here :-)
from adafruit_circuitplayground import cp
import time

    cp.pixels.fill((50, 0, 0))

while True:
    cp.pixels.brightness = 0.3
    print ("Neopixel On")
    time.sleep(0.5)
    cp.pixels.brightness = 0
    print ("Neopixel Off")
