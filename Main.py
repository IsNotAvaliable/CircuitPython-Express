# Write your code here :-)
import digitalio
import board

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
print("The LED is now on!")
time.sleep(5)
