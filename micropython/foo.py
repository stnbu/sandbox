



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
def _flash_pin():
    from machine import Pin
    import time
    led = Pin(3, Pin.OUT)
    for _ in range(0, 100):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)


# works
def _flash_pin_w_timer():
    from microcontroller import Pin, Timer
    led = Pin(3, Pin.OUT)
    flash = Timer(0)
    def flash_led(timer):
        led.value(not led.value())
    flash.init(period=500, mode=Timer.PERIODIC, callback=flash_led)
    # flash.deinit()

# works
def _toggle_led_button():
    from machine import Pin
    led = Pin(3, Pin.OUT)
    button = Pin(1, Pin.IN)
    def button_press(pin):
        led.value(not led.value())
    button.irq(trigger=Pin.IRQ_FALLING, handler=button_press)

############################################################
############################################################
############################################################

"""
display:

dc/data command: Pin(7)
cs/chip select: Pin(8)
reset: Pin(11)

all about esp32s3 SPI pins, hopefully: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#gpio-matrix-and-io-mux

//////////
esp-who mburr$ git grep -il 'ssd.*1306'
components/screen/CMakeLists.txt
components/screen/Kconfig
components/screen/component.mk
components/screen/controller_driver/ssd1306/ssd1306.c
components/screen/controller_driver/ssd1306/ssd1306.h
components/screen/controller_driver/ssd1307/ssd1307.h
components/screen/controller_driver/ssd1322/ssd1322.h
components/screen/interface_driver/scr_interface_driver.c
components/screen/screen_driver.c
components/screen/screen_driver.h
components/screen/test/lcd_mono_test.c
//////////

From ssd1306.c --

#define LCD_BPP  1  // <--- does this mean "bytes per packet"?
"""

def _dud1():
    # lcd dispay
    from machine import Pin, SPI
    from ssd1306 import SSD1306_SPI
    width = 128
    height = 64
    SPI2_HOST = 2  # appears in esp-who/components/modules/lcd/who_lcd.c
    hspi = SPI(SPI2_HOST)
    dc = Pin(7)
    rst = Pin(11)
    cs = Pin(8)
    display = SSD1306_SPI(width, height, hspi, dc, rst, cs)


def _play_w_lcd():
    from machine import Pin, I2C
    import ssd1306
    i2c = I2C(sda=Pin(21), scl=Pin(22))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text('Hello, World!', 0, 0, 1)
    display.show()

###### NEXT: try with SoftI2C
# i2c@lcd
def do_lcd():
    i2c_pins = [
        # These from https://github.com/espressif/esp-who/blob/7199eb1619cffbae91f1f0199c6aae9c7ac08dc7/components/bus/test/test_i2c_bus.c#L24
        (21, 22), # confirmed by https://youtu.be/LY-1DHTxRAk
        (16, 17),
        # These from here 
        (19, 18), # bus #0
        (26, 25), # bus #1 -- slave?
    ]
    from machine import Pin, I2C
    import ssd1306
    for sda, scl in i2c_pins:
        print("trying: sda=%s,sdb=%s" % (sda, scl))
        try:
            i2c = I2C(sda=Pin(sda), scl=Pin(scl))
        except:
            print("failed at I2C: sda=%s,sdb=%s" % (sda, scl))
            continue
        try:
            display = ssd1306.SSD1306_I2C(128, 64, i2c)
        except:
            print("failed at SSD1306: sda=%s,scl=%s" % (sda, scl))
            continue
        print("OMG WE GOT THIS FAR! SDA=%s,SLC=%S" % (sda, scl))
        display.text('Hello, World!', 0, 0, 1) ; display.show()
        break
    
############################################################
############################################################
############################################################

"""
accel:
chip: qma7981
Nums:
.scl_io_num = 5,
.sda_io_num = 4,
uint32_t clk_speed = 400000;

arduino c++ library: https://github.com/cammiboi/qma7981-library
pdf: http://www.siitek.com.cn/Upfiles/down/QMA7981%20Datasheet%20Rev.%20A.PDF
driver used by esp-who: https://github.com/espressif/esp-who/tree/master/components/modules/imu

////////
	uint32_t clk_speed = 400000;
	i2c_config_t conf = {
		.mode = I2C_MODE_MASTER,
		.scl_io_num = 5,
		.sda_io_num = 4,
		.scl_pullup_en = GPIO_PULLUP_ENABLE,
		.sda_pullup_en = GPIO_PULLUP_ENABLE,
		.master.clk_speed = clk_speed,
	};
	i2c_bus_handle = i2c_bus_create(0, &conf);
	assert(i2c_bus_handle != NULL);
	qma7981_handle = i2c_bus_device_create(i2c_bus_handle, 0x12, clk_speed);
////////
"""
def _dud2():
    # accelerometer: does not choke but might be wrong
    from machine import SoftI2C, Pin
    i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)
