from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

star_x = 320 - 10
star_y = 470

paddle_x = 0
paddle_y = 0

label.mygame
star_y -= 1

if star_y < -20:
    star_y = 470

game.clear()
game.drawImage("star.gif", star_x, star_y)
game.drawImage("paddle.gif", paddle_x, paddle_y)
game.reveal()

goto.mygame

'''
Exercises:
1) Move the paddle using the 'A' and 'D' keys (left and right, respectively)
2) Extension: apply 'inertia' to the paddle
'''