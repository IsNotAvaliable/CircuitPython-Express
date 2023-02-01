# Write your code here :-)
from adafruit_circuitplayground import cp
import time

    cp.pixels.fill((50, 0, 0))
    cp.pixels.brightness = 0.3
while True:
    
    if cp.shake(shake_threshold=20):
        cp.pixels[0] = (255, 0, 0)
         print ("Shaking")
        else
        cp.pixels[0] = (0, 0, 0)
         print ("Not Shaking")
