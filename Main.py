# Write your code here :-)
import time
from adafruit_circuitplayground import cp
def buttons():
    if cp.button_b:
        cp.play_tone(294, 1)
    if cp.button_a:
        cp.play_tone(262, 1)
    if cp.button_ab:
        cp.play_tone(150, 3)
while True:
    buttons()
