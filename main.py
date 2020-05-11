import machine, display
from panda import Panda
from items import Items
from time import ticks_diff, ticks_ms, sleep_ms


# global variables
framerate = 30
ms_per_frame = int(1000/24)
ms_hungry_bar_drop = 10000

# Displat size: 240x135
tft = display.TFT()

# Display initialization
tft.init(tft.ST7789, rot=tft.LANDSCAPE, miso=17, backl_pin=4, backl_on=1, mosi=19, clk=18, cs=5, dc=16, splash=False)
tft.setwin(40,52,320,240)

# If colors are wrong (white background)
tft.tft_writecmd(0x21)

tft.text(5, 124, "Diana", tft.BLUE)

panda = Panda(tft)
items = Items(tft)

# Panda coordinates
# tft.circle(92, 38, 1)
# tft.circle(92, 75, 1)
# tft.circle(92, 102, 1)
#
# tft.circle(148, 38, 1)
# tft.circle(148, 75, 1)
# tft.circle(148, 102, 1)


def game_over():
    tft.clear()
    items.draw_clouds()
    tft.text(75, 65, "GAME OVER")


def b0_press(pin):
    print("Button 0 {}".format("pressed" if pin.value() else panda.eat_bamboo()))

def b1_press(pin):
    print("Button 1 {}".format("pressed" if pin.value() else items.make_it_rain()))


b0 = machine.Pin(0, handler=b0_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000, pull=machine.Pin.PULL_UP)
b1 = machine.Pin(35, handler=b1_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000)

last_time = 0
hungry_time = ticks_ms()
hungry_segment_coor = 220
while True:
    # tick()   #Run one game step
    tdiff = ms_per_frame - ticks_diff(ticks_ms(), last_time)
    if tdiff > 0:
        sleep_ms(tdiff)
    last_time = ticks_ms()

    if not hungry_segment_coor >= 178:
        game_over()
        sleep_ms(10000)

    if ticks_diff(ticks_ms(), hungry_time) > 60000:
      print(ticks_diff(ticks_ms(), hungry_time))
      tft.roundrect(hungry_segment_coor, 37, 13, 4, 1, color=tft.BLACK, fillcolor=tft.BLACK)
      hungry_segment_coor -= 14
      hungry_time = ticks_ms()
