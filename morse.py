from machine import Pin, Timer
from time import sleep

morse = {
    "a":"01",
    "b":"1000",
    "c":"1010",
    "d":"100",
    "e":"0",
    "f":"0010",
    "g":"110",
    "h":"0000",
    "i":"00",
    "j":"0111",
    "k":"101",
    "l":"0100",
    "m":"11",
    "n":"10",
    "o":"111",
    "p":"0110",
    "q":"1101",
    "r":"010",
    "s":"000",
    "t":"1",
    "u":"001",
    "v":"0001",
    "w":"011",
    "x":"1001",
    "y":"1011",
    "z":"1100",
    "1":"01111",
    "2":"00111",
    "3":"00011",
    "4":"00001",
    "5":"00000",
    "6":"100000",
    "7":"11000",
    "8":"11100",
    "9":"11110",
    "0":"11111",
    }

led = Pin(25, Pin.OUT)

inp_text = input("enter a text:")

for c in inp_text.lower():
    if c in morse:
        for m in morse[c]:
            if m == "0":
                led.on()
                sleep(1/4)
                led.off()
            elif m == "1":
                led.on()
                sleep(1)
                led.off()
            sleep(1/2)
            
led.off()