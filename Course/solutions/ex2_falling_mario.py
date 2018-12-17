from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

mario_x = 320 - 32
mario_y = 393

label .mygame
mario_y -= 1
game.clear()
game.drawImage("mario.gif", mario_x, mario_y)
game.reveal()

goto .mygame

