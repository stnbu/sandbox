
from machine import Pin
import network

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('urmom', 'huskyballoon666')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


# Toggle that stupid green light with "UP+"
led = Pin(3, Pin.OUT)
button = Pin(1, Pin.IN)
def button_press(pin):
    led.value(not led.value())
button.irq(trigger=Pin.IRQ_FALLING, handler=button_press)


wifi_connect()

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
