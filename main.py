import machine, display
from panda import Panda
from time import ticks_diff, ticks_ms, sleep_ms


# global variables
framerate = 24
ms_per_frame = int(1000/24)

tft = display.TFT()

# Display initialization
tft.init(tft.ST7789, rot=tft.LANDSCAPE, miso=17, backl_pin=4, backl_on=1, mosi=19, clk=18, cs=5, dc=16, splash=False)
tft.setwin(40,52,320,240)

# If colors are wrong (white background)
tft.tft_writecmd(0x21)

# 240x135

# draw cloud
tft.circle(10, 13, 7, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(23, 13, 10, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(35, 13, 9, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(47, 13, 7, color=tft.CYAN, fillcolor=tft.CYAN)

tft.circle(95, 13, 7, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(108, 13, 9, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(120, 13, 10, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(132, 13, 8, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(142, 13, 6, color=tft.CYAN, fillcolor=tft.CYAN)

tft.circle(190, 13, 7, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(203, 13, 10, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(215, 13, 9, color=tft.CYAN, fillcolor=tft.CYAN)
tft.circle(227, 13, 7, color=tft.CYAN, fillcolor=tft.CYAN)


tft.text(5, 124, "Diana", tft.BLUE)




def b0_press(pin):
    print("Button 0 {}".format("pressed" if pin.value() else "released"))

def b1_press(pin):
    print("Button 1 {}".format("pressed" if pin.value() else eyes_left()))



panda = Panda(tft)


# b0 = machine.Pin(0, handler=b0_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000, pull=machine.Pin.PULL_UP)
# b1 = machine.Pin(35, handler=b1_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000)

last_time = 0
while True:
      # tick()   #Run one game step
      tdiff = ms_per_frame - ticks_diff(ticks_ms(), last_time)
      if tdiff > 0:
        sleep_ms(tdiff)
      last_time = ticks_ms()
