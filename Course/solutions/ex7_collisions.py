from CS4HS import *

from collision import *

# creating our Graphics object
game = Graphics(640, 480)

star_x = 320 - 10
star_y = 470

paddle_x = 0
paddle_y = 0

label.mygame
star_y -= 1

if game.isKeyPressed(KEY_A):
    paddle_x -= 1
if game.isKeyPressed(KEY_D):
    paddle_x += 1

if IsColliding(paddle_x, paddle_y, 80, 16, star_x, star_y, 20, 20):
    star_y = 470
elif star_y < -20:
    goto .end

game.clear()
game.drawImage("star.gif", star_x, star_y)
game.drawImage("paddle.gif", paddle_x, paddle_y)
game.reveal()

goto.mygame

label .end
print ("GAME OVER!!!")
'''
Exercises:
1) When the paddle collides with the star, reset the star, otherwise end the game
'''