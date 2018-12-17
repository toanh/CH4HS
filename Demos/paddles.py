# using the CS4HS library
from CS4HS import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
ball_x = 300
ball_y = 200

player1_x = 20
player1_y = 150

player2_x = 560
player2_y = 150

@game.code
def main():
    # your main game code goes here
    # remember to refer to any variables above as global
    global ball_x, ball_y, player1_x, player1_y, player2_x, player2_y

    # drawing all the objects
    game.clear()
    game.drawImage("ball.gif", ball_x, ball_y)
    game.drawImage("paddle_red.gif", player1_x, player1_y)
    game.drawImage("paddle_blue.gif", player2_x, player2_y)

    # doing the input checking
    if game.isKeyPressed(KEY_W):
        player1_y += 1

    # activities:
    #   move the paddles according to the W,S and UP,DOWN keys
    # extensions:
    #   limit the movement so that the paddles don't go off the screen
    #   introduce 'inertia' to the paddle so that they don't immediately
    #       stop when the key is let go (e.g. they slowly come to a stop)
