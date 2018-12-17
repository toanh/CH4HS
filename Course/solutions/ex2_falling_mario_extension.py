from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

mario_x = 320 - 32
mario_y = 393

mario_speed = 0

label .mygame
mario_speed += 0.01
mario_y -= mario_speed
game.clear()
game.drawImage("mario.gif", mario_x, mario_y)
game.reveal()

goto .mygame

