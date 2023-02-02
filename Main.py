# Write your code here :-)
import time
from adafruit_circuitplayground import cp
def buttons():
    if cp.button_b:
        cp.play_tone(500, 1)
    if cp.button_a:
        cp.play_tone(100, 1)
def BRIGHT():
    if cp.light >= 50:
        cp.pixels[0] = (255, 0, 0)
        cp.pixels[1] = (255, 0, 0)
        cp.pixels[8] = (255, 0, 0)
        cp.pixels[9] = (255, 0, 0)
        print("Light:", cp.light)
        print((cp.light,))
        time.sleep(0.2)
        
    elif cp.light <= 49:
        cp.pixels[0] = (0, 0, 0)
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)
        cp.pixels[9] = (0, 0, 0)
        print("Light:", cp.light)
        print((cp.light,))
        time.sleep(0.2)
        
while True:
    buttons()
    BRIGHT()
