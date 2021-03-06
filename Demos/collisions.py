# using the CS4HS library
from CS4HS import *

######################## collision code #############################
def IsColliding(x1, y1, width1, height1, x2, y2, width2, height2):
    return not(x1 > (x2 + width2) or \
               y1 > (y2 + height2) or \
               x2 > (x1 + width1) or \
               y2 > (y1 + height1))
#####################################################################

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
ball_x = 300
ball_y = 200
ball_vel_x = 3
ball_vel_y = -1

player1_x = 20
player1_y = 150

player2_x = 560
player2_y = 150

@game.code
def main():
    # your main game code goes here
    # remember to refer to any variables above as global
    global ball_x, ball_y, player1_x, player1_y, player2_x, player2_y, \
           ball_vel_x, ball_vel_y

    # drawing all the objects
    game.clear()
    game.drawImage("ball.gif", ball_x, ball_y)
    game.drawImage("paddle_red.gif", player1_x, player1_y)
    game.drawImage("paddle_blue.gif", player2_x, player2_y)

    # doing the input checking
    if game.isKeyPressed(KEY_W):
        player1_y += 1
    if game.isKeyPressed(KEY_S):
        player1_y -= 1
    if game.isKeyPressed(KEY_UP):
        player2_y += 1
    if game.isKeyPressed(KEY_DOWN):
        player2_y -= 1

    # updating the ball's position based on its velocity
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # checking for collision with boundaries and flipping velocity
    # and SNAPPING back to position
    # if we don't SNAP the position, there is a chance it might
    # zig zag along the border
    
    # the right border
    if ball_x > 600-20:
        # the -20 is to cater for the width of the ball
        # due to the anchor point being the bottom right
        
        # we are checking to right edge of the ball with the
        # right edge of the screen
        ball_vel_x = -ball_vel_x
        ball_x = 600 - 20
    # the left border
    if ball_x < 0:
        # we are checking to left edge of the ball with the
        # left edge of the screen
        ball_vel_x = -ball_vel_x
        ball_x = 0
    # the top border
    if ball_y > 400-20:
        # the -20 is to cater for the height of the ball
        # due to the anchor point being the bottom right

        # we are checking to top edge of the ball with the
        # top edge of the screen        
        ball_vel_y = -ball_vel_y
        ball_y = 400 - 20
    # the bottom border
    if ball_y < 0:
        # we are checking to bottom edge of the ball with the
        # bottom edge of the screen          
        ball_vel_y = -ball_vel_y
        ball_y = 0

    # collisions activies:
    #   do the collision check here for both players, if the ball collides
    #       snap it back to the correct position and reverse the
    #       x velocity!
    if IsColliding(player1_x, player1_y, 16, 80, ball_x, ball_y, 24, 24):
        ball_vel_x = ball_vel_x * -1

    if IsColliding(player2_x, player2_y, 16, 80, ball_x, ball_y, 24, 24):
        ball_vel_x = ball_vel_x * -1

        
    
