# Panda Game

This game runs on the TTGO T-Display board.

The game is inspired by the old Tamagotchi game where you have to
take care of an animal.

I used a panda that can eat bamboo and sleep. Because the panda lives outside sometimes it happens to rain.

## Functionalities
The left button has the action for eating and the right button the action for
sleeping.
It has two life bars: the upper one representing the eating level and the lower
one the sleeping level. If the bars are empty the panda will die soon and the
game will be over. If the user decides to feed the panda, the food bar will fill.
It works the same for sleeping.

Additionally, the user can add two extra sensors to the game: a photoresistor and a sound sensor.
When the light is gone (e.g. turn off the lights), the panda will go to sleep and, when a loud enough noise is recorded (e.g. a clap) it will start raining.

## Challenges
One of the main challenges was to remove objects from the screen. Instead of
using the clean() function, I redraw the elements using the background color.
Another challenge was to give the impression that the raindrops are moving.
I solve this problem by deleting the first set of rain and redrawing them a
couple of centimeters down.

See video [here](https://www.youtube.com/watch?v=8NU83tFDy1k).