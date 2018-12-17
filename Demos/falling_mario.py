# using the CS4HS library
import sys
sys.path.append("..")

from CS4HS import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 0
y = 300

@game.code
def main():
    # your main game code goes here
    # remember to refer to any variables above as global
    global x, y
    
    game.clear()
    game.drawImage("mario.gif", x, y)

    # activities:
    #   make mario fall vertically down the screen
    #   make mario fall diagonally across the screen
    #   extension: make mario fall under the influence of "gravity"
