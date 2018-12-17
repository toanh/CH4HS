from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

star_x = 320 - 10
star_y = 470

label .mygame
star_y -= 1

if star_y < -20:
    star_y = 470

game.clear()
game.drawImage("star.gif", star_x, star_y)
game.reveal()

goto .mygame