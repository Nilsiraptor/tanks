from pyglet.window import Window as pygletWindow
from pyglet.window import key
from pyglet.window import mouse
import pyglet

class Window(pygletWindow):
    def __init__(self, menuLoop):
        super(Window, self).__init__()

        self.menuLoop = menuLoop

    def on_draw(self):
        pass

    def on_key_press(self, symbol, modifier):
        if symbol == key.A:
            print("True")

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            #print("clicked")
            pyglet.clock.schedule_interval(self.menuLoop, 1/60)
