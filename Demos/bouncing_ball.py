# using the CS4HS library
import sys
sys.path.append("..")

from CS4HS import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 0
y = 300
y_velocity = -3
x_velocity = 3
player1_y = 0
player2_y = 0

@game.mainloop
def main():
    # your main game code goes here
    # remember to refer to any variables above as global
    global x, y, y_velocity, x_velocity, player1_y, player2_y
    
    game.clear()
    game.drawImage("ball.gif", x, y)

    game.drawImage("paddle_red.gif", 20, player1_y)
    game.drawImage("paddle_blue.gif", 580, player2_y)

    if game.isKeyPressed(KEY_W):# KEY_W, KEY_S, KEY_UP, KEY_DOWN
        # make player1 go up
        player1_y = player1_y + 1

    if game.isKeyPressed(KEY_S):# KEY_W, KEY_S, KEY_UP, KEY_DOWN
        # make player1 go up
        player1_y = player1_y - 1

    if game.isKeyPressed(KEY_UP):# KEY_W, KEY_S, KEY_UP, KEY_DOWN
        # make player1 go up
        player2_y = player2_y + 1

    if game.isKeyPressed(KEY_DOWN):# KEY_W, KEY_S, KEY_UP, KEY_DOWN
        # make player1 go up
        player2_y = player2_y - 1

    y = y + y_velocity
    x = x + x_velocity

    # we are checking if the y-position of the anchor point is at zero
    if y < 0:
        # reset the position
        y = 0
        y_velocity = y_velocity * -1

    if y > 384:
        y_velocity = y_velocity * -1

    if x > 584:
        x_velocity = x_velocity * -1

    if x < 0:
        x_velocity = x_velocity * -1
        

    # activities:
    #   make the ball fall down the screen... and STOP it when it
    #       hits the bottom edge
    #   make the ball fall down the screen... and BOUNCE it back up
    #       when it hits the bottom edge     
    #   make the ball move diagonally across and screen and bounce it
    #       off all the edges of the screen

game.run()