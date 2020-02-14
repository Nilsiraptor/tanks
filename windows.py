import pyglet.window.Window
from pyglet.window import key

class Window(pyglet.window.Window):
    def __init__(self):
        super(MenuWindow, self).__init__()

    def on_draw(self):
        pass

    def on_key_press(self, symbol, modifier):
        if symbol == key.A:
            print("True")
