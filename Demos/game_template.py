# using the CS4HS library
from CS4HS import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# declare my variables
# (creating my buckets)
y = 300
x = 0
speed = 0

# your variables go here

@game.code
def main():
    # your main game code goes here
    # remember to refer to any variables above as global
    global y, x, speed
    
    game.clear()
    game.drawImage("mario.gif", x, y)

    speed = speed - 0.01
    y = y + speed

    
    

    
