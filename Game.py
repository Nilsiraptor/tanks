from pyglet.window import Window as pygletWindow
from pyglet.window import key

class Window(pygletWindow):
    def __init__(self):
        super(Window, self).__init__()

    def on_draw(self):
        pass

    def on_key_press(self, symbol, modifier):
        if symbol == key.A:
            print("True")


i = 0
def menuLoop(dt):
    global i
    i += 1
    if i%60 == 0:
        print(i//60)
