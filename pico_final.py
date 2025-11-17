from machine import Pin, ADC, PWM, I2C
import time
from pico_i2c_lcd import I2cLcd
import utime
import math
import neopixel

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.putstr("Hello World!")

onboard = Pin(25, Pin.OUT)
blink_led = Pin(15, Pin.OUT)
buzzer = PWM(Pin(9))
servo = PWM(Pin(16))
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
ir_out = Pin(17, Pin.OUT)
ir_in = Pin(22, Pin.IN)

buzzer.duty_u16(2500)
servo.freq(50)

red_pin = 14
green_pin = 13
blue_pin = 12
red_led = PWM(Pin(red_pin))
green_led = PWM(Pin(green_pin))
blue_led = PWM(Pin(blue_pin))

np = neopixel.NeoPixel(machine.Pin(4), 8)
np[0] = (255, 0, 0)
np[1] = (255, 165, 0)
np[2] = (255, 255, 0)
np[3] = (0, 255, 25)
np[4] = (0, 0, 255)
np[5] = (128, 0, 128)
np[6] = (255, 0, 255)
np[7] = (255, 255, 255)
np.write()

# Set PWM frequency (1000 Hz is good for LEDs)
red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

def check_ir():
    if ir_in.value() == 0:
        ir_out.value(1)
    else:
        ir_out.value(0)

def set_color(red, green, blue):
    red_duty = int(red * 65535 / 255)
    green_duty = int(green * 65535 / 255)
    blue_duty = int(blue * 65535 / 255)
    
    red_led.duty_u16(red_duty)
    green_led.duty_u16(green_duty)
    blue_led.duty_u16(blue_duty)

def ReadThermistor():
    therm = ADC(26)
    therm_value = therm.read_u16()
    voltage = therm_value / 65535.0 * 3.3
    Rt = 10 * voltage / (3.3 - voltage)
    tempK = (1 / (1 / (273.15 + 25) + (math.log(Rt / 10)) / 3950))
    tempC = int(tempK - 273.15)
    
    return tempC

def ReadPotentiometer():
    pot = ADC(27)
    adc_value = pot.read_u16()

    pct = int((100/65535)*adc_value)

    return pct

def ReadPhotoresistor():
    phot = ADC(28)
    adc_value = phot.read_u16()
    
    pct = int((100/65535)*adc_value)
    
    return pct

def ReadUltrasonic():
    # Send out a pulse from trigger pin
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    # Measure time of signal on vs off
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff

    # Calculate distance from speed of sound
    return (timepassed * 0.0343) / 2


while True:

    potvalue = ReadPotentiometer()
    print("Potentiometer: " + str(potvalue))
    
    photvalue = ReadPhotoresistor()
    print("Photoresistor: " + str(photvalue))
    
    ultravalue = ReadUltrasonic()
    print("Ultrasonic: " + str(ultravalue) + " cm")
    
    thermvalue = ReadThermistor()
    print("Thermistor: ", thermvalue, " degrees C")
    
    check_ir()
    
    # servo goes @ potentiometer max
    duty_a = 1802
    duty_b = 1802
    duty_c = 1802
    if potvalue==100:
        duty_a = 1802
        duty_b = int((1802 + 8400) / 2)
        duty_c = 8350
    
    onboard.on()
    blink_led.off()
    set_color(255, 0, 0)
    servo.duty_u16(duty_a)
    
    time.sleep(1)
    
    check_ir()    
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    onboard.off()
    blink_led.on()
    set_color(0, 255, 0)
    servo.duty_u16(duty_b)
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    
    time.sleep(1)
    
    check_ir()
    servo.duty_u16(duty_c)
    onboard.off()
    blink_led.off()
    set_color(0, 0, 255)
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    
    time.sleep(1)
    

