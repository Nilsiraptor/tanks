import pyglet
import Game

window = Game.Window()
pyglet.clock.schedule_interval(Game.menuLoop, 1/60)
pyglet.app.run()
