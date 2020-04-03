from gpiozero import LED
from time import sleep
from gpiozero import Button

# 12 16 20 21
led1 = LED(12)
led2 = LED(16)
led3 = LED(20)
led4 = LED(21)

wait = 0.003

def s1():
    led1.on()
    led2.off()
    led3.off()
    led4.off()
    sleep(wait)
def s2():    
    led1.on()
    led2.on()
    led3.off()
    led4.off()
    sleep(wait)
def s3():    
    led1.off()
    led2.on()
    led3.off()
    led4.off()
    sleep(wait)
def s4():
    led1.off()
    led2.on()
    led3.on()
    led4.off()
    sleep(wait)
def s5():    
    led1.off()
    led2.off()
    led3.on()
    led4.off()
    sleep(wait)
def s6():    
    led1.off()
    led2.off()
    led3.on()
    led4.on()
    sleep(wait)
def s7():    
    led1.off()
    led2.off()
    led3.off()
    led4.on()
    sleep(wait)
def s8():    
    led1.on()
    led2.off()
    led3.off()
    led4.on()
    sleep(wait)
    
    
def forward():
    i=0
    while i < 10:

        s1()
        s2()
        s3()
        s4()
        s5()
        s6()
        s7()
        s8()
        i+=1
    
def backward():
    j=0
    while j < 10:
        s8()
        s7()
        s6()
        s5()
        s4()
        s3()
        s2()
        s1()
        j+=1
    
def off():    
    led1.off()
    led2.off()
    led3.off()
    led4.off()


        
    

    
