from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

mario_x = 320 - 32
mario_y = 393

label .mygame
game.clear()
game.drawImage("mario.gif", mario_x, mario_y)
game.reveal()

goto .mygame

'''
Exercises:
1) Make Mario fall down the screen
2) Extension: make him fall down the screen under the influence of gravity
'''
