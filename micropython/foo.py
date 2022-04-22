



def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass


    #print('network config:', wlan.ifconfig())




# works
from machine import Pin
import time
led = Pin(3, Pin.OUT)
for _ in range(0, 100):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)


# works
from machine import Pin, Timer
led = Pin(3, Pin.OUT)
flash = Timer(0)
def flash_led(timer):
    led.value(not led.value())
flash.init(period=500, mode=Timer.PERIODIC, callback=flash_led)
# flash.deinit()

# works
from machine import Pin
led = Pin(3, Pin.OUT)
button = Pin(1, Pin.IN)
def button_press(pin):
    led.value(not led.value())
button.irq(trigger=Pin.IRQ_FALLING, handler=button_press)
