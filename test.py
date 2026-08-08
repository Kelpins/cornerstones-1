from machine import Pin, PWM
import time
from neopixel import NeoPixel as np
import utime

data_pin = Pin(9, Pin.OUT)    # SER (data)
latch_pin = Pin(8, Pin.OUT)   # RCLK (latch)
clock_pin = Pin(22, Pin.OUT)  # SRCLK (clock)

bit_order = [6, 0, 7, 5, 1, 4, 2, 3]  # last two are sprinkle LEDs

trigger_right = Pin(2, Pin.OUT)
echo_right = Pin(3, Pin.IN)


def send_byte(val):
    """Send a full byte to the 74HC595, LSB first."""
    for i in range(8):
        data_pin.value((val >> i) & 1)
        clock_pin.high()
        clock_pin.low()
    latch_pin.high()
    latch_pin.low()
    
    
def ultra(trigger, echo): #inputs are the GPIO pins
    
    avgDist = [] #avg list to hold values so that it runs three times
    for i in range(5): #runs 5 times so that one value is not way crazy
        trigger.low()
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5) 
        trigger.low()
        
        
        signaloff = 0  # Initialize
        signalon = 0   # Initialize
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        
        while echo.value() == 1:
            signalon = utime.ticks_us()
        
        
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        avgDist.append(distance)
        time.sleep(0.1)
        
    avgDist.remove(max(avgDist)) #removes highest and lowest
    avgDist.remove(min(avgDist)) #removes highest and lowest
    return (sum(avgDist) / len(avgDist)) #returns an average of the remaining three

start_dist = ultra(trigger_right, echo_right)
mask = 128

while True:#utime.time() - startTime < 100:
        
        us = ultra(trigger_right, echo_right)
        
        print(us)
        
        mask |= (1 << bit_order[:-2][5])
        
        print(mask)
        
        send_byte(mask)
        
        time.sleep(1)

