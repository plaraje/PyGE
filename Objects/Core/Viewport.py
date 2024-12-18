class Viewport:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.zoom = 1.0

    def contains(self, entity):
        return (self.x <= entity.x <= self.x + self.width and
                self.y <= entity.y <= self.y + self.height)

    def get_relative_position(self, x, y):
        return (x - self.x) * self.zoom, (y - self.y) * self.zoom
