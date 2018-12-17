from CS4HS import *

# creating our Graphics object
game = Graphics(640, 480)

label .mygame
game.clear()
game.drawImage("mario.gif", 320 - 32, 240 - 44)
game.reveal()

goto .mygame
