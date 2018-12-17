from CS4HS import *

# creating our Graphics object
# what do the 2 numbers in the brackets mean?
game = Graphics(640, 480)

game.clear()
game.drawImage("mario.gif", 0, 0)
game.reveal()

'''
Exercises:
1) Make the screen stop disappearing!
2) Draw Mario in the DEAD CENTRE of the screen. (hint: his width is 64, and his height is 87)
'''