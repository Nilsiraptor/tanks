import pyglet
import Game

i = 0
def gameLoop(dt):
    global i
    i += 1
    if i%60 == 0:
        print(i//60)

window = Game.Window(gameLoop)
#pyglet.clock.schedule_interval(menuLoop, 1/60)
pyglet.app.run()
