from pyglet.window import key
from pyglet.window import mouse
import pyglet

class Window(pyglet.window.Window):
    def __init__(self, gameLoop):
        super(Window, self).__init__()

        super(Window, self).set_fullscreen(True)

        self.background = pyglet.image.load("textures/background.png")

        self.gameLoop = gameLoop

        self.buttonExit = Button(660, 100, 600, 50, "textures/button.png")
        self.buttonStart = Button(660, 500, 600, 50, "textures/button.png")
        self.buttonSettings = Button(660, 300, 600, 50, "textures/button.png")

    def on_draw(self):
        self.background.blit(0, 0, 0)
        self.buttonExit.draw()
        self.buttonStart.draw()
        self.buttonSettings.draw()

    def on_key_press(self, symbol, modifier):
        if symbol == key.A:
            print("True")
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.buttonExit.is_clicked(x, y):
                pyglet.app.exit()
            elif self.buttonStart.is_clicked(x, y):
                pyglet.clock.schedule_interval(self.gameLoop, 1/60)

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

    def is_clicked(self, x, y):
        return (x > self.x and x < self.x+self.width) and (y > self.y and y < self.y + self.height)
