import display
from panda import Panda
from items import Items
from time import sleep_ms


class Game(object):
    def __init__(self):
         self.hungry_segments = 3
         self.sleep_segments = 3
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
        sleep_ms(200)
        self.items.eat_bamboo()
        if self.hungry_segments < 3:
            print("Add: ", self.hungry_segments)
            self.tft.roundrect(192 + (self.hungry_segments* 14), 37, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
            self.hungry_segments += 1
            print("Remaining: ", self.hungry_segments)
        self.is_panda_eating = False

    def is_eating(self):
        return self.is_panda_eating

    def panda_sleep(self):
        self.panda.remove_panda()
        self.panda.draw_sleeping_panda()
        for i in range(5):
            sleep_ms(200)
            self.tft.text(140, 40, "Z", color=self.tft.LIGHTGREY)
            sleep_ms(200)
            self.tft.text(146, 45, "Z", color=self.tft.LIGHTGREY)
            sleep_ms(200)
            self.tft.text(152, 50, "Z", color=self.tft.LIGHTGREY)
            sleep_ms(400)
            self.tft.text(140, 40, "Z", color=self.tft.BLACK)
            self.tft.text(146, 45, "Z", color=self.tft.BLACK)
            self.tft.text(152, 50, "Z", color=self.tft.BLACK)
        self.panda.remove_sleeping_panda()
        self.panda.draw_panda()
        if self.sleep_segments < 3:
            print("Add: ", self.sleep_segments)
            self.tft.roundrect(192 + (self.sleep_segments* 14), 52, 13, 4, 1, color=self.tft.GREENYELLOW, fillcolor=self.tft.GREENYELLOW)
            self.sleep_segments += 1
            print("Remaining: ", self.sleep_segments)

    # check if the game is over
    def game_over(self):
        if self.hungry_segments >= 0 and self.sleep_segments >=0:
            return False
        else:
            self.tft.clear()
            self.items.draw_clouds()
            self.tft.text(75, 65, "GAME OVER")
            return True

    # remove one segment from the hungry bar
    def remove_hungry_segment(self):
        print("Remove hungry: ", self.hungry_segments)
        self.hungry_segments -= 1
        self.tft.roundrect(192 + (self.hungry_segments * 14), 37, 13, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        print("Remaining: ", self.hungry_segments)

    # remove one segment from the sleep bar
    def remove_sleep_segment(self):
        print("Remove sleep: ", self.sleep_segments)
        self.sleep_segments -= 1
        self.tft.roundrect(192 + (self.sleep_segments * 14), 52, 13, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        print("Remaining: ", self.sleep_segments)
