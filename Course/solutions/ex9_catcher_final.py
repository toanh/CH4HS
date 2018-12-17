from CS4HS import *

from collision import *

from random import *

# creating our Graphics object
game = Graphics(640, 480)

star_x = randint(0, 640 - 20)
star_y = 470
star_speed = 1

paddle_x = 0
paddle_y = 0

score = 0

# using GOTOs... Evil??
# Or a good scaffolding tool?
label.mygame
star_y -= star_speed

if game.isKeyPressed(KEY_A):
    paddle_x -= 1
if game.isKeyPressed(KEY_D):
    paddle_x += 1

if IsColliding(paddle_x, paddle_y, 80, 16, star_x, star_y, 20, 20):
    # resetting the star's position
    star_y = 470
    star_x = randint(0, 640 - 20)
    score += 1
    # slowly increasing its speed to ramp up difficulty
    star_speed += 0.05
elif star_y < -20:
    goto .end

game.clear()

# drawing the images
# note the order, drawn from back to front
game.drawImage("star.gif", star_x, star_y)
game.drawImage("paddle.gif", paddle_x, paddle_y)

# BUG: drawText() has to be the LAST call to game or else everything after it flickers
# AND there can only be ONE drawText call
game.drawText("Score: " + str(score), 280, 440, fontSize=20)
game.reveal()

goto.mygame

label .end
print ("GAME OVER!!!")

'''
extension ideas:
- stop the paddle at the boundaries of the screen
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