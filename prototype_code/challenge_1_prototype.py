#First Challenge Example Board

# Red & Green LED's for what function is running
# button swaps between modes
# 1. Ping & colour wheel change combo
# 2. Potentiometer & rainbow chase control
# OLED Screen describing score

import board
from digitalio import DigitalInOut, Direction, Pull
import time
from math import floor
from rainbowio import colorwheel
import neopixel
from analogio import AnalogIn
from adafruit_simplemath import map_range
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

#init button D12 as pull up
button = DigitalInOut(board.D12)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

#init red LED D11
r_led = DigitalInOut(board.D11)
r_led.direction = Direction.OUTPUT

#init green LED D10
g_led = DigitalInOut(board.D10)
g_led.direction = Direction.OUTPUT

#init ping sensor D7
ping_sensor = DigitalInOut(board.D7)

#init neopixel ring D8
num_pixels = 16
pixels = neopixel.NeoPixel(board.D8, 16, brightness=0.1)

#init Potentiometer A1
pot = AnalogIn(board.A1)

#reset displays, needed as if the m4 reboots, we must release the screen before init again.
displayio.release_displays()

oled_reset = board.D9
# init i2C object for OLED screen
i2c = board.I2C()
#perhaps capitalD for address?)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

#declare variables
button_state = False
ping_sensor_state = True
distance = 0
wait = 0.009

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0,0,0)

def sonar(pin):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Pin Sensor. Trigger & Echo are on the 'same pin'.
    pin = the pin with the ping sensor
    returns: Distance in cm between 0 & 568

    Note: If object is <5cm away, it will register either 0 or 568cm away.
    Note: Introduce a 0.1sec delay when taking sensor readings in CircuitPython, else the code will stop parsing.

    '''

    usleep = lambda x: x/1000000

    pin.direction = Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    usleep(2)
    pin.value = 1
    usleep(10)
    pin.value = 0

    #recieve echo signal
    pin.direction = Direction.INPUT
    while pin.value == 0:
        start_time = time.monotonic_ns()

    while pin.value == 1:
        end_time = time.monotonic_ns()

    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash.
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        print("object too close")
        distance = 0

    return distance

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


#OLED Screen setup
#display parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

#create a full white rectangle object
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#write the object to the display
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

def display_word(word):
    # Set text, font, and color
    text = str(word)
    font = terminalio.FONT
    color = 0xFFFFFF

    # Create the text label
    text_area = label.Label(font, text=text, color=color, x = 28, y=HEIGHT // 2-1)
    # Show it
    display.show(text_area)

while True:
    button_state = button.value

    if not button_state:
        #toggle main bool
        ping_sensor_state = False
    else:
        ping_sensor_state = True

    if ping_sensor_state:
        #ping chooses which colour displays in colour chase
        display_word("Ping State\nDistance: " + str(distance))
        r_led.value = True
        g_led.value = False

        distance = sonar(ping_sensor)
        #print(distance)
        if distance > 50:
            color_choice = CYAN
            color_chase(color_choice, wait)
            color_choice = PURPLE
            color_chase(color_choice, wait)
        else:
            color_choice = BLUE
            color_chase(color_choice, wait)
            color_choice = RED
            color_chase(color_choice, wait)


    else:
        #pot changes speed of rainbow show
        r_led.value = False
        g_led.value = True
        voltage = pot.value
        voltage = (map_range(voltage, 0,55353,0.01,0.1)/100)
        #voltage = int(voltage)
        display_word("Pot. State\nWait: " + str(voltage))
        rainbow_cycle(voltage)







