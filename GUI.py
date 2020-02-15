from pyglet.window import key
from pyglet.window import mouse
import pyglet

class Window(pyglet.window.Window):
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
            pass
            #print("clicked")
            #pyglet.clock.schedule_interval(self.gameLoop, 1/60)

class Button():
    def __init__(self, x, y, width, height, texture=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if texture == None:
            self.texture = None
        else:
            self.texture = pyglet.image.load(texture)
            self.texture = self.texture.get_region(0, 0, self.width, self.height)

    def draw(self):
        if self.texture != None:
            self.texture.blit(self.x, self.y, 0, self.width, self.height)
