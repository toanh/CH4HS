from CS4HS import *

import random

######################## collision code #############################
def IsColliding(x1, y1, width1, height1, x2, y2, width2, height2):
    return not(x1 > (x2 + width2) or \
               y1 > (y2 + height2) or \
               x2 > (x1 + width1) or \
               y2 > (y1 + height1))
#####################################################################

# creating our Graphics object
game = Graphics(640, 480)

player_x = 0                    # width = 80
player_y = 0                    # height = 16

star_x = random.randint(0, 620)   # width = 20
star_y = 480   # height = 20

player_speed = 2
star_speed = 1

score = 0

# using GOTOs... Evil??
# Or a good scaffolding tool?
label .run

game.clear()

star_y = star_y - star_speed

# checking for input
if game.isKeyPressed(KEY_A):
    player_x -= player_speed
if game.isKeyPressed(KEY_D):
    player_x += player_speed

if IsColliding(player_x, player_y, 80, 16, star_x, star_y, 20, 20):
    score += 1
    # resetting the star's position
    star_x = random.randint(0, 620)   # width = 20
    star_y = 480
    # slowly increasing its speed to ramp up difficulty
    star_speed += 0.05

if star_y < -20:
    goto .end

# drawing the images
# note the order, drawn from back to front

game.drawImage("star.gif", star_x, star_y)
game.drawImage("paddle.gif", player_x, player_y)
# BUG: drawText() has to be the LAST call to game or else everything after it flickers
# AND there can only be ONE drawText call
game.drawText("Score: " + str(score), 280, 440, fontSize=20)

# must "reveal" the game to see the updated screen
game.reveal()

goto .run

label .end
print("GAME OVER!!")

'''
extension ideas:
- applying "gravity" to the star
- applying "inertia" to the paddle
- supporting multiple lives
- supporting 2 players
- Remove "goto" scaffold (understanding of state variables and loops)
- game over and start screens
- Power ups (expand size of paddles, slow down star, change star size, etc. etc.)
- displaying lives as icons (requires loops)
- multiple falling stars (requires lists)
- allowing paddles to "shoot" the stars (requires lists)
'''

