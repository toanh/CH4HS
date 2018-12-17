from CS4HS import *

import random

######################## collision code #############################
def IsColliding(x1, y1, width1, height1, x2, y2, width2, height2):
    return not(x1 > (x2 + width2) or \
               y1 > (y2 + height2) or \
               x2 > (x1 + width1) or \
               y2 > (y1 + height1))
#####################################################################

game = Graphics(800, 600)

player_1_x = 0                    # width = 24
player_1_y = 0                    # height = 24

player_2_x = 100                  # width = 24
player_2_y = 100                  # height = 24

star_x = random.randint(0, 750)   # width = 20
star_y = random.randint(0, 550)   # height = 20

player_1_speed = 2
player_2_speed = 1


label .run

game.clear()

# checking for input
if game.isKeyPressed(KEY_A):
    player_1_x -= player_1_speed
if game.isKeyPressed(KEY_D):
    player_1_x += player_1_speed
if game.isKeyPressed(KEY_W):
    player_1_y += player_1_speed
if game.isKeyPressed(KEY_S):
    player_1_y -= player_1_speed

if game.isKeyPressed(KEY_LEFT):
    player_2_x -= player_2_speed
if game.isKeyPressed(KEY_RIGHT):
    player_2_x += player_2_speed
if game.isKeyPressed(KEY_UP):
    player_2_y += player_2_speed
if game.isKeyPressed(KEY_DOWN):
    player_2_y -= player_2_speed

# drawing the images
# note the order, drawn from back to front
game.drawImage("star.gif", star_x, star_y)

game.drawImage("red.gif", player_1_x, player_1_y)
game.drawImage("blue.gif", player_2_x, player_2_y)



# must "reveal" the game to see the updated screen
game.reveal()

goto .run



