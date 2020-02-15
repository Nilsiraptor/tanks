import pyglet

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
