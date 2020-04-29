import time
from pixel_ring import pixel_ring
from gpiozero import LED

power = LED(5)

def start_LED(n):
    power.on()
    pixel_ring.set_brightness(10)
    time_end = time.time() + n;
    return time_end

def end_LED():
    pixel_ring.off()
    power.off()

def wakeup(n):
    time_end = start_LED(n)   
    pixel_ring.wakeup()
    time.sleep(n)
    end_LED()

def think(n):
    time_end = start_LED(n)
    pixel_ring.wakeup() 
    pixel_ring.think()
    time.sleep(n)
    end_LED()

def speak(n):
    time_end = start_LED(n)
    pixel_ring.wakeup()  
    pixel_ring.speak()
    time.sleep(n)
    end_LED()
