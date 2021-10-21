#Moisture_sensor_1.py                             

from math import ceil
import machine
import utime
led_onboard = machine.Pin(25,machine.Pin.OUT)
x = 0
print ("BLINKY_!")
for x in range(1):
    led_onboard.value(1)
    utime.sleep(.1)
    led_onboard.value(0)
    utime.sleep(.1)                                                                                                
    x = x+1
print ("Program Ready   ")

moisture = machine.ADC(26)
led1 = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)

led1.value(0)
led2.value(0)
led3.value(0)
av1 = 0
av2 = 0
av3 = 0
av4 = 0
av5 = 0
k = 0
#>>>>>>>PROGRAM>>>>>>>>

print ("HELLO MOISTURE_ADC")

while True:
    led1.value(0)
    led2.value(0)
    led3.value(0)
    
    conversion_factor = 3.3/(65535)
    
    x = (moisture.read_u16()) * conversion_factor    #Analog Voltage
    x1 = round(x,3)
#Averaage over 5 readings    
    av5 = av4
    av4 = av3
    av3 = av2
    av2 = av1
    av1 = x1
    x2 = (av1+av2+av3+av4+av5)/5
    
    print ('X1:  ','{:.5}'.format(str( x1)))
    print ('X2:  ','{:.5}'.format(str( x2)))  #format for 5 digits
    
    if x2 > 1.9 :   #DRY  RED
        
        if k>8:
            led1.value(1)
            led2.value(0)
            led3.value(0)
            utime.sleep_ms(250)
            led1.value(0)
            print ("LED1   RED  DRY")
            
               
    elif x2 > 1.62:    #Needs Watering  YELLOW
        
        if k> 8:
            led2.value(1)
            led1.value(0)
            led3.value(0)
            utime.sleep_ms(250)
            led2.value(0)
            print ("LED2   YELLOW  NEEDS WATER")
            
        

    else:
        
        if k> 8:
            led3.value(1)    #WET  GREEN
            led1.value(0)
            led2.value(0)
            utime.sleep_ms(250)
            led3.value(0)
            print ("LED3   GREEN   WET")
    k = k+1
    utime.sleep_ms(250)
 
       