from time import sleep_ms


class Items(object):
    def __init__(self, tft):
        self.tft = tft
        self.draw_clouds()

    # draw clouds
    def draw_clouds(self):
        # left cloud
        self.tft.circle(10, 13, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(23, 13, 10, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(35, 13, 9, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(47, 13, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        # middle cloud
        self.tft.circle(95, 13, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(108, 13, 9, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(120, 13, 10, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(132, 13, 8, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(142, 13, 6, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        # right cloud
        self.tft.circle(190, 13, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(203, 13, 10, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(215, 13, 9, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(227, 13, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)

    def rain(self, x, y, rain_color):
        for i in range(5, 236, 20):
            for j in range(x, 121, 25):
                if (not (i in range(92, 150) and j in range(38, 102))) and (not (i in range(190, 240) and j in range(30, 58))):
                    self.tft.line(i, j, i, j + 4, color=rain_color)
        for i in range(15, 236, 20):
            for j in range(y, 121, 25):
                if (not (i in range(92, 150) and j in range(38, 102))) and (not (i in range(190, 240) and j in range(30, 58))):
                    self.tft.line(i, j, i, j + 4, color=rain_color)

    def make_it_rain(self):
        for i in range(3):
            self.rain(25, 35, self.tft.DARKCYAN)
            sleep_ms(500)
            self.rain(25, 35, self.tft.BLACK)
            sleep_ms(100)
            self.rain(30, 40, self.tft.DARKCYAN)
            sleep_ms(500)
            self.rain(30, 40, self.tft.BLACK)
            sleep_ms(100)
            self.rain(35, 45, self.tft.DARKCYAN)
            sleep_ms(500)
            self.rain(35, 45, self.tft.BLACK)
            sleep_ms(100)

    # draw bamboo
    def draw_bamboo(self):
        self.tft.roundrect(50, 46, 7, 4, 1, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 50, 7, 10, 2, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 60, 7, 4, 1, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 64, 7, 10, 2, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 74, 7, 4, 1, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 78, 7, 10, 2, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.roundrect(50, 88, 7, 4, 1, color=self.tft.GREEN, fillcolor=self.tft.GREEN)
        self.tft.line(54, 55, 60, 48, color=self.tft.GREENYELLOW)
        self.tft.line(54, 70, 60, 63, color=self.tft.GREENYELLOW)
        # tft.line(54, 85, 60, 78, color=tft.GREENYELLOW)
        self.tft.line(52, 55, 46, 48, color=self.tft.GREENYELLOW)
        # tft.line(52, 70, 46, 63, color=tft.GREENYELLOW)
        self.tft.line(52, 85, 46, 78, color=self.tft.GREENYELLOW)

    def eat_bamboo(self):
        sleep_ms(700)
        self.tft.roundrect(50, 46, 7, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.roundrect(50, 50, 7, 10, 2, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.line(54, 55, 60, 48, color=self.tft.BLACK)
        self.tft.line(52, 55, 46, 48, color=self.tft.BLACK)
        sleep_ms(700)
        self.tft.roundrect(50, 60, 7, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.roundrect(50, 64, 7, 10, 2, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.line(54, 70, 60, 63, color=self.tft.BLACK)
        sleep_ms(700)
        self.tft.roundrect(50, 74, 7, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.roundrect(50, 78, 7, 10, 2, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.roundrect(50, 88, 7, 4, 1, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.line(52, 85, 46, 78, color=self.tft.BLACK)
