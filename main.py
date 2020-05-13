import machine, display
from panda import Panda
from items import Items
from time import ticks_diff, ticks_ms, sleep_ms


class Game(object):
    def __init__(self):
         self.hungry_segments = 3
         self.is_panda_eating = False
         # Displat size: 240x135
         self.tft = display.TFT()

         # Display initialization
         self.tft.init(self.tft.ST7789, rot=self.tft.LANDSCAPE, miso=17, backl_pin=4, backl_on=1, mosi=19, clk=18, cs=5, dc=16, splash=False)
         self.tft.setwin(40,52,320,240)

         # If colors are wrong (white background)
         self.tft.tft_writecmd(0x21)

         self.panda = Panda(self.tft)
         self.items = Items(self.tft)

         self.draw_life_bars()


    def get_tft(self):
        return self.tft

    def get_items(self):
        return self.items

    def get_panda(self):
        return self.panda

    def draw_life_bars(self):
        self.tft.roundrect(190, 35, 45, 8, 2, color=self.tft.GREENYELLOW)
        # segments
        self.tft.roundrect(192, 37, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
        self.tft.roundrect(206, 37, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
        self.tft.roundrect(220, 37, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)

        self.tft.roundrect(190, 50, 45, 8, 2, color=self.tft.GREENYELLOW)
        # segments
        self.tft.roundrect(192, 52, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
        self.tft.roundrect(206, 52, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
        self.tft.roundrect(220, 52, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)

    def panda_eat(self):
        self.is_panda_eating = True
        self.items.draw_bamboo()
        sleep_ms(900)
        self.items.eat_bamboo()
        if self.hungry_segments < 3:
            print("Add: ", self.hungry_segments)
            self.tft.roundrect(192 + (self.hungry_segments* 14), 37, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
            self.hungry_segments += 1
            print("Remaining: ", self.hungry_segments)
        self.is_panda_eating = False

    def is_eating(self):
        return self.is_panda_eating

    def game_over(self):
        if self.hungry_segments >= 0:
            return False
        else:
            self.tft.clear()
            self.items.draw_clouds()
            self.tft.text(75, 65, "GAME OVER")
            return True

    def remove_segment(self):
        print("Remove: ", self.hungry_segments)
        self.hungry_segments -= 1
        self.tft.roundrect(192 + (self.hungry_segments * 14), 37, 13, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        print("Remaining: ", self.hungry_segments)


game = Game()

def b0_press(pin):
    print("Button 0 {}".format("pressed" if pin.value() else game.panda_eat()))


def b1_press(pin):
    print("Button 1 {}".format("pressed" if pin.value() else game.get_items().make_it_rain()))


b0 = machine.Pin(0, handler=b0_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000, pull=machine.Pin.PULL_UP)
b1 = machine.Pin(35, handler=b1_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000)

framerate = 30
ms_per_frame = int(1000/24)
last_time = 0
hungry_time = ticks_ms()
panda_blink = 0
make_rain = 0
while True:
    # tick()   #Run one game step
    tdiff = ms_per_frame - ticks_diff(ticks_ms(), last_time)
    if tdiff > 0:
        sleep_ms(tdiff)
    last_time = ticks_ms()

    if game.game_over():
        sleep_ms(10000)
        break

    # move panda's eyes every 8 seconds
    if ticks_diff(ticks_ms(), panda_blink) > 5000:
        game.get_panda().move_eyes()
        panda_blink = ticks_ms()

    if game.is_eating():
        print("Panda is eating!")
        hungry_time = ticks_ms()

    # drop one hungry bar every 10 seconds
    if ticks_diff(ticks_ms(), hungry_time) > 20000:
        print(ticks_diff(ticks_ms(), hungry_time))
        game.remove_segment()
        hungry_time = ticks_ms()
