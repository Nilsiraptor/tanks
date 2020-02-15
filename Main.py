import pyglet
import GUI

def gameLoop(dt):
    print("Game started!")

window = GUI.Window(gameLoop)

pyglet.app.run()
