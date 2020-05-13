Panda Game

For this game, I got my inspiration from the old Tamagotchi game where you have to
take care of an animal.

I used a panda that can eat bamboo and sleep. The panda moves his eyes from time
to time and because it lives outside, sometimes it rains.
The left button has the action for eating and the right button the action for
sleeping.
It has two life bars: the upper one representing the eating level and the lower
one the sleeping level. If the bars are empty the panda will die soon and the
game will be over. If the user decides to feed the panda, the food bar will fill.
It works the same for sleeping.

One of the main challenges was to remove objects from the screen. Instead of
using the clean() function, I redraw the elements using the background color.
Another challenge was to give the impression that the raindrops are moving.
I solve this problem by deleting the first set of rain and redrawing them a
couple of centimeters down.
