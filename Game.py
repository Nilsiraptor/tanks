from pyglet.window import Window as pygletWindow
from pyglet.window import key
from pyglet.window import mouse
import pyglet
from Button import Button

class Window(pygletWindow):
    def __init__(self, gameLoop):
        super(Window, self).__init__()

        super(Window, self).set_fullscreen(True)

        self.background = pyglet.image.load("textures/background.png")

        self.gameLoop = gameLoop
        self.buttons = [Button(960 - 300, 100 + i*100, 600, 50, "textures/button.png") for i in range(3)]

    def on_draw(self):
        self.background.blit(0, 0, 0)
        for b in self.buttons:
            b.draw()

    def on_key_press(self, symbol, modifier):
        if symbol == key.A:
            print("True")
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            #print("clicked")
            pyglet.clock.schedule_interval(self.gameLoop, 1/60)
