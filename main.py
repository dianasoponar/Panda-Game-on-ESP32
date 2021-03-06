import machine, display
from game import Game
from time import ticks_diff, ticks_ms, sleep_ms

game = Game()

def b0_press(pin):
    print("Button 0 {}".format("pressed" if pin.value() else game.panda_eat()))

def b1_press(pin):
    print("Button 1 {}".format("pressed" if pin.value() else game.panda_sleep()))

def sound_rain(pin):
    print("Sound sensor")
    game.get_items().make_it_rain()

def light_sleep(pin):
    if (pin.value() == 1):
        game.panda_sleep()

b0 = machine.Pin(0, handler=b0_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000, pull=machine.Pin.PULL_UP)
b1 = machine.Pin(35, handler=b1_press, trigger=machine.Pin.IRQ_ANYEDGE, debounce=50000)
sound_sensor = machine.Pin(26, handler=sound_rain, trigger=machine.Pin.IRQ_ANYEDGE, debounce=500000)
sound_sensor = machine.Pin(25, handler=light_sleep, trigger=machine.Pin.IRQ_ANYEDGE, debounce=500000)

framerate = 30
ms_per_frame = int(1000/24)
last_time = 0
hungry_time = ticks_ms()
sleep_time = ticks_ms()
panda_blink = 0
while True:
    # tick()   #Run one game step
    tdiff = ms_per_frame - ticks_diff(ticks_ms(), last_time)
    if tdiff > 0:
        sleep_ms(tdiff)
    last_time = ticks_ms()

    # check if the game is over
    if game.game_over():
        sleep_ms(10000)
        break

    # move panda's eyes every 8 seconds
    if ticks_diff(ticks_ms(), panda_blink) > 2000:
        game.get_panda().move_eyes()
        panda_blink = ticks_ms()

    if game.is_eating():
        print("Panda is eating!")
        hungry_time = ticks_ms()

    # drop one hungry bar every 10 seconds
    if ticks_diff(ticks_ms(), hungry_time) > 40000:
        print(ticks_diff(ticks_ms(), hungry_time))
        game.remove_hungry_segment()
        hungry_time = ticks_ms()

    # drop one sleep bar every 10 seconds
    if ticks_diff(ticks_ms(), sleep_time) > 50000:
        print(ticks_diff(ticks_ms(), sleep_time))
        game.remove_sleep_segment()
        sleep_time = ticks_ms()
