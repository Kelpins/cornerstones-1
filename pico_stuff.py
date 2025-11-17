from machine import Pin, ADC, PWM, I2C
from pico_i2c_lcd import I2cLcd
import time
import utime

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def slowType(lcd, text, delay=0.1):
    for i in text:
        lcd.putstr(i)
        sleep(delay)

while True:
    lcd.show_cursor()
    lcd.blink_cursor_on()
    slowType(lcd, "Place text here", 0.3)
    sleep(3)
    lcd.blink_cursor_off()
    lcd.hide_cursor()
    sleep(1)
    lcd.clear()

onboard = Pin(25, Pin.OUT)
blink_led = Pin(15, Pin.OUT)
buzzer = PWM(Pin(9))
servo = PWM(Pin(16))
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

buzzer.duty_u16(2500)
servo.freq(50)

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
    #potentiometer (3)
    potvalue = ReadPotentiometer()
    time_delay = max(potvalue / 33, 0.5)
    print("Potentiometer: " + str(potvalue))
    
    photvalue = ReadPhotoresistor()
    print("Photoresistor: " + str(photvalue))
    
    ultravalue = ReadUltrasonic()
    print("Ultrasonic: " + str(ultravalue) + " cm")
    
    duty_a = 1802
    duty_b = 1802
    duty_c = 1802
    if potvalue==100:
        duty_a = 1802
        duty_b = int((1802 + 8500) / 2)
        duty_c = 8370
    
    #leds (1 & 2)
    onboard.on()
    blink_led.off()
    servo.duty_u16(duty_a)
    time.sleep(time_delay)
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    onboard.off()
    blink_led.on()
    servo.duty_u16(duty_b)
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    time.sleep(time_delay)
    servo.duty_u16(duty_c)
    onboard.off()
    blink_led.off()
    buzzer.freq(max(50, int(ReadPhotoresistor() * 4500 / 100)))
    time.sleep(time_delay)
    
