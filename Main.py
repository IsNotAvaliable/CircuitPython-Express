# Write your code here :-)
from adafruit_circuitplayground import cp
import time

    cp.pixels.fill((50, 0, 0))
    cp.pixels.brightness = 0.3
    minimum_temp = 24
maximum_temp = 30
def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)
    
while True:
     peak = scale_range(cp.temperature)
        
    if cp.shake(shake_threshold=20):
        cp.pixels.fill((255, 0, 0))
        cp.pixels.show()
         print ("Shaking")
            time.sleep(0.2)
            print ("Not Shaking")
elif cp.loud_sound(sound_threshold=250):
    cp.pixels.fill((255, 0, 0))
    cp.pixels.show()
    print ("LOUD")
        time.sleep(0.2)
        print ("SHUT")
        elif cp.light > 10: 
               cp.pixels.fill((255, 0, 0))
    cp.pixels.show()
    print ("BRIGHT")
        time.sleep(0.2)
        print ("Dark")
        elif cp.temperature > 24:
            cp.pixels.fill((255, 0, 0))
    cp.pixels.show()
    print ("Hot")
        time.sleep(0.2)
        print ("Cold")
            
