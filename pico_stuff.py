from machine import Pin
from machine import ADC
import time

# Define the LED pin (GPIO 25 is the on-board LED)
onboard = Pin(25, Pin.OUT)
blink_led = Pin(15, Pin.OUT) #sets pin 15 as an output pin
photoresistor = machine.ADC(28)

def ReadPotentiometer():
    pot = ADC(27)
    adc_value = pot.read_u16()

    pct = int((100/65535)*adc_value)

    return pct


while True:
    #potentiometer (3)
    potvalue = ReadPotentiometer()
    print("Potentiometer: " + str(potvalue))
    print("Photoresistor: " + str(photoresistor.read_u16()))
    
    #leds (1 & 2)
    onboard.on()
    blink_led.off()
    time.sleep(0.5)
    onboard.off()
    blink_led.on()
    time.sleep(0.5)
    
